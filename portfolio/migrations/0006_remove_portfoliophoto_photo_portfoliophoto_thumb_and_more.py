# Generated by Django 4.0 on 2023-09-23 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_portfoliophoto_photo_alter_portfoliophoto_src'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='portfoliophoto',
            name='photo',
        ),
        migrations.AddField(
            model_name='portfoliophoto',
            name='thumb',
            field=models.ImageField(default=1, upload_to='', verbose_name='Миниатюра'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='portfoliophoto',
            name='src',
            field=models.ImageField(upload_to='portfolio', verbose_name='Фотография'),
        ),
    ]
