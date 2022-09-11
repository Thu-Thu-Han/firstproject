from django.db import models

# Create your models here.

class Student(models.Model):
    roll = models.CharField(max_length=200)
    name = models.CharField(max_length=200)