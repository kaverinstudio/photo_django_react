from django.contrib import admin
from django.template.loader import get_template
from django.utils.translation import gettext as _
from django.utils.safestring import mark_safe
from .models import ProductModel, ProductCategoryModel, ProductPhoto, ShopOrderModel


class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'category_name', 'category_slug']
    list_display_links = ['id', 'category_name']
    search_fields = ['category_name']
    prepopulated_fields = {'category_slug': ['category_name']}


admin.site.register(ProductCategoryModel, ProductCategoryAdmin)


class PhotoInline(admin.TabularInline):
    model = ProductPhoto
    readonly_fields = ['thumbnail']
    exclude = ['for_category']

    def thumbnail(self, instance):
        tpl = get_template('show_thumbnail.html')
        return tpl.render({'photo': instance.photo})
    thumbnail.short_description = _('Фотографии')


@admin.register(ProductModel)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'product_name', 'price', 'available']
    list_editable = ['price', 'available']
    list_display_links = ['id', 'product_name']
    list_filter = ['product_name', 'available']
    readonly_fields = ['view_count', 'rating', 'product_slug']
    # prepopulated_fields = {'product_slug': ['product_name']}
    inlines = [PhotoInline]

    def image_show(self, obj):
        img = ProductPhoto.objects.filter(for_product_id=obj.id).first()
        return mark_safe(f'<img src="{img.image.url}" style="max-height: 60px;"')


@admin.register(ShopOrderModel)
class ShopOrderView(admin.ModelAdmin):
    list_display = ['first_name', 'phone', 'delivery', 'address', 'comments', 'create_at']
    readonly_fields = ['first_name', 'last_name', 'email', 'phone', 'delivery', 'address', 'comments', 'create_at', 'products', 'user']
    search_fields = ['first_name', 'user']

    list_filter = ['first_name', 'phone', 'create_at']

