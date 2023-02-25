from rest_framework import routers
from django.urls import path
from .api import PortfolioAllViewAPI, PortfolioCategoryViewAPI

router = routers.DefaultRouter()

urlpatterns = [
    path('api/portfolio/', PortfolioAllViewAPI.as_view()),
    path('api/portfolio/<int:pk>/', PortfolioCategoryViewAPI.as_view())
]

urlpatterns += router.urls