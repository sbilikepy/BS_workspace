from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class LiteraryFormat(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("name",)


class Author(AbstractUser):
    class Meta:
        ordering = ("username",)


class Book(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    format = models.ForeignKey(
        LiteraryFormat,
        on_delete=models.CASCADE,
        related_name="books"
    )
    authors: list = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="books"
    )

    class Meta:
        ordering = ("title", )

    def __str__(self):
        return f"{self.title} (price: {self.price}, format:{self.format.name})"
