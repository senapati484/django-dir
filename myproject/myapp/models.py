from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(max_length=100)

class Items(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    image = models.URLField(max_length=200)