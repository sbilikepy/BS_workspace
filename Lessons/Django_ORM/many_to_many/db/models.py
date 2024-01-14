from django.db import models


class LiteraryFormat(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Book(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    format = models.ForeignKey(
        LiteraryFormat, related_name="by_genre", on_delete=models.CASCADE
    )
    authors = models.ManyToManyField(Author, related_name="by_author")
