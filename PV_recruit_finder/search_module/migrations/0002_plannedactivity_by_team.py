# Generated by Django 4.0.2 on 2023-12-19 16:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('search_module', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='plannedactivity',
            name='by_team',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='search_module.team'),
        ),
    ]