from django.urls import path

from . import views

app_name = "lotnisko"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:lot_id>", views.lott, name="lott"),
    path("<int:lot_id>/book", views.book, name="book")
]
