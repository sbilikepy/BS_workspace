# Generated by Django 4.1.7 on 2023-08-07 23:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("db", "0004_book"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="title",
            field=models.CharField(default="Unknown", max_length=255),
        ),
    ]
