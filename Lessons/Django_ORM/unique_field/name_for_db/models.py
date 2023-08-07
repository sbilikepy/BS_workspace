from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField(default = 1)