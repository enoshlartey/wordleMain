from django.urls import path
from . import views

app_name = "fourLetters"

urlpatterns = [
    path("four/", views.index_view, name="index")
]