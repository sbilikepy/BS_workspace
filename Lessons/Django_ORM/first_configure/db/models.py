from django.db import models


class LiteraryFromat(models.Model):
    format = models.CharField(max_length=63)  # descriptor
    # self = row from table?
