from rest_framework import serializers
from .models import PortfolioPhoto, Portfolio


class PortfolioPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PortfolioPhoto
        fields = ['src', 'width', 'height', 'photo']


class PortfolioCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio
        fields = '__all__'

