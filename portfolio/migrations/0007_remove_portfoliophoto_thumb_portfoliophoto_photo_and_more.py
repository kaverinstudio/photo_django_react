# Generated by Django 4.0 on 2023-09-23 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0006_remove_portfoliophoto_photo_portfoliophoto_thumb_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='portfoliophoto',
            name='thumb',
        ),
        migrations.AddField(
            model_name='portfoliophoto',
            name='photo',
            field=models.ImageField(default=1, upload_to='portfolio', verbose_name='Фотография'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='portfoliophoto',
            name='src',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Миниатюра'),
        ),
    ]
