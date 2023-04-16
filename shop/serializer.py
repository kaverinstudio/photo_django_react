from rest_framework import serializers
from .models import ProductModel, ProductPhoto, ProductCategoryModel, CartModel, ShopOrderModel


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategoryModel
        fields = '__all__'


class ProductModelSerializer(serializers.ModelSerializer):
    category = ProductCategorySerializer(
        read_only=True
    )

    class Meta:
        model = ProductModel
        fields = '__all__'


class ProductPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductPhoto
        fields = '__all__'


class CartCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartModel
        fields = '__all__'

    def create(self, validated_data):
        if self.context['request'].user.is_anonymous:
            user = None
        else:
            user = self.context['request'].user
        product_list = CartModel.get_user_cart(self.context['request']).filter(product_id=validated_data['product'].id)
        if product_list:
            for item in product_list:
                item.product_count += int(self.context['request'].data['count'])
                item.save()
                return item
        item = CartModel.objects.create(user=user, product_id=validated_data['product'].id, **validated_data)
        return item


class CartViewSerializer(serializers.ModelSerializer):
    product = ProductModelSerializer(
        read_only=True
    )

    class Meta:
        model = CartModel
        fields = '__all__'


class CartUpdateSerializer(serializers.Serializer):
    product_count = serializers.IntegerField()

    def update(self, instance, validated_data):
        instance.product_count = self.context['request'].data['count']

        instance.save()
        return instance


class ShopOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShopOrderModel
        fields = ['first_name', 'last_name', 'phone', 'email', 'delivery', 'comments', 'address', 'products']

    def create(self, validated_data):
        products = self.context['request'].data['order']
        if self.context['request'].user.is_anonymous:
            user = None
        else:
            user = self.context['request'].user
        order = ShopOrderModel.objects.create(user=user, products=products, **validated_data)
        return order
