from django.shortcuts import render


def index(request):
  return render(request, 'helloworld/index.html')


def insult(request, name):
  return render(request, 'helloworld/insult.html', {'name': name.capitalize()})


def insultbase(request):
  return render(request, 'helloworld/insultbase.html')


# Create your views here.
