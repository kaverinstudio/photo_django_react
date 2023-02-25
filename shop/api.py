import json
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import permissions, generics
from rest_framework.response import Response
from .serializer import ProductModelSerializer, ProductPhotoSerializer, CartCreateSerializer, CartViewSerializer
from .models import ProductModel, ProductPhoto, ProductCategoryModel, CartModel


class AllProductViewAPI(generics.ListAPIView):
    permission_classes = [
        permissions.AllowAny
    ]

    def list(self, request, *args, **kwargs):
        products = ProductModel.objects.all()
        products_serializer = ProductModelSerializer(products, many=True)
        photos = ProductPhoto.objects.all()
        photos_serializer = ProductPhotoSerializer(photos, many=True)
        return Response({
            'products': products_serializer.data,
            'photos': photos_serializer.data
        })


class ProductCategoryViewAPI(generics.ListAPIView):
    permission_classes = [
        permissions.AllowAny
    ]

    def list(self, request, *args, **kwargs):
        cat_id = ProductCategoryModel.objects.get(category_slug=self.kwargs['category_slug'])
        products = ProductModel.objects.filter(category_id=cat_id.id)
        products_serializer = ProductModelSerializer(products, many=True)
        photos = ProductPhoto.objects.filter(for_category=cat_id.id)
        photos_serializer = ProductPhotoSerializer(photos, many=True)
        return Response({
            'products': products_serializer.data,
            'photos': photos_serializer.data
        })


class OneProductViewAPI(generics.RetrieveAPIView):
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ProductModelSerializer

    def get_object(self):
        product = ProductModel.objects.get(product_slug=self.kwargs['product_slug'])
        return product

    def get(self, request, *args, **kwargs):
        product = self.get_object()
        product_serializer = ProductModelSerializer(product)
        photos = ProductPhoto.objects.filter(for_product_id=product.id)
        photos_serializer = ProductPhotoSerializer(photos, many=True)
        return Response({
            'products': product_serializer.data,
            'photos': photos_serializer.data
        })


class CartCreateViewAPI(generics.GenericAPIView):
    serializer_class = CartCreateSerializer
    permission_classes = [
        permissions.AllowAny
    ]

    # parser_classes = [MultiPartParser, FormParser]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        products_in_cart = CartModel.get_user_cart(request)
        products_serializer = CartViewSerializer(products_in_cart, many=True)
        return Response({
            'product': products_serializer.data
        })


class CartViewAPI(generics.GenericAPIView):
    permission_classes = [
        permissions.AllowAny
    ]

    def get(self, request):
        product = CartModel.get_user_cart(request)
        serializer = CartViewSerializer(product, many=True)
        return Response({
            'product': serializer.data
        })
