# Generated by Django 4.1.7 on 2023-08-22 23:46

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "bus_station",
            "0006_user_alter_trip_source_alter_ticket_unique_together_and_more",
        ),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="ticket",
            unique_together=set(),
        ),
        migrations.AddConstraint(
            model_name="ticket",
            constraint=models.UniqueConstraint(
                fields=("trip", "seat"), name="unique trip and seat combination"
            ),
        ),
    ]
