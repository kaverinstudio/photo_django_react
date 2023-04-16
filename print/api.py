from rest_framework import permissions, generics
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from datetime import datetime
from .models import Photo, Services, PapierType, PapierSize, OrderPhotos
from .serializers import FileViewSerializer, FileUploadSerializer, ServiceSerializer, PapierTypeSerializer, \
    PapierSizeSerializer, FileUpdateSerializer, OrderSerializer
from .sorting import move_files
from .models import Orders
from django.shortcuts import redirect
from emails.email import SendingEmail
from photo.settings import MEDIA_ROOT



class FileViewAPI(generics.GenericAPIView):
    permission_classes = [
        permissions.AllowAny
    ]

    def get(self, request):
        files = Photo.get_user_photos(request).order_by('-uploaded_at')
        files_serializer = FileViewSerializer(files, many=True)
        services = Services.objects.all()
        services_serializer = ServiceSerializer(services, many=True)
        papier_type = PapierType.objects.all()
        papier_type_serializer = PapierTypeSerializer(papier_type, many=True)
        papier_size = PapierSize.objects.all()
        papier_size_serializer = PapierSizeSerializer(papier_size, many=True)
        return Response({
            'files': files_serializer.data,
            'services': services_serializer.data,
            'papier_type': papier_type_serializer.data,
            'papier_size': papier_size_serializer.data
        })


class FileUploadAPI(generics.GenericAPIView):
    serializer_class = FileUploadSerializer
    permission_classes = [
        permissions.BasePermission
    ]
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        file = serializer.save()
        return Response({
            'file': FileViewSerializer(file, context=self.get_serializer_context()).data
        })


class FileUpdateAPI(generics.UpdateAPIView):
    serializer_class = FileUpdateSerializer
    permission_classes = [
        permissions.AllowAny
    ]
    lookup_field = 'pk'

    def get_queryset(self):
        queryset = Photo.get_user_photos(self.request).order_by('-uploaded_at')
        return queryset

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        files_serializer = FileViewSerializer(self.get_queryset(), many=True)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({
                'files': files_serializer.data
            })


class FileDeleteAPI(generics.GenericAPIView):
    serializer_class = FileViewSerializer
    permission_classes = [
        permissions.AllowAny
    ]
    lookup_field = 'pk'

    def get_queryset(self):
        queryset = Photo.get_user_photos(self.request).order_by('-uploaded_at')
        return queryset

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({
            'files': 'file was deleted'
        })


class ConfirmOrderAPI(generics.GenericAPIView):
    serializer_class = OrderSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        order = serializer.save()

        date = datetime.now().strftime('%d_%m_%Y_%H_%M')

        move_files(request, order.id, date)

        order_detail = request.data['order']

        for item in order_detail:
            OrderPhotos.objects.create(order_id=order.id, name=item['name'], count=item['count'], price=item['price'])

        files = Photo.get_user_photos(request).order_by('-uploaded_at')
        files_serializer = FileViewSerializer(files, many=True)

        email = SendingEmail()

        if request.user.is_authenticated:
            user_email = request.user.email
            email.sending_email(type_id=2, email=user_email, order=order, data=order_detail, order_type=2)
        else:
            if 'email' in request.data:
                user_email = request.data['email']
                email.sending_email(type_id=2, email=user_email, order=order, data=order_detail, order_type=2)
        email.sending_email(type_id=1, order=order, data=order_detail, order_type=2)

        return Response({
            'order': OrderSerializer(order, context=self.get_serializer_context()).data,
            'files': files_serializer.data
        })


def load_orders(request, id):
    name_link = Orders.objects.all().filter(id=id)

    for item in name_link:
        return redirect(item.link + '.zip')
