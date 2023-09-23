from django.db import models
from PIL import Image
import os
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.core.files.base import ContentFile

class Portfolio(models.Model):
    category = models.CharField(max_length=100, blank=True, null=True, verbose_name='Категория фотографии')

    def __str__(self):
        return f'{self.category}'

    class Meta:
        verbose_name = 'Фотография в портфолио'
        verbose_name_plural = 'Фотографии в портфолио'


class PortfolioPhoto(models.Model):
    active = models.ForeignKey(Portfolio, on_delete=models.CASCADE, related_name='images')
    src = models.ImageField(upload_to='', verbose_name='Миниатюра', blank=True, null=True)
    width = models.PositiveBigIntegerField(blank=True, null=True)
    height = models.PositiveBigIntegerField(blank=True, null=True)
    photo = models.ImageField(upload_to='portfolio', verbose_name='Фотография')
    photo_desc = models.CharField(max_length=100, blank=True, null=True, verbose_name='Описание фотографии')

        
@receiver(pre_save, sender=PortfolioPhoto)
def create_thumbnail(sender, instance, **kwargs):
    if instance.photo:
        img = Image.open(instance.photo)

        thumbnail_size = (500, 500) 
        img.thumbnail(thumbnail_size)
        
        instance.width = img.width 
        instance.height = img.height

        thumbnail_name = f"portfolio/thumb/{os.path.basename(instance.photo.name)}"
        
        thumbnail_tmp = ContentFile(b'')
        img.save(thumbnail_tmp, 'JPEG')

        instance.src.save(thumbnail_name, thumbnail_tmp, save=False)

