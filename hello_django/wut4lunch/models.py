from django.db import models

# Create your models here.

class Lunch(models.Model):
    submitter = models.CharField(max_length=63)
    food = models.CharField(max_length=255)
