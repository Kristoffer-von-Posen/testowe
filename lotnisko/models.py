from django.db import models

# Create your models here.


# klasa opisujaca lotniska
class lotnisko(models.Model):
  code = models.CharField(max_length=3)
  city = models.CharField(max_length=64)

  def __str__(self):
    return f"{self.city} ({self.code})"


# klasa opisujaca loty
class lot(models.Model):
  origin = models.ForeignKey(lotnisko,
                             on_delete=models.CASCADE,
                             related_name="departures")
  destination = models.ForeignKey(lotnisko,
                                  on_delete=models.CASCADE,
                                  related_name="arrivals")
  duration = models.IntegerField()

  def __str__(self):
    return f"{self.id}: {self.origin} to {self.destination}"


# klasa pasazer
class pasazer(models.Model):
  imie = models.CharField(max_length=64)
  nazwisko = models.CharField(max_length=64)
  flights = models.ManyToManyField(lot, blank=True, related_name="passengers")

  def __str__(self):
    return f"{self.imie} {self.nazwisko}"
