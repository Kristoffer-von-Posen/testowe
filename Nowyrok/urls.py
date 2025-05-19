from django.urls import path

from . import views

app_name = "Nowyrok"
urlpatterns = [
    path('', views.index, name='index'),
]
