from django.db import models
from django.contrib.auth.models import AbstractUser


class UserModel(AbstractUser):
    city = models.TextField(max_length=100, blank=True, null=True, verbose_name='Адрес доставки')
    phone = models.CharField(max_length=13, blank=True, null=True, verbose_name='Телефон')
    email = models.EmailField(max_length=100, blank=False, null=True, unique=True, verbose_name='Email')
    first_name = models.CharField(max_length=64, blank=True, null=True, verbose_name='Имя')
    last_name = models.CharField(max_length=64, blank=True, null=True, verbose_name='Фамилия')
    avatar = models.ImageField(upload_to='user-images', verbose_name='Аватарка', blank=True, null=True)

    def __str__(self):
        short_name = self.get_short_name()

        if short_name:
            return f'{short_name} ({self.email})'

        return f'{self.username} ({self.email})'
