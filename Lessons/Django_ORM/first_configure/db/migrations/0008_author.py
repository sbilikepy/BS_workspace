# Generated by Django 4.1.7 on 2023-08-10 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0007_alter_book_format'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
            ],
        ),
    ]
