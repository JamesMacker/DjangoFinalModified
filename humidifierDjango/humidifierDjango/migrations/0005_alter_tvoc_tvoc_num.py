# Generated by Django 4.1 on 2024-04-07 19:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("humidifierDjango", "0004_tvoc_delete_airquality"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tvoc",
            name="tvoc_num",
            field=models.DecimalField(decimal_places=1, max_digits=4),
        ),
    ]
