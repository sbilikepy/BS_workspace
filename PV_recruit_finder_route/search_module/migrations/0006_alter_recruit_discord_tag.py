# Generated by Django 4.0.2 on 2023-12-29 07:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("search_module", "0005_recruit_discord_tag"),
    ]

    operations = [
        migrations.AlterField(
            model_name="recruit",
            name="discord_tag",
            field=models.CharField(default="unknown", max_length=255),
        ),
    ]
