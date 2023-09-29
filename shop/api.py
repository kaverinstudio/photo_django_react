import json
from knox.auth import TokenAuthentication
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import permissions, generics
from rest_framework.response import Response
from .serializer import ProductModelSerializer, ProductPhotoSerializer, CartCreateSerializer, \
    CartViewSerializer, CartUpdateSerializer, ShopOrderSerializer, ProductReviewsSerializer, ProductReviewCreateSerializer
from .models import ProductModel, ProductPhoto, ProductCategoryModel, CartModel, ProductReviewsModel
from emails.email import SendingEmail


class AllProductViewAPI(generics.ListAPIView):
    permission_classes = [
        permissions.AllowAny
    ]

    def list(self, request, *args, **kwargs):
        if request.query_params.get('minPrice') and request.query_params.get('maxPrice') and request.query_params.get('sort'):
            kwargs = {}
            if request.query_params.get('manufactured'):
                manufactured = []
                for item in request.query_params.get('manufactured').split(','):
                    manufactured.append(str(item))
                kwargs['manufactured__in'] = manufactured
            if request.query_params.get('cat'):
                cat = []
                for item in request.query_params.get('cat').split(','):
                    cat.append(str(item))
                kwargs['category__category_name__in'] = cat
            products = ProductModel.objects.order_by(request.query_params.get('sort')) \
                .filter(
                price__range=(request.query_params.get('minPrice'), request.query_params.get('maxPrice'))).filter(
                **kwargs)
        else:
            products = ProductModel.objects.all().order_by('rating')
        products_serializer = ProductModelSerializer(products, many=True, context={'request': request})
        photos = ProductPhoto.objects.all()
        photos_serializer = ProductPhotoSerializer(photos, many=True, context={'request': request})
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
        kwargs = {}
        kwargs['category_id'] = cat_id.id
        if request.query_params.get('minPrice') and request.query_params.get('maxPrice') and request.query_params.get(
                'sort'):
            if request.query_params.get('manufactured'):
                manufactured = []
                for item in request.query_params.get('manufactured').split(','):
                    manufactured.append(str(item))
                kwargs['manufactured__in'] = manufactured
            if request.query_params.get('cat'):
                cat = []
                for item in request.query_params.get('cat').split(','):
                    cat.append(str(item))
                kwargs['category_name__in'] = cat
            products = ProductModel.objects.order_by(request.query_params.get('sort')) \
                .filter(
                price__range=(request.query_params.get('minPrice'), request.query_params.get('maxPrice'))).filter(
                **kwargs).filter()
        else:
            products = ProductModel.objects.filter(category_id=cat_id.id).order_by('rating')
        products_serializer = ProductModelSerializer(products, many=True, context={'request': request})
        photos = ProductPhoto.objects.filter(for_category=cat_id.id)
        photos_serializer = ProductPhotoSerializer(photos, many=True, context={'request': request})
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
        photos_serializer = ProductPhotoSerializer(photos, many=True, context={'request': request})
        reviews = ProductReviewsModel.objects.filter(product_id=product.id).filter(moderated=True)
        reviews_serializer = ProductReviewsSerializer(reviews, many=True, context={'request': request})
        return Response({
            'products': product_serializer.data,
            'photos': photos_serializer.data,
            'reviews': reviews_serializer.data
        })


class CartCreateViewAPI(generics.GenericAPIView):
    serializer_class = CartCreateSerializer
    permission_classes = [
        permissions.AllowAny
    ]
    authentication_classes = [
        TokenAuthentication
    ]
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        products_in_cart = CartModel.get_user_cart(request).order_by('id')
        products_serializer = CartViewSerializer(products_in_cart, many=True, context={'request': request})
        photos = []
        photos_list = ProductPhoto.objects.all()
        for item in products_in_cart:
            queryset = photos_list.filter(for_product_id=item.product.id)
            photos.append(queryset[0])
        photos_serializer = ProductPhotoSerializer(photos, many=True, context={'request': request})
        return Response({
            'product': products_serializer.data,
            'photos': photos_serializer.data
        })


class CartViewAPI(generics.GenericAPIView):
    permission_classes = [
        permissions.AllowAny
    ]
    authentication_classes = [
        TokenAuthentication
    ]

    def get(self, request):
        product = CartModel.get_user_cart(request).order_by('id')
        serializer = CartViewSerializer(product, many=True, context={'request': request})
        photos = []
        photos_list = ProductPhoto.objects.all()
        for item in product:
            queryset = photos_list.filter(for_product_id=item.product.id)
            photos.append(queryset[0])
        photos_serializer = ProductPhotoSerializer(photos, many=True, context={'request': request})
        return Response({
            'product': serializer.data,
            'photos': photos_serializer.data
        })


class CartUpdateAPI(generics.UpdateAPIView):
    serializer_class = CartUpdateSerializer
    permission_classes = [
        permissions.AllowAny
    ]
    authentication_classes = [
        TokenAuthentication
    ]
    lookup_field = 'pk'

    def get_queryset(self):
        queryset = CartModel.get_user_cart(self.request).order_by('id')
        return queryset

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True, context={'request': request})
        product_serializer = CartViewSerializer(self.get_queryset(), many=True, context={'request': request})
        product = self.get_queryset()
        photos = []
        photos_list = ProductPhoto.objects.all()
        for item in product:
            queryset = photos_list.filter(for_product_id=item.product.id)
            photos.append(queryset[0])
        photos_serializer = ProductPhotoSerializer(photos, many=True, context={'request': request})

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({
                'product': product_serializer.data,
                'photos': photos_serializer.data
            })


class CartDeleteAPI(generics.GenericAPIView):
    serializer_class = CartViewSerializer
    permission_classes = [
        permissions.AllowAny
    ]
    lookup_field = 'pk'

    def get_queryset(self):
        queryset = CartModel.get_user_cart(self.request).order_by('id')
        return queryset

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        product_serializer = CartViewSerializer(self.get_queryset(), many=True, context={'request': request})
        product = self.get_queryset()
        photos = []
        photos_list = ProductPhoto.objects.all()
        for item in product:
            queryset = photos_list.filter(for_product_id=item.product.id)
            photos.append(queryset[0])
        photos_serializer = ProductPhotoSerializer(photos, many=True, context={'request': request})
        return Response({
            'product': product_serializer.data,
            'photos': photos_serializer.data
        })

class CartAllDeleteAPI(generics.GenericAPIView):
    serializer_class = CartViewSerializer
    permission_classes = [
        permissions.AllowAny
    ]
    authentication_classes = [
        TokenAuthentication
    ]

    def get_queryset(self):
        queryset = CartModel.get_user_cart(self.request).order_by('id')
        return queryset

    def delete(self, request, *args, **kwargs):
        for item in self.get_queryset():
            item.delete()
        product_serializer = CartViewSerializer(self.get_queryset(), many=True, context={'request': request})

        return Response({
            'product': product_serializer.data,
            'photos': []
        })


class ConfirmShopOrderAPI(generics.GenericAPIView):
    serializer_class = ShopOrderSerializer
    authentication_classes = [
        TokenAuthentication
    ]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        order = serializer.save()

        user_cart = CartModel.get_user_cart(request)
        user_cart.delete()

        order_detail = request.data['order']

        email = SendingEmail()

        if request.user.is_authenticated:
            user_email = request.user.email
            email.sending_email(type_id=2, email=user_email, order=order, data=order_detail, order_type=1)
        else:
            if 'email' in request.data:
                user_email = request.data['email']
                email.sending_email(type_id=2, email=user_email, order=order, data=order_detail, order_type=1)
        email.sending_email(type_id=1, order=order, data=order_detail, order_type=1)

        return Response({
            'order': ShopOrderSerializer(order, context=self.get_serializer_context()).data
        })


class ProductReviewCreateAPI(generics.GenericAPIView):
    serializer_class = ProductReviewCreateSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response('Ваш отзыв отправлен на модерацию')


