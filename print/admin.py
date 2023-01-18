from django.contrib import admin
from django.template.loader import get_template
from django.utils.html import format_html


from .models import Services, PapierType, PapierSize, Photo, Orders, OrderPhotos

admin.site.register(Services)
admin.site.register(PapierType)
admin.site.register(PapierSize)
admin.site.register(Photo)


class OrderView(admin.ModelAdmin):
    list_display = ['first_name', 'phone', 'delivery', 'address', 'comments', 'create_at', 'show_firm_url']

    readonly_fields = ['first_name', 'last_name', 'email', 'phone', 'delivery', 'address', 'comments', 'create_at', 'link', 'user', 'order_table']

    def show_firm_url(self, obj):
        return format_html('<a href="{url}">Скачать заказ</a>', url=f'/orders/{obj.id}')

    show_firm_url.short_description = 'Ссылка на заказ'

    def order_table(self, obj):
        table_context = OrderPhotos.objects.all().filter(order_id=obj.id)
        total = 0
        for item in table_context:
            price = int(item.count) * int(item.price)
            total += price
        table = get_template('order-table.html')
        return table.render({'table_context': table_context, 'total': total})
    
    order_table.short_description = 'Таблица заказа'


admin.site.register(Orders, OrderView)
