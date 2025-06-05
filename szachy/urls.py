from django.urls import path
from . import views

app_name = "szachy"
urlpatterns = [
    path("", views.index, name="index"),
]
