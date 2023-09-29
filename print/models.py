from django.db import models
from .utils import user_directory_path
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.core.files.base import ContentFile
from PIL import Image
import os


class Services(models.Model):
    name = models.CharField(max_length=50, blank=True, null=False, verbose_name='Услуга')
    price = models.PositiveBigIntegerField(
        blank=True, null=True, verbose_name='Цена')

    papier_size = models.ForeignKey('PapierSize', on_delete=models.PROTECT, verbose_name='Размер фотографии', null=True,
                                    blank=True)
    papier_type = models.ForeignKey('PapierType', on_delete=models.PROTECT, verbose_name='Тип бумаги', null=True,
                                    blank=True)

    def __str__(self) -> str:
        return f'{self.name}'

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'


class PapierSize(models.Model):
    papier_width = models.PositiveIntegerField(blank=True, null=False, verbose_name='Ширина')
    papier_height = models.PositiveIntegerField(blank=True, null=False, verbose_name='Высота')

    def __str__(self):
        return f'{self.papier_width} x {self.papier_height}'

    class Meta:
        verbose_name = 'Размер фотографии'
        verbose_name_plural = 'Размеры фоторафий'

    @classmethod
    def get_papier_sizes(cls):
        return f'{cls.papier_width} x {cls.papier_height}'


class PapierType(models.Model):
    papier_type = models.CharField(max_length=50, blank=True, null=False, verbose_name='Тип бумаги')

    def __str__(self):
        return f'{self.papier_type}'

    class Meta:
        verbose_name = 'Тип бумаги'
        verbose_name_plural = 'Типы бумаги'


class Photo(models.Model):
    # papier_size = PapierSize.objects.all()
    # papier_type = PapierType.objects.all()

    # FORMATS = []
    # TYPES = []
    
    FORMATS = [('10x15', '10x15')]
    TYPES = [('Глянцевая', 'Глянцевая')]

    # for f in papier_size:
    #     form = tuple([f'{f.papier_width}x{f.papier_height}', f'{f.papier_width}x{f.papier_height}'])
    #     FORMATS.append(form)

    # for t in papier_type:
    #     type = tuple([f'{t.papier_type}', f'{t.papier_type}'])
    #     TYPES.append(type)

    format = models.CharField(choices=FORMATS, max_length=50, default='10x15', blank=False)
    papier = models.CharField(choices=TYPES, max_length=50, default='Глянцевая', blank=False)
    file = models.ImageField(upload_to=user_directory_path, null=True)
    thumb = models.ImageField(upload_to='', blank=True, null=True)
    session_key = models.CharField(max_length=100, blank=True, null=True)
    user = models.ForeignKey('user.UserModel', on_delete=models.SET_NULL, blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True, null=True)
    count = models.PositiveIntegerField(blank=True, null=False, default=1)

    class Meta:
        verbose_name = 'Фотографии заказа'
        verbose_name_plural = 'Фотографии заказов'

    @classmethod
    def get_user_photos(cls, request):
        if request.user.is_anonymous:
            return cls.objects.filter(models.Q(session_key=request.META.get('HTTP_X_CSRFTOKEN')))
        return cls.objects.filter(models.Q(user=request.user) | models.Q(session_key=request.META.get('HTTP_X_CSRFTOKEN'))) 

    @classmethod
    def get_initial_print(cls):
        return {cls.papier_size, cls.papier_type}
    
@receiver(pre_save, sender=Photo)
def create_thumbnail(sender, instance, **kwargs):
    if instance.file:
        img = Image.open(instance.file)

        thumbnail_size = (400, 400) 
        img.thumbnail(thumbnail_size)
        
        instance.width = img.width 
        instance.height = img.height

        thumbnail_name = f"orders/thumb/{os.path.basename(instance.file.name)}"
        
        thumbnail_tmp = ContentFile(b'')
        img.save(thumbnail_tmp, 'JPEG')

        instance.thumb.save(thumbnail_name, thumbnail_tmp, save=False)


class Orders(models.Model):
    user = models.ForeignKey('user.UserModel', on_delete=models.CASCADE, blank=True, null=True)
    first_name = models.CharField(max_length=60, blank=True, null=True, verbose_name='Имя заказчика')
    last_name = models.CharField(max_length=60, blank=True, null=True, verbose_name='Фамилия заказчика')
    phone = models.CharField(max_length=20, blank=True, null=True, verbose_name='Телефон')
    email = models.CharField(max_length=100, blank=True, null=True, verbose_name='Email')
    delivery = models.CharField(max_length=20, blank=True, null=True, verbose_name='Способ доставки')
    address = models.TextField(max_length=100, blank=True, null=True, verbose_name='Адрес доставки')
    comments = models.TextField(max_length=200, blank=True, null=True, verbose_name='Комментарии к заказу')
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время заказа')
    file_field = models.FileField(upload_to='', blank=True, null=True)
    link = models.FilePathField(blank=True, null=True, allow_folders=True, verbose_name='Папка с заказом')

    def __str__(self):
        return f'{self.first_name}'

    class Meta:
        verbose_name = 'Сформированный заказ'
        verbose_name_plural = 'Сформированные заказы'


class OrderPhotos(models.Model):
    order = models.ForeignKey(Orders, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    count = models.CharField(max_length=10, blank=True, null=True)
    price = models.CharField(max_length=10, blank=True, null=True)
