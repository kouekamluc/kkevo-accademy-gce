"""Small cache-based rate limiter for login and password-reset requests.

A fixed window starts at the first counted event; once `limit` events have been
counted the key stays blocked until the window expires. Keys are hashed so no
email address or IP is stored in the cache in clear text.

Uses the default cache. With several worker processes, set CACHE_URL to a shared
cache (database, Redis or Memcached) so the limit is shared too.
"""

import hashlib
import math
import time

from django.conf import settings
from django.core.cache import cache


def client_ip(request):
    """The client's IP. Reads X-Forwarded-For only when we sit behind trusted proxies."""
    proxies = getattr(settings, "TRUSTED_PROXY_COUNT", 0)
    if proxies:
        forwarded = [p.strip() for p in request.META.get("HTTP_X_FORWARDED_FOR", "").split(",") if p.strip()]
        if len(forwarded) >= proxies:
            return forwarded[-proxies]
    return request.META.get("REMOTE_ADDR", "")


class RateLimit:
    def __init__(self, scope, *parts, limit, window):
        digest = hashlib.sha256("|".join(str(p) for p in parts).encode()).hexdigest()[:32]
        self.key = f"ratelimit:{scope}:{digest}"
        self.limit = limit
        self.window = window

    def _state(self):
        return cache.get(self.key) or {"count": 0, "started": time.time()}

    @property
    def count(self):
        return self._state()["count"]

    @property
    def remaining(self):
        return max(0, self.limit - self.count)

    def is_blocked(self):
        return self.count >= self.limit

    def retry_after_minutes(self):
        state = self._state()
        seconds_left = state["started"] + self.window - time.time()
        return max(1, math.ceil(seconds_left / 60))

    def hit(self):
        state = self._state()
        state["count"] += 1
        timeout = max(1, math.ceil(state["started"] + self.window - time.time()))
        cache.set(self.key, state, timeout)
        return state["count"]

    def reset(self):
        cache.delete(self.key)


def login_limiter(request, email):
    return RateLimit(
        "login", (email or "").strip().lower(), client_ip(request),
        limit=settings.LOGIN_RATE_LIMIT_ATTEMPTS, window=settings.LOGIN_RATE_LIMIT_WINDOW,
    )


def password_reset_limiter(request):
    return RateLimit(
        "password-reset", client_ip(request),
        limit=settings.PASSWORD_RESET_RATE_LIMIT, window=settings.PASSWORD_RESET_RATE_LIMIT_WINDOW,
    )
