from rest_framework import routers
from django.urls import path
from .api import MainCardViewSet, FlatPageViewSet, ContactPageViewAPI, MainPageSliderViewSet


router = routers.DefaultRouter()

urlpatterns = [
  path("api/main/", MainCardViewSet.as_view()),
  path("api/main/<slug:slug>/", FlatPageViewSet.as_view()),
  path("api/contact/", ContactPageViewAPI.as_view()),
  path("api/slider/", MainPageSliderViewSet.as_view())
]


urlpatterns += router.urls