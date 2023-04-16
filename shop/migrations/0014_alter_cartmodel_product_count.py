# Generated by Django 4.1.1 on 2023-03-08 09:03

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0013_alter_cartmodel_options_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cartmodel",
            name="product_count",
            field=models.PositiveIntegerField(
                blank=True,
                default=1,
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(1),
                    django.core.validators.MaxValueValidator(100),
                ],
            ),
        ),
    ]
