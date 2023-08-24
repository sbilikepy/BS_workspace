<<<<<<< HEAD
from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import UniqueConstraint
=======
from django.db import models
>>>>>>> e105492d111a88feb65c4f7d51e4d6554ce7df4a


class Bus(models.Model):
    info = models.CharField(max_length=255, null=True)
    num_seats = models.IntegerField()

<<<<<<< HEAD
    class Meta:
        # db_table = "bus"    # db_table = db/tables/new_name
        verbose_name = "bus"
        verbose_name_plural = "buses"

=======
>>>>>>> e105492d111a88feb65c4f7d51e4d6554ce7df4a
    def __str__(self):
        return self.info


class Trip(models.Model):
<<<<<<< HEAD
    source = models.CharField(max_length=63)  # db_index=True
=======
    source = models.CharField(max_length=63)
>>>>>>> e105492d111a88feb65c4f7d51e4d6554ce7df4a
    destination = models.CharField(max_length=63)
    departure = models.DateTimeField()
    bus = models.ForeignKey("Bus", on_delete=models.CASCADE)

<<<<<<< HEAD
    class Meta:
        # TREE STRUCTURE |   Find O(logN), Insert O(logN) #with index
        # List           |   Find O(N), Insert O(1) #without index
        # index_together = ["source", "destination"]
        indexes = [
            models.Index(fields=["source", "destination"]),
            models.Index(fields=["departure"])
        ]

=======
>>>>>>> e105492d111a88feb65c4f7d51e4d6554ce7df4a
    def __str__(self):
        return f"{self.source} - {self.destination} ({self.departure})"


class Ticket(models.Model):
    seat = models.IntegerField()
    trip = models.ForeignKey("Trip", on_delete=models.CASCADE)
    order = models.ForeignKey("Order", on_delete=models.CASCADE)

<<<<<<< HEAD
    class Meta:
        # unique_together = ["trip", "seat"] # combination should be unique
        constraints = [
            UniqueConstraint(fields=["trip", "seat"],
                             name="unique trip and seat combination")
        ]

    def clean(self):
        if not (1 <= self.seat <= self.trip.bus.num_seats):
            raise ValidationError(
                {"seat": f"seat must be in range "
                         f"[1, {self.trip.bus.num_seats}], not {self.seat}"}
            )
    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        """
        Call clean_fields(), clean(), validate_unique(), and
        validate_constraints() on the model. Raise a ValidationError for any
        errors that occur.
        """
        self.full_clean()
        return super(
            Ticket, self
        ).save(
            force_insert,force_update,using,update_fields
        )
=======
>>>>>>> e105492d111a88feb65c4f7d51e4d6554ce7df4a
    def __str__(self):
        return f"{self.trip} - (seat: {self.seat})"


class Order(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

<<<<<<< HEAD
    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return str(self.created_at)


class User(models.Model):
    username = models.CharField(max_length=63, unique=True)  # constraintq
=======
    def __str__(self):
        return str(self.created_at)
>>>>>>> e105492d111a88feb65c4f7d51e4d6554ce7df4a
