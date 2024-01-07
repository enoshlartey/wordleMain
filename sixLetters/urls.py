from django.urls import path
from . import views

app_name = "sixLetters"

urlpatterns = [
    path("six/", views.indexView, name="index")
]