# Generated by Django 4.0.2 on 2023-12-22 04:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('search_module', '0016_alter_user_guild'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='guild',
            field=models.ForeignKey(blank=True, default=777, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='users_guild', to='search_module.guild'),
        ),
    ]
