# Generated by Django 4.1.7 on 2023-08-11 18:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0016_rename_format_literaryformat_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='literaryformat',
            old_name='name',
            new_name='format',
        ),
    ]
