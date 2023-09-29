from rest_framework import routers
from django.urls import path, include
from .api import UserAPI, RegisterAPI, LoginAPI, UpdateAPI, UploadAvatarAPI
from knox import views as knox_views

router = routers.DefaultRouter()

urlpatterns = [
    path('api/auth', include('knox.urls')),
    path('api/auth/register', RegisterAPI.as_view()),
    path('api/auth/login', LoginAPI.as_view()),
    path('api/auth/user', UserAPI.as_view()),
    path('api/auth/update/<int:pk>', UpdateAPI.as_view()),
    path('api/auth/avatar', UploadAvatarAPI.as_view()),
    path('api/auth/logout', knox_views.LogoutView.as_view(), name='knox_logout')
]

urlpatterns += router.urls
