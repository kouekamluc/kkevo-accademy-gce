from django.urls import path

from . import views

app_name = "learning"

urlpatterns = [
    path("progress/", views.progress, name="progress"),
    path("progress/add-to-planner/", views.add_suggestions, name="add_suggestions"),
    path("planner/", views.planner, name="planner"),
    path("planner/sessions/new/", views.session_create, name="session_create"),
    path("planner/sessions/<int:pk>/toggle/", views.session_toggle, name="session_toggle"),
    path("planner/sessions/<int:pk>/delete/", views.session_delete, name="session_delete"),
    path("saved/", views.saved, name="saved"),
]
