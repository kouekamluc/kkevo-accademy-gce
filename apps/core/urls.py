from django.urls import path

from . import pwa, views

app_name = "core"

urlpatterns = [
    path("", views.landing, name="landing"),
    path("how-it-works/", views.how_it_works, name="how_it_works"),
    path("manifest.webmanifest", pwa.manifest, name="manifest"),
    path("sw.js", pwa.service_worker, name="service_worker"),
    path("offline/", pwa.offline, name="offline"),
    path("about/", views.about, name="about"),
]
