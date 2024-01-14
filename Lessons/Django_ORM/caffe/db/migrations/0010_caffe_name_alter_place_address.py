# Generated by Django 4.1.7 on 2023-08-08 01:05

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("db", "0009_rename_caffee_caffe_place_address"),
    ]

    operations = [
        migrations.AddField(
            model_name="caffe",
            name="name",
            field=models.CharField(default="unknown", max_length=255),
        ),
        migrations.AlterField(
            model_name="place",
            name="address",
            field=models.CharField(default="no location", max_length=255),
        ),
    ]
