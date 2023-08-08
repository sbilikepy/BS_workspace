from django.db import models


class Company(models.Model):
    description = models.TextField(blank=True)
    company_name = models.CharField(max_length=255, default="noname",
                                    unique=True)

    def __str__(self):
        return f"{self.name}, {self.description}"