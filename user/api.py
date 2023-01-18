from knox.models import AuthToken
from rest_framework import permissions, generics
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from .models import UserModel

from .serializers import UserSerializer, RegisterSerializer, LoginSerializer, UpdateSerializer, UploadAvatarSerializer


# Get User API
class UserAPI(generics.RetrieveAPIView):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


# Register API

class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            'user': UserSerializer(user, context=self.get_serializer_context()).data,
            'token': AuthToken.objects.create(user)[1],
            'message': 'Вы успешно зарегистрировались на сайте'
        })


# Login API

class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        return Response({
            'user': UserSerializer(user, context=self.get_serializer_context()).data,
            'token': AuthToken.objects.create(user)[1]
        })


class UpdateAPI(generics.UpdateAPIView):
    queryset = UserModel.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]

    serializer_class = UpdateSerializer
    lookup_field = 'pk'

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({
                'user': UserSerializer(instance, context=self.get_serializer_context()).data,
                'token': AuthToken.objects.create(instance)[1],
                'message': 'Профиль пользователя изменен'
            })


class UploadAvatarAPI(generics.GenericAPIView):
    queryset = UserModel.objects.all()
    parser_classes = [MultiPartParser, FormParser]
    permission_classes = [
        permissions.IsAuthenticated
    ]

    def post(self, request, format=None):
        serializer = UploadAvatarSerializer(data=request.data, instance=request.user, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save(avatar=request.data.get('avatar'))
            return Response({
                'user': UserSerializer(request.user, context=self.get_serializer_context()).data,
                'token': AuthToken.objects.create(request.user)[1],
                'message': 'Аватарка была загружена'
            })

