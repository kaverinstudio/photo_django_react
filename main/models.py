from django.db import models

class MainCardModel(models.Model):
    image = models.ImageField(upload_to='site-images',
                              verbose_name='Изображение')
    name = models.CharField(max_length=50, blank=True, null=True, verbose_name='Название')
    description = models.TextField(max_length=150, verbose_name='Описание')
    post_link = models.URLField(max_length=200)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Карточка на главной странице'
        verbose_name_plural = 'Карточки на главной странице'
