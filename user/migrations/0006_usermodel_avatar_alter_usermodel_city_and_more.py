# Generated by Django 4.1.1 on 2022-12-10 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0005_alter_usermodel_phone"),
    ]

    operations = [
        migrations.AddField(
            model_name="usermodel",
            name="avatar",
            field=models.ImageField(
                blank=True, null=True, upload_to="user-images", verbose_name="Аватарка"
            ),
        ),
        migrations.AlterField(
            model_name="usermodel",
            name="city",
            field=models.CharField(
                blank=True, max_length=100, null=True, verbose_name="Адрес доставки"
            ),
        ),
        migrations.AlterField(
            model_name="usermodel",
            name="email",
            field=models.EmailField(
                max_length=100, null=True, unique=True, verbose_name="Email"
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
