# Generated by Django 4.1.7 on 2023-08-08 01:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0011_alter_place_post_index'),
    ]

    operations = [
        migrations.AlterField(
            model_name='caffe',
            name='place',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.place', unique=True),
        ),
    ]
