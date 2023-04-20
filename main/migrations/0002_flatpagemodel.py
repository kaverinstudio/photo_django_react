# Generated by Django 4.0 on 2023-04-16 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FlatPageModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True, verbose_name='Описание страницы')),
                ('image', models.ImageField(upload_to='site-images', verbose_name='Изображение')),
                ('name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Название')),
                ('description', models.TextField(max_length=150, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Простая страница',
                'verbose_name_plural': 'Простые страницы',
            },
        ),
    ]