# Generated by Django 4.1.7 on 2023-08-11 17:50

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("db", "0015_alter_book_authors"),
    ]

    operations = [
        migrations.RenameField(
            model_name="literaryformat",
            old_name="format",
            new_name="name",
        ),
    ]
