# Generated by Django 4.1.1 on 2023-02-26 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0010_productmodel_create_at"),
    ]

    operations = [
        migrations.AddField(
            model_name="productmodel",
            name="category_name",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
