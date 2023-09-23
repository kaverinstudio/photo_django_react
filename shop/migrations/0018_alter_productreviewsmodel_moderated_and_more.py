# Generated by Django 4.0 on 2023-05-06 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0017_productreviewsmodel_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productreviewsmodel',
            name='moderated',
            field=models.BooleanField(null=True, verbose_name='Отзыв прошел модерацию'),
        ),
        migrations.AlterField(
            model_name='productreviewsmodel',
            name='user_name',
            field=models.CharField(default=1, max_length=100, verbose_name='Имя пользователя'),
            preserve_default=False,
        ),
    ]