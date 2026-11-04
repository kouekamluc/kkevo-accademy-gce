from django.urls import path

from apps.core.views import planned

app_name = "courses"

# Implemented in milestone 3 (catalog & course overview).
urlpatterns = [
    path("subjects/", planned, {"page": "Explore subjects"}, name="catalog"),
    path("courses/<slug:slug>/", planned, {"page": "Course overview"}, name="detail"),
]
