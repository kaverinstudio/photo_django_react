# Generated by Django 4.1.1 on 2023-01-25 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0006_productphoto_for_category"),
    ]

    operations = [
        migrations.AlterField(
            model_name="productphoto",
            name="for_category",
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
