# Generated by Django 4.0 on 2023-04-23 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('print', '0015_remove_orders_session_key_orders_file_field'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='papier',
            field=models.CharField(choices=[('Глянцевая', 'Глянцевая'), ('Матовая', 'Матовая')], default='Глянцевая', max_length=50),
        ),
    ]
