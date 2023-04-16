from rest_framework import routers
from django.urls import path
from .api import ProductCategoryViewAPI, AllProductViewAPI, OneProductViewAPI, CartCreateViewAPI, CartViewAPI, CartUpdateAPI, CartDeleteAPI, CartAllDeleteAPI, ConfirmShopOrderAPI


router = routers.DefaultRouter()

urlpatterns = [
    path('api/products/', AllProductViewAPI.as_view(), name='products'),
    path('api/products/<slug:category_slug>/', ProductCategoryViewAPI.as_view(), name='category'),
    path('api/products/<slug:category_slug>/<slug:product_slug>/', OneProductViewAPI.as_view(), name='product'),
    path('api/cart/', CartViewAPI.as_view(), name='cart'),
    path('api/cart/create/', CartCreateViewAPI.as_view(), name='addToCart'),
    path('api/cart/update/<int:pk>', CartUpdateAPI.as_view()),
    path('api/cart/delete/<int:pk>', CartDeleteAPI.as_view()),
    path('api/cart/delete/', CartAllDeleteAPI.as_view()),
    path('api/cart/confirm', ConfirmShopOrderAPI.as_view())
]

urlpatterns += router.urls