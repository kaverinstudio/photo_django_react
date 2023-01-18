from django.contrib.auth.decorators import user_passes_test
from rest_framework import routers
from django.urls import path
from .api import FileViewAPI, FileUploadAPI, FileUpdateAPI, FileDeleteAPI, ConfirmOrderAPI, load_orders

router = routers.DefaultRouter()

urlpatterns = [
    path('api/print/', FileViewAPI.as_view()),
    path('api/print/upload', FileUploadAPI.as_view()),
    path('api/print/update/<int:pk>', FileUpdateAPI.as_view()),
    path('api/print/delete/<int:pk>', FileDeleteAPI.as_view()),
    path('api/print/confirm', ConfirmOrderAPI.as_view()),
    path('orders/<int:id>/', user_passes_test(lambda u: u.is_superuser)(load_orders), name='orders')
]

urlpatterns += router.urls
