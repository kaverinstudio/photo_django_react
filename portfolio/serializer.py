from rest_framework import serializers
from .models import PortfolioPhoto


class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = PortfolioPhoto
        fields = ['src', 'width', 'height']

