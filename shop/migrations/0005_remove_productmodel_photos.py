# Generated by Django 4.1.1 on 2023-01-25 16:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0004_alter_productmodel_photos"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="productmodel",
            name="photos",
        ),
    ]
