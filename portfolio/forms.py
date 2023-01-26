from django import forms
from .models import Portfolio


class PortfolioAdminForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = ['category']


