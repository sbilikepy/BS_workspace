# Generated by Django 4.1.7 on 2023-08-10 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0010_rename_authors_book_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ManyToManyField(to='db.author'),
        ),
    ]