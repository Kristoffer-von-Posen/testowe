from django.db import models

# Create your models here.


class user_add(models.Model):
  name = models.CharField(max_length=32)
  password = models.CharField(max_length=32)

  def __str__(self):
    return f"{self.name}"
