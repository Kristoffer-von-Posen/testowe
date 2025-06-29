from django.shortcuts import render

# Create your views here.


def index(request):
  return render(request, "java/index.html")


def snake(request):
  return render(request, "java/snake.html")
