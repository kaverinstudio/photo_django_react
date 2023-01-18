from rest_framework import serializers
from .models import MainCardModel


class MainCardSerialiser(serializers.ModelSerializer):
    class Meta:
        model = MainCardModel
        fields = '__all__'
