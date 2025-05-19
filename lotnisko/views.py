from django.shortcuts import render
from .models import lot, lotnisko, pasazer
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.


def index(request):
  return render(request, "lotnisko/index.html", {"Flieg": lot.objects.all()})


def lott(request, lot_id):
  lota = lot.objects.get(pk=lot_id)
  return render(
      request, "lotnisko/lott.html", {
          "lot": lota,
          "pasazerowie": lota.passengers.all(),
          "non_passengers": pasazer.objects.exclude(flights=lota).all()
      })


def book(request, lot_id):
  if request.method == "POST":
    flight = lot.objects.get(pk=lot_id)
    passenger = pasazer.objects.get(pk=int(request.POST["passenger"]))
    passenger.flights.add(flight)
    return HttpResponseRedirect(reverse("lotnisko:lott", args=(flight.id, )))
