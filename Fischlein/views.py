from django.shortcuts import render
from .models import Fisch


# Create your views here.
def index(request):
  return render(request, "Fischlein/index.html")


def slowo(request, id_s):
  return render(request, "Fischlein/slowo.html",
                {"Fisch": Fisch.objects.get(id=id_s)})
