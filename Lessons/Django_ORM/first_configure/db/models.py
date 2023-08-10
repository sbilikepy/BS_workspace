from django.db import models


class LiteraryFormat(models.Model):
    format = (models.CharField
        (
        max_length=63,
    )
    )  # descriptor

    # self = row from table?
    def __repr__(self):
        return str(self.format)

class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Book(models.Model):
    title = models.CharField(max_length=255, default="Unknown")
    price = models.DecimalField(max_digits=7, decimal_places=2)
    format = models.ForeignKey(
        LiteraryFormat,
        on_delete=models.CASCADE, related_name="by_format"
        # on_delete MANDATORY for ForeignKey
        # CASCADE will delete all related rows
        # PROTECT / DO_NOTHING
        # BE CAREFUL, sometimes SET_NULL bette ->(null=True)
    ) # ForeignKey MANY to ONE

    authors = models.ManyToManyField(Author,related_name="by_author")


    def __repr__(self):
        return (f"{self.title} {self.price} "
                f"{self.format.format}")


