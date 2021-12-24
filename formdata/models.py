from django.db import models
from django.db.models.fields import CharField, IntegerField

# Create your models here.


class student(models.Model):
    name=models.CharField(max_length=10)
    marks=models.IntegerField()

