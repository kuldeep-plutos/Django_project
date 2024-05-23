from django.urls import path
from . import views

app_name="polls"   # to set the application namespace
urlpatterns = [
    path("",views.index, name="Index"),
    path("<int:question_id>/",views.details,name="details"),
    path("<int:question_id>/results/",views.results,name="results"),
    path("<int:question_id>/vote/",views.vote,name="vote"),
]