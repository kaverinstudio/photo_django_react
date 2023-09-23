# Generated by Django 4.1.1 on 2023-02-24 08:48

from django.db import migrations, models
import json.decoder
import json.encoder


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0008_alter_productmodel_rating_shopordermodel_cartmodel"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="shopordermodel",
            name="link",
        ),
        migrations.AddField(
            model_name="shopordermodel",
            name="products",
            field=models.JSONField(
                blank=True,
                decoder=json.decoder.JSONDecoder,
                encoder=json.encoder.JSONEncoder,
                null=True,
                verbose_name="Товары",
            ),
        ),
    ]