# Generated by Django 4.1.7 on 2023-08-07 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='company_name',
            field=models.CharField(default='noname', max_length=255),
        ),
    ]