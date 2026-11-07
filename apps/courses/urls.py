from django.urls import path

from . import lesson_views, views

app_name = "courses"

urlpatterns = [
    path("subjects/", views.catalog, name="catalog"),
    path("my-subjects/", views.my_subjects, name="my_subjects"),
    path("my-subjects/add-class/", views.add_class_subjects, name="add_class_subjects"),
    path("my-subjects/<int:offering_pk>/toggle/", views.toggle_plan, name="toggle_plan"),
    path("continue/", views.continue_learning, name="continue"),
    path("courses/<slug:slug>/", views.course_detail, name="detail"),
    path("courses/<slug:slug>/path/", views.course_path, name="path"),
    path("courses/<slug:course_slug>/lessons/<int:pk>/", lesson_views.lesson_detail, name="lesson"),
    path("courses/<slug:course_slug>/lessons/<int:pk>/complete/", lesson_views.lesson_complete, name="lesson_complete"),
    path("courses/<slug:course_slug>/lessons/<int:pk>/heartbeat/", lesson_views.lesson_heartbeat, name="lesson_heartbeat"),
    path("courses/<slug:course_slug>/lessons/<int:pk>/save/", lesson_views.lesson_save, name="lesson_save"),
    path("courses/<slug:course_slug>/lessons/<int:pk>/notes/", lesson_views.lesson_note, name="lesson_note"),
    path("courses/<slug:course_slug>/lessons/<int:pk>/notes/<int:note_pk>/delete/", lesson_views.lesson_note_delete,
         name="lesson_note_delete"),
]
