from django.urls import path

from apps.core.views import planned

app_name = "dashboard"

# Implemented in milestone 4 (student dashboard).
urlpatterns = [
    path("", planned, {"page": "Dashboard"}, name="home"),
]
