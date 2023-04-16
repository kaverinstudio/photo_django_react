from django.db import models

class MainCardModel(models.Model):
    image = models.ImageField(upload_to='site-images',
                              verbose_name='Изображение')
    name = models.CharField(max_length=50, blank=True, null=True, verbose_name='Название')
    description = models.TextField(max_length=150, verbose_name='Описание')
    post_link = models.URLField(max_length=200)
    slug = models.SlugField(max_length=255, blank=True, null=True, verbose_name='URL')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Карточка на главной странице'
        verbose_name_plural = 'Карточки на главной странице'
        

class FlatPageModel(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True, verbose_name='Описание страницы')
    image = models.ImageField(upload_to='site-images',
                              verbose_name='Изображение', blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True, verbose_name='Название')
    description = models.TextField(max_length=None, verbose_name='Описание', blank=True, null=True)
    slug = models.SlugField(max_length=255, blank=True, null=True, verbose_name='URL')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Простая страница'
        verbose_name_plural = 'Простые страницы'
        

class ContactPageModel(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True, verbose_name='Название страницы')
    slug = models.SlugField(max_length=255, blank=True, null=True, verbose_name='URL')
    address = models.TextField(max_length=250, blank=True, null=True, verbose_name='Адрес')
    phone = models.CharField(max_length=15, blank=True, null=True, verbose_name='Телефон')
    work_time = models.CharField(max_length=150, blank=True, null=True, verbose_name='Время работы')
    
    
    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Страница контакты'
        verbose_name_plural = 'Страница контакты'
        