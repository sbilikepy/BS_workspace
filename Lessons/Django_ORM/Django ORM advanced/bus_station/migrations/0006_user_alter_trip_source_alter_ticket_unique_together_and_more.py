# Generated by Django 4.1.7 on 2023-08-22 23:27

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("bus_station", "0005_alter_trip_source"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("username", models.CharField(max_length=63, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name="trip",
            name="source",
            field=models.CharField(max_length=63),
        ),
        migrations.AlterUniqueTogether(
            name="ticket",
            unique_together={("trip", "seat")},
        ),
        migrations.AddIndex(
            model_name="trip",
            index=models.Index(
                fields=["source", "destination"], name="bus_station_source_5ca985_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="trip",
            index=models.Index(
                fields=["departure"], name="bus_station_departu_971b25_idx"
            ),
        ),
    ]
