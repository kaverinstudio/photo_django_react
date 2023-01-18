# Generated by Django 4.1.1 on 2023-01-02 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("print", "0012_orders_orderphotos"),
    ]

    operations = [
        migrations.AddField(
            model_name="orders",
            name="email",
            field=models.CharField(
                blank=True, max_length=100, null=True, verbose_name="Email"
            ),
        ),
        migrations.AddField(
            model_name="orders",
            name="phone",
            field=models.CharField(
                blank=True, max_length=20, null=True, verbose_name="Телефон"
            ),
        ),
    ]
