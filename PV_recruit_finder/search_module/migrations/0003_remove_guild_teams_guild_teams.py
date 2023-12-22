# Generated by Django 4.0.2 on 2023-12-19 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search_module', '0002_plannedactivity_by_team'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='guild',
            name='teams',
        ),
        migrations.AddField(
            model_name='guild',
            name='teams',
            field=models.ManyToManyField(blank=True, default=None, null=True, related_name='teams', to='search_module.Team'),
        ),
    ]