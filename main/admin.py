from django.contrib import admin
from django.utils.safestring import mark_safe
from modeltranslation.admin import TranslationAdmin
from .models import MainCardModel, FlatPageModel, ContactPageModel, MainSliderModel

admin.site.site_header = 'Админпанель сайта Фото № 1'


class MainCardModelPreview(TranslationAdmin):
    fields = ['name', 'description', 'image', 'preview', 'post_link', 'slug']
    readonly_fields = ["preview"]
    prepopulated_fields = {'slug': ['name']}

    def preview(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" style="max-height: 200px;>')


admin.site.register(MainCardModel, MainCardModelPreview)

class FlatPageModelPreview(admin.ModelAdmin):
    fields = ['title', 'name', 'description', 'image', 'preview', 'slug']
    readonly_fields = ['preview']
    prepopulated_fields = {'slug': ['name']}
    
    def preview(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" style="max-height: 200px;>')
    
admin.site.register(FlatPageModel, FlatPageModelPreview)

admin.site.register(ContactPageModel)

class MainSliderModelPreview(admin.ModelAdmin):
    fields = ['title', 'post_link', 'image', 'preview']
    readonly_fields = ['preview']
    
    def preview(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" style="max-height: 200px;>')

admin.site.register(MainSliderModel, MainSliderModelPreview)
