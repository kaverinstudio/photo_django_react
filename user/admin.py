from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import UserModel

class UserAdminModel(admin.ModelAdmin):
    fields = ['username', 'email', 'first_name', 'last_name', 'phone', 'city', 'avatar', 'preview']
    readonly_fields = ["preview"]

    def preview(self, obj):
        return mark_safe(f'<img src="{obj.avatar.url}" style="max-height: 200px;>')

admin.site.register(UserModel, UserAdminModel)
