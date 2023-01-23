from django.contrib import admin
from django.template.loader import get_template
from django.utils.translation import gettext_lazy as _

from .models import Portfolio, PortfolioPhoto
from .forms import PortfolioAdminForm


class PortfolioAdminView(admin.TabularInline):
    model = PortfolioPhoto

    readonly_fields = ['photo_thumbnail', 'width', 'height']

    def photo_thumbnail(self, instance):
        tpl = get_template('show_thumbnail.html')
        return tpl.render({'photo': instance.src})

    photo_thumbnail.short_description = _('Фотографии')


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    form = PortfolioAdminForm
    inlines = [PortfolioAdminView]

