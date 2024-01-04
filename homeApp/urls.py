from django.urls import path
from . import views

app_name = "home"

urlpatterns = [
    path("", views.homeView, name="home"),
    path("selection/", views.selectView, name="select")
]