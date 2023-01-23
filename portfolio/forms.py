from django import forms
from django.core.validators import validate_image_file_extension
from .models import Portfolio, PortfolioPhoto


class PortfolioAdminForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = ['category']

    # def clean(self):
    #     count = PortfolioPhoto.objects.filter(active_id=self.instance.id)
    #     photos = self.files.getlist(f'images-{len(count)}-src')
    #     for upload in photos:
    #         validate_image_file_extension(upload)

