# Generated by Django 4.0 on 2023-09-23 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_alter_portfoliophoto_height_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfoliophoto',
            name='photo',
            field=models.ImageField(default=1, upload_to='portfolio', verbose_name='Фотография'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='portfoliophoto',
            name='src',
            field=models.ImageField(upload_to='portfolio/thumb', verbose_name='Миниатюра'),
        ),
    ]
