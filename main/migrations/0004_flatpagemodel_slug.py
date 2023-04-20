# Generated by Django 4.0 on 2023-04-16 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_maincardmodel_slug_alter_flatpagemodel_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='flatpagemodel',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, null=True, verbose_name='URL'),
        ),
    ]
