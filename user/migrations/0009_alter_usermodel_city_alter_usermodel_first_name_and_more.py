# Generated by Django 4.1.1 on 2023-01-08 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0008_alter_usermodel_city_alter_usermodel_first_name_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="usermodel",
            name="city",
            field=models.TextField(
                blank=True, max_length=100, null=True, verbose_name="Адрес доставки"
            ),
        ),
        migrations.AlterField(
            model_name="usermodel",
            name="first_name",
            field=models.CharField(
                blank=True, max_length=64, null=True, verbose_name="Имя"
            ),
        ),
        migrations.AlterField(
            model_name="usermodel",
            name="last_name",
            field=models.CharField(
                blank=True, max_length=64, null=True, verbose_name="Фамилия"
            ),
        ),
        migrations.AlterField(
            model_name="usermodel",
            name="phone",
            field=models.CharField(
                blank=True, max_length=13, null=True, verbose_name="Телефон"
            ),
        ),
    ]
