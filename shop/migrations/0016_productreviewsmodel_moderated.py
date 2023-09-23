# Generated by Django 4.0 on 2023-05-05 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0015_productreviewsmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='productreviewsmodel',
            name='moderated',
            field=models.BooleanField(default=1, verbose_name='Отзыв прошел модерацию'),
            preserve_default=False,
        ),
    ]