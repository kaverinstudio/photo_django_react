# Generated by Django 4.0 on 2023-04-17 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_mainslidermodel_post_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainslidermodel',
            name='post_link',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Ссылка'),
        ),
    ]
