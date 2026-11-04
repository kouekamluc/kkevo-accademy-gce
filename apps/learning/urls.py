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
    path("planner/sessions/<int:pk>/edit/", views.session_edit, name="session_edit"),
    path("planner/exam-date/", views.exam_date, name="exam_date"),
    path("planner/rest-day/", views.rest_day, name="rest_day"),
    path("links/<str:purpose>/", views.private_link, name="private_link"),
    path("calendar/<str:token>.ics", views.calendar_feed, name="calendar_feed"),
    path("week/", views.weekly, name="weekly"),
    path("week/goal/", views.goal_adjust, name="goal_adjust"),
    path("report/<str:token>/", views.report, name="report"),
    path("saved/", views.saved, name="saved"),
]
