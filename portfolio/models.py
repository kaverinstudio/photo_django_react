from django.db import models
from PIL import Image


class Portfolio(models.Model):
    category = models.CharField(max_length=100, blank=True, null=True, verbose_name='Категория фотографии')

    def __str__(self):
        return f'{self.category}'

    class Meta:
        verbose_name = 'Фотография в портфолио'
        verbose_name_plural = 'Фотографии в портфолио'


class PortfolioPhoto(models.Model):
    active = models.ForeignKey(Portfolio, on_delete=models.CASCADE, related_name='images')
    src = models.ImageField(upload_to='portfolio', verbose_name='Фотография')
    width = models.PositiveBigIntegerField(blank=True, null=True)
    height = models.PositiveBigIntegerField(blank=True, null=True)
    photo_desc = models.CharField(max_length=100, blank=True, null=True, verbose_name='Описание фотографии')

    def save(self, *args, **kwargs):
        with Image.open(self.src) as img:
            self.width, self.height = img.size
        super(PortfolioPhoto, self).save(*args, **kwargs)

