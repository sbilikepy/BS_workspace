# Generated by Django 4.1.7 on 2023-08-08 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0010_caffe_name_alter_place_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='post_index',
            field=models.IntegerField(),
        ),
    ]
