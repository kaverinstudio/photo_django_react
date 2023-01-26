from rest_framework import routers
from django.urls import path
from .api import ProductCategoryViewAPI, AllProductViewAPI, OneProductViewAPI


router = routers.DefaultRouter()

urlpatterns = [
    path('api/products/', AllProductViewAPI.as_view(), name='products'),
    path('api/products/<slug:category_slug>/', ProductCategoryViewAPI.as_view(), name='category'),
    path('api/products/<slug:category_slug>/<slug:product_slug>/', OneProductViewAPI.as_view(), name='product')
]

urlpatterns += router.urls