from django.db import models

# Create your models here.


# klasa zawierajaca fiszki uwu
class Fisch(models.Model):
  niem = models.CharField(max_length=64)
  tlum = models.CharField(max_length=64)

  def __str__(self):
    return f"{self.niem} znaczy {self.tlum}"
