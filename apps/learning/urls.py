from django.urls import path

from . import views

app_name = "learning"

urlpatterns = [
    path("planner/sessions/<int:pk>/toggle/", views.session_toggle, name="session_toggle"),
]
