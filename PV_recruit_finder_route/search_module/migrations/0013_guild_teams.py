# Generated by Django 4.0.2 on 2023-12-22 04:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('search_module', '0012_alter_team_team_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='guild',
            name='teams',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='teams', to='search_module.team'),
        ),
    ]
