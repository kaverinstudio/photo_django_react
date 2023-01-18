from rest_framework import viewsets, permissions
from .models import MainCardModel
from .serializers import MainCardSerialiser


class MainCardViewSet(viewsets.ModelViewSet):
    queryset = MainCardModel.objects.all()

    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = MainCardSerialiser
