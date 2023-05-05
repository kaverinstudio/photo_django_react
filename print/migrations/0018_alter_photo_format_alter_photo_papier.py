# Generated by Django 4.0 on 2023-04-23 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('print', '0017_alter_photo_format_alter_photo_papier'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='format',
            field=models.CharField(choices=[('10x15', '10x15')], default='10x15', max_length=50),
        ),
        migrations.AlterField(
            model_name='photo',
            name='papier',
            field=models.CharField(choices=[('Глянцевая', 'Глянцевая')], default='Глянцевая', max_length=50),
        ),
    ]
