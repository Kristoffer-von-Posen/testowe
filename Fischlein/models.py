from django.db import models

# Create your models here.


# klasa zawierajaca fiszki uwu
class Fisch(models.Model):
  niem = models.CharField(max_length=256)
  prompt_num = models.IntegerField()

  def __str__(self):
    return f"{self.niem}"


class Prompts(models.Model):
  opis = models.CharField(max_length=256, null=True)
  chat = models.CharField(max_length=2048)

  def __str__(self):
    return f"{self.chat}"
