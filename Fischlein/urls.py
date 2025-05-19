from django.urls import path
from . import views

app_name = "Fischlein"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:id_s>", views.slowo, name="slowo")
]
