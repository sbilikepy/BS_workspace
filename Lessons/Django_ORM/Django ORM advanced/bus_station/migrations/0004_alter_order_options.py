# Generated by Django 4.1.7 on 2023-08-22 22:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bus_station', '0003_alter_bus_options_alter_bus_table'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ['-created_at']},
        ),
    ]