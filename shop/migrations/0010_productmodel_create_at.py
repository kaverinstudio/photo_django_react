# Generated by Django 4.1.1 on 2023-02-25 16:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0009_remove_shopordermodel_link_shopordermodel_products"),
    ]

    operations = [
        migrations.AddField(
            model_name="productmodel",
            name="create_at",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
    ]