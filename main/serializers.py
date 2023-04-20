from rest_framework import serializers
from .models import MainCardModel, FlatPageModel, ContactPageModel, MainSliderModel


class MainCardSerialiser(serializers.ModelSerializer):
    class Meta:
        model = MainCardModel
        fields = '__all__'
        
class FlatPageSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = FlatPageModel
        fields = '__all__'
        
        
class ContactPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactPageModel
        fields = '__all__'
        
        
class MainPageSliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainSliderModel
        fields = '__all__'
