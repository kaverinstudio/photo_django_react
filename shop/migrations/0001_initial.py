# Generated by Django 4.1.1 on 2023-01-24 16:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ProductCategoryModel",
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
                    "category_name",
                    models.CharField(
                        blank=True,
                        max_length=100,
                        null=True,
                        verbose_name="Категория товара",
                    ),
                ),
                (
                    "category_slug",
                    models.SlugField(
                        blank=True, max_length=255, null=True, verbose_name="URL"
                    ),
                ),
            ],
            options={
                "verbose_name": "Категория товара",
                "verbose_name_plural": "Категории товаров",
            },
        ),
        migrations.CreateModel(
            name="ProductModel",
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
                    "product_name",
                    models.CharField(
                        blank=True,
                        max_length=50,
                        null=True,
                        verbose_name="Наименование товара",
                    ),
                ),
                (
                    "manufactured",
                    models.CharField(
                        blank=True,
                        max_length=50,
                        null=True,
                        verbose_name="Производитель",
                    ),
                ),
                (
                    "view_count",
                    models.PositiveBigIntegerField(
                        blank=True, null=True, verbose_name="Количество просмотров"
                    ),
                ),
                (
                    "rating",
                    models.IntegerField(blank=True, null=True, verbose_name="Рейтинг"),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True,
                        max_length=1000,
                        null=True,
                        verbose_name="Описание товара",
                    ),
                ),
                (
                    "price",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        max_digits=10,
                        null=True,
                        verbose_name="Цена",
                    ),
                ),
                (
                    "product_slug",
                    models.SlugField(
                        blank=True, max_length=255, null=True, verbose_name="URL"
                    ),
                ),
                (
                    "available",
                    models.BooleanField(default=True, verbose_name="В наличии"),
                ),
            ],
            options={
                "verbose_name": "Товар в магазине",
                "verbose_name_plural": "Товары в магазине",
            },
        ),
        migrations.CreateModel(
            name="ProductPhoto",
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
                    "photo",
                    models.ImageField(
                        upload_to="shop-images", verbose_name="Фотография товара"
                    ),
                ),
                (
                    "for_product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="product_images",
                        to="shop.productmodel",
                    ),
                ),
            ],
        ),
    ]
