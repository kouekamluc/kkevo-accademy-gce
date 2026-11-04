from django.urls import path

from . import views

app_name = "practice"

urlpatterns = [
    path("", views.index, name="index"),
    path("sets/<int:pk>/", views.start_page, name="set"),
    path("sets/<int:pk>/start/", views.start, name="start"),
    path("attempts/<int:attempt>/q/<int:number>/", views.question, name="question"),
    path("attempts/<int:attempt>/results/", views.finish, name="finish"),
]
