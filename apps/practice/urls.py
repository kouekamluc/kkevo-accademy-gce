from django.urls import path

from . import views

app_name = "practice"

urlpatterns = [
    path("", views.index, name="index"),
    path("sets/<int:pk>/", views.start_page, name="set"),
    path("sets/<int:pk>/start/", views.start, name="start"),
    path("attempts/<int:attempt>/q/<int:number>/", views.question, name="question"),
    path("attempts/<int:attempt>/results/", views.finish, name="finish"),
    path("review/", views.review, name="review"),
    path("review/start/", views.review_start, name="review_start"),
    path("review/<int:session>/q/<int:number>/", views.review_question, name="review_question"),
    path("review/<int:session>/results/", views.review_finish, name="review_finish"),
]
