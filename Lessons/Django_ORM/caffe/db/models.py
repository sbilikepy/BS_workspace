from django.db import models


class Place(models.Model):
    address = models.CharField(max_length=255, default="no location")
    post_index = models.IntegerField()

    def str(self):
        return self.address


class Caffe(models.Model):
    name = models.CharField(max_length=255, default="unknown")
    place = models.OneToOneField(
        Place, on_delete=models.CASCADE
    )  # BEST PRACTICE > unique=True

    # place = models.ForeignKey(
    #     Place,
    #     unique=True,
    #     on_delete=models.CASCADE
    # )

    def __str__(self):
        return self.name
