from django.urls import path
from . import views

app_name = "fiveLetters"

urlpatterns = [
    path("five/", views.indexView, name="index")
]