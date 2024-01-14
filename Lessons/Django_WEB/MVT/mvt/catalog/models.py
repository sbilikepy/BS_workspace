from django.db import models


# Create your models here.
class SomeModel(models.Model):
    name = models.CharField(max_length=255)


class SomeModel_two(models.Model):
    age = models.CharField(max_length=255)
