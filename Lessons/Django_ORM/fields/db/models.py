from django.db import models


class Car(models.Model):
    SEGMENT = (
        ("A", "prem"),
        ("B", "mid")
    )
    brand = models.CharField(max_length=255)
    horse_power = models.IntegerField(default=0)
    creation_date = models.DateField(
        "Date, when this car was created",
        null=True) #auto_now = True
    description = models.TextField(default="wow")  # no length
    market_segment = models.CharField(
        max_length=1,
        choices=SEGMENT,
        default="A",
    )

    def __repr__(self):
        return (f"{self.id} : {self.brand}, {self.horse_power},"
                f"{self.creation_date}, {self.description}")
