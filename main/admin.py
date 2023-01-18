from django.contrib import admin
from django.utils.safestring import mark_safe
from modeltranslation.admin import TranslationAdmin
from .models import MainCardModel

admin.site.site_header = 'Админпанель сайта Фото № 1'


class MainCardModelPreview(TranslationAdmin):
    fields = ['name', 'description', 'image', 'preview', 'post_link']
    readonly_fields = ["preview"]

    def preview(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" style="max-height: 200px;>')


admin.site.register(MainCardModel, MainCardModelPreview)
