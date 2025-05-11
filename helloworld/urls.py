from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('insult/<str:name>/', views.insult, name='insult'),
    path('insult/', views.insultbase, name='insultbase')
]
