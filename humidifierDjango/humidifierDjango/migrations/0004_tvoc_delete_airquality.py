# Generated by Django 4.1 on 2024-04-07 18:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("humidifierDjango", "0003_alter_humidity_humidity_num"),
    ]

    operations = [
        migrations.CreateModel(
            name="tvoc",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("tvoc_num", models.DecimalField(decimal_places=1, max_digits=3)),
            ],
        ),
        migrations.DeleteModel(
            name="airQuality",
        ),
    ]
