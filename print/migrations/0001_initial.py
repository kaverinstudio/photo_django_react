# Generated by Django 4.1.1 on 2022-12-11 16:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="PapierType",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "papier_width",
                    models.PositiveIntegerField(
                        blank=True, unique=True, verbose_name="Ширина"
                    ),
                ),
                (
                    "papier_height",
                    models.PositiveIntegerField(
                        blank=True, unique=True, verbose_name="Высота"
                    ),
                ),
                (
                    "papier_type",
                    models.CharField(
                        blank=True, max_length=50, verbose_name="Тип бумаги"
                    ),
                ),
            ],
            options={
                "verbose_name": "Тип фотографии",
                "verbose_name_plural": "Типы фоторафий",
            },
        ),
        migrations.CreateModel(
            name="Services",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(blank=True, max_length=50, verbose_name="Услуга"),
                ),
                (
                    "price",
                    models.PositiveBigIntegerField(
                        blank=True, null=True, verbose_name="Цена"
                    ),
                ),
                (
                    "papier",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        to="print.papiertype",
                        verbose_name="Тип бумаги",
                    ),
                ),
            ],
            options={
                "verbose_name": "Услуга",
                "verbose_name_plural": "Услуги",
            },
        ),
    ]
