from django.db import models

class Alumnat(models.Model):
    name = models.CharField(max_length=500)
    surname = models.CharField(max_length=500)
    age = models.CharField(max_length=500)

