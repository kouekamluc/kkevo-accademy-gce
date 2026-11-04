from django.urls import path

from . import views

app_name = "studio"

urlpatterns = [
    path("", views.lessons, name="lessons"),
    path("overview/", views.overview, name="overview"),
    path("lessons/bulk/", views.bulk, name="bulk"),
    path("lessons/new/", views.lesson_new, name="new"),
    path("lessons/<int:pk>/", views.lesson_edit, name="edit"),
    path("lessons/<int:pk>/status/", views.lesson_status, name="status"),
    path("lessons/<int:pk>/changes/", views.lesson_changes, name="changes"),
    path("lessons/<int:pk>/history/", views.lesson_history, name="history"),
    path("lessons/<int:pk>/history/<int:number>/", views.revision_detail, name="revision"),
    path("lessons/<int:pk>/history/<int:number>/restore/", views.revision_restore, name="restore"),
    path("lessons/<int:pk>/blocks/add/", views.block_add, name="block_add"),
    path("lessons/<int:pk>/blocks/<int:block_pk>/save/", views.block_save, name="block_save"),
    path("lessons/<int:pk>/blocks/<int:block_pk>/move/", views.block_move, name="block_move"),
    path("lessons/<int:pk>/blocks/<int:block_pk>/delete/", views.block_delete, name="block_delete"),
    path("lessons/<int:pk>/blocks/<int:block_pk>/media/", views.media_picker, name="media_picker"),
    path("lessons/<int:pk>/blocks/<int:block_pk>/media/insert/", views.block_media, name="block_media"),
    path("media/", views.media_library, name="media"),
]
