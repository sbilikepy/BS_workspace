# Generated by Django 4.1.7 on 2023-08-07 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0002_company_company_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='company_name',
            field=models.CharField(default='noname', max_length=255, unique=True),
        ),
    ]
