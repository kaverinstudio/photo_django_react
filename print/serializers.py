from rest_framework import serializers
from .models import Photo, Services, PapierSize, PapierType, Orders, OrderPhotos


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = '__all__'


class PapierSizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PapierSize
        fields = '__all__'


class PapierTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PapierType
        fields = '__all__'


class FileViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = '__all__'


class FileUploadSerializer(serializers.ModelSerializer):
    file = serializers.ListField(child=serializers.ImageField())

    class Meta:
        model = Photo
        fields = '__all__'

    def create(self, validated_data):
        if self.context['request'].user.is_anonymous:
            user = None
        else:
            user = self.context['request'].user

        files = validated_data.pop('file')
        for img in files:
            photo = Photo.objects.create(user=user, file=img, **validated_data)
        return photo


class FileUpdateSerializer(serializers.Serializer):
    format = serializers.CharField()
    papier = serializers.CharField()
    count = serializers.IntegerField()

    def update(self, instance, validated_data):
        instance.format = validated_data.get('format', instance.format)
        instance.papier = validated_data.get('papier', instance.papier)
        instance.count = validated_data.get('count', instance.count)

        instance.save()
        return instance

class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Orders
        fields = ['first_name', 'last_name', 'phone', 'email', 'delivery', 'comments', 'address']

    def create(self, validated_data):
        if self.context['request'].user.is_anonymous:
            user = None
        else:
            user = self.context['request'].user

        order = Orders.objects.create(user=user, **validated_data)
        return order

# class PhotoOrderSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = OrderPhotos
#         fields = ['']

