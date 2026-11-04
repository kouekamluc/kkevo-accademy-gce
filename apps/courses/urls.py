from django.urls import path

from apps.core.views import planned

from . import views

app_name = "courses"

urlpatterns = [
    path("subjects/", views.catalog, name="catalog"),
    path("my-subjects/", views.my_subjects, name="my_subjects"),
    path("my-subjects/<int:offering_pk>/toggle/", views.toggle_plan, name="toggle_plan"),
    path("continue/", views.continue_learning, name="continue"),
    path("courses/<slug:slug>/", views.course_detail, name="detail"),
    path("courses/<slug:course_slug>/lessons/<int:pk>/", planned, {"page": "Lesson"}, name="lesson"),
]
