import json
from localStoragePy import localStoragePy
from django.db import models
from django.urls import reverse
from .utils import unique_slugify
from django.core.validators import MinValueValidator, MaxValueValidator


class ProductModel(models.Model):
    product_name = models.CharField(max_length=50, blank=True, null=True, verbose_name='Наименование товара')
    manufactured = models.CharField(max_length=50, blank=True, null=True, verbose_name='Производитель')
    category = models.ForeignKey('ProductCategoryModel', on_delete=models.PROTECT, verbose_name='Категория товара')
    # category_name = models.CharField(max_length=50, blank=True, null=True)
    sizes = models.CharField(max_length=50, blank=True, null=True, verbose_name='Размеры')
    view_count = models.PositiveBigIntegerField(blank=True, null=True, verbose_name='Количество просмотров')
    rating = models.FloatField(blank=True, null=True, verbose_name='Рейтинг')
    description = models.TextField(max_length=1000, blank=True, null=True, verbose_name='Описание товара')
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, verbose_name='Цена')
    product_slug = models.SlugField(max_length=255, blank=True, null=True, verbose_name='URL')
    available = models.BooleanField(default=True, verbose_name='В наличии')
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product_name

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_slug': self.product_slug})

    def save(self, **kwargs):
        slug_str = self.product_name
        self.category_name = str(self.category)
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


class CartModel(models.Model):
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE, verbose_name='Товар в корзине')
    product_count = models.PositiveIntegerField(blank=True, null=True, default=1, validators=[MinValueValidator(1), MaxValueValidator(100)])
    user = models.ForeignKey('user.UserModel', on_delete=models.SET_NULL, blank=True, null=True)
    session_key = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        verbose_name = 'Корзина заказа'
        verbose_name_plural = 'Корзины заказов'

    @classmethod
    def get_user_cart(cls, request):
        if request.user.is_anonymous:
            return cls.objects.filter(models.Q(session_key=request.META.get('HTTP_X_CSRFTOKEN')))
        return cls.objects.filter(models.Q(user=request.user) | models.Q(session_key=request.META.get('HTTP_X_CSRFTOKEN'))) 


class ShopOrderModel(models.Model):
    user = models.ForeignKey('user.UserModel', on_delete=models.CASCADE, blank=True, null=True)
    first_name = models.CharField(max_length=60, blank=True, null=True, verbose_name='Имя заказчика')
    last_name = models.CharField(max_length=60, blank=True, null=True, verbose_name='Фамилия заказчика')
    phone = models.CharField(max_length=20, blank=True, null=True, verbose_name='Телефон')
    email = models.CharField(max_length=100, blank=True, null=True, verbose_name='Email')
    delivery = models.CharField(max_length=20, blank=True, null=True, verbose_name='Способ доставки')
    address = models.TextField(max_length=100, blank=True, null=True, verbose_name='Адрес доставки')
    comments = models.TextField(max_length=200, blank=True, null=True, verbose_name='Комментарии к заказу')
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время заказа')
    products = models.JSONField(blank=True, null=True, encoder=json.JSONEncoder, decoder=json.JSONDecoder, verbose_name='Товары')

    def __str__(self):
        return f'{self.first_name}'

    class Meta:
        verbose_name = 'Заказ в магазине'
        verbose_name_plural = 'Заказы в магазине'



class ProductReviewsModel(models.Model):
    product = models.ForeignKey(ProductModel, on_delete=models.PROTECT, verbose_name='Товар')
    user = models.ForeignKey('user.UserModel', on_delete=models.CASCADE, blank=True, null=True)
    user_name = models.CharField(max_length=100, verbose_name='Имя пользователя')
    review_text = models.TextField(max_length=1000, verbose_name='Текст отзыва')
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)], verbose_name='Рейтинг')
    moderated = models.BooleanField(verbose_name='Отзыв прошел модерацию', null=True)
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время отзыва')
    
    def __str__(self):
        return f'{self.product.product_name}'

    class Meta:
        verbose_name = 'Отзыв о товаре'
        verbose_name_plural = 'Отзывы о товарах'