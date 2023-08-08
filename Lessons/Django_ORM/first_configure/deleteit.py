from django.db import models


class Band(models.Model):
    name = models.CharField(max_length=63)
    country = models.CharField(max_length=63,
                               blank=True)


class Album(models.Model):
    title = models.CharField(max_length=63)
    description = models.TextField(max_length=63,
                                   blank=True)
    price = models.IntegerField(
        null=True, blank=True
    )


class Concert(models.Model):
    name = models.CharField(max_length=63)
    audience = models.IntegerField(
        default=100
    )
