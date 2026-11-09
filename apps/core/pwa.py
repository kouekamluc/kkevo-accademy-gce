"""Installable app + offline lessons: web manifest, service worker, offline page.

The service worker is rendered from a template so the precache list uses real (hashed, in
production) static URLs, and its cache version changes whenever any of them changes.
"""
import hashlib
import json
import os

from django.conf import settings
from django.contrib.staticfiles import finders
from django.http import JsonResponse
from django.shortcuts import render
from django.templatetags.static import static
from django.urls import reverse
from django.utils.crypto import salted_hmac
from django.views.decorators.http import require_GET

# Bump to force every browser to drop its cached app shell.
SW_VERSION = "1"
USER_HEADER = "X-KKEVO-User"

# Paths the service worker must never touch (auth, CSRF, submissions, staff).
NEVER_CACHE_PREFIXES = ("/accounts/", "/admin/", "/studio/", "/practice/", "/sw.js")

PRECACHE_STATIC = (
    "css/app.css",
    "vendor/htmx.min.js",
    "vendor/alpine.min.js",
    "vendor/fonts/nunito-latin-wght-normal.woff2",
    "js/lesson.js",
    "js/pwa.js",
    "img/favicon.svg",
    "img/icon-192.png",
    "vendor/katex/katex.min.css",
    "vendor/katex/katex.min.js",
    "vendor/katex/auto-render.min.js",
)


def _static(path):
    try:
        return static(path)
    except ValueError:  # manifest storage without collectstatic (tests, first run)
        return f"/{settings.STATIC_URL.strip('/')}/{path}"


def _dev_asset_stamp():
    """Modified times of the precached files, only in DEBUG.

    In production the static URLs are hashed, so a changed file means a new URL and a new worker
    version. In development the URLs never change, so without this a restyled app.css would be served
    from the worker's cache-first static cache forever.
    """
    if not settings.DEBUG:
        return ""
    stamps = []
    for path in PRECACHE_STATIC:
        found = finders.find(path)
        stamps.append(str(int(os.path.getmtime(found))) if found else "-")
    return "|".join(stamps)


def user_key(user):
    """Opaque per-user token. The worker compares it so one student's cached lessons are never shown to another."""
    return salted_hmac("kkevo.pwa.user", str(user.pk)).hexdigest()[:24]


class PwaUserHeaderMiddleware:
    """Tags HTML responses for signed-in users with their opaque key (read by the service worker)."""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        user = getattr(request, "user", None)
        if user is not None and user.is_authenticated and "text/html" in response.get("Content-Type", ""):
            response[USER_HEADER] = user_key(user)
        return response


@require_GET
def manifest(request):
    data = {
        "id": "/",
        "name": "KKEVO Academy",
        "short_name": "KKEVO",
        "description": "Clear, structured lessons for the Cameroon GCE O and A Levels, readable offline.",
        "lang": "en",
        "dir": "ltr",
        "start_url": reverse("dashboard:home") + "?source=pwa",
        "scope": "/",
        "display": "standalone",
        "orientation": "portrait",
        "background_color": "#F7F5FF",
        "theme_color": "#5B3FE4",
        "categories": ["education"],
        "icons": [
            {"src": _static("img/icon-192.png"), "sizes": "192x192", "type": "image/png", "purpose": "any"},
            {"src": _static("img/icon-512.png"), "sizes": "512x512", "type": "image/png", "purpose": "any"},
            {"src": _static("img/icon-maskable-512.png"), "sizes": "512x512", "type": "image/png", "purpose": "maskable"},
        ],
    }
    response = JsonResponse(data, json_dumps_params={"indent": 2})
    response["Content-Type"] = "application/manifest+json"
    response["Cache-Control"] = "public, max-age=3600"
    return response


@require_GET
def service_worker(request):
    offline_url = reverse("core:offline")
    precache = [_static(p) for p in PRECACHE_STATIC]
    version = hashlib.sha1((SW_VERSION + "|".join(precache) + offline_url + _dev_asset_stamp()).encode()).hexdigest()[:10]
    response = render(
        request,
        "pwa/sw.js",
        {
            "version": version,
            # One static cache for the life of a production build; a new one per change in development.
            "static_cache": f"kkevo-static-{version}" if settings.DEBUG else "kkevo-static-v1",
            "offline_url": offline_url,
            "precache_json": json.dumps(precache),
            "static_prefix": "/" + settings.STATIC_URL.strip("/") + "/",
            "never_cache_json": json.dumps(list(NEVER_CACHE_PREFIXES)),
            "user_header": USER_HEADER,
        },
        content_type="text/javascript; charset=utf-8",
    )
    response["Service-Worker-Allowed"] = "/"
    response["Cache-Control"] = "no-cache, max-age=0"
    return response


@require_GET
def offline(request):
    response = render(request, "pwa/offline.html")
    response["Cache-Control"] = "no-cache"
    return response
