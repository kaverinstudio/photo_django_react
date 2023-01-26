from django.db import models
from django.urls import reverse
from .utils import unique_slugify


class ProductModel(models.Model):
    product_name = models.CharField(max_length=50, blank=True, null=True, verbose_name='Наименование товара')
    manufactured = models.CharField(max_length=50, blank=True, null=True, verbose_name='Производитель')
    category = models.ForeignKey('ProductCategoryModel', on_delete=models.PROTECT, verbose_name='Категория товара')
    view_count = models.PositiveBigIntegerField(blank=True, null=True, verbose_name='Количество просмотров')
    rating = models.IntegerField(blank=True, null=True, verbose_name='Рейтинг')
    description = models.TextField(max_length=1000, blank=True, null=True, verbose_name='Описание товара')
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, verbose_name='Цена')
    product_slug = models.SlugField(max_length=255, blank=True, null=True, verbose_name='URL')
    available = models.BooleanField(default=True, verbose_name='В наличии')

    def __str__(self):
        return self.product_name

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_slug': self.product_slug})

    def save(self, **kwargs):
        slug_str = self.product_name
        unique_slugify(self, slug_str)
        super(ProductModel, self).save(**kwargs)


    class Meta:
        verbose_name = 'Товар в магазине'
        verbose_name_plural = 'Товары в магазине'


class ProductPhoto(models.Model):
    for_product = models.ForeignKey(ProductModel, on_delete=models.CASCADE, related_name='product_images')
    for_category = models.PositiveIntegerField(blank=True, null=True)
    photo = models.ImageField(upload_to='shop-images', verbose_name='Фотография товара')

    def save(self, *args, **kwargs):
        cat_id = ProductModel.objects.get(id=self.for_product_id)
        self.for_category = cat_id.category_id
        super(ProductPhoto, self).save(*args, **kwargs)




class ProductCategoryModel(models.Model):
    category_name = models.CharField(max_length=100, blank=True, null=True, verbose_name='Категория товара')
    category_slug = models.SlugField(max_length=255, blank=True, null=True, verbose_name='URL')

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = 'Категория товара'
        verbose_name_plural = 'Категории товаров'
