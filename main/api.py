from rest_framework import viewsets, permissions, generics
from .models import MainCardModel, FlatPageModel, ContactPageModel, MainSliderModel
from .serializers import MainCardSerialiser, FlatPageSerializer, ContactPageSerializer, MainPageSliderSerializer


class MainCardViewSet(generics.ListAPIView):
    queryset = MainCardModel.objects.all()

    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = MainCardSerialiser


class FlatPageViewSet(generics.RetrieveAPIView):
    queryset = FlatPageModel.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    
    lookup_field = 'slug'
    
    serializer_class = FlatPageSerializer
    

class ContactPageViewAPI(generics.ListAPIView):
    queryset = ContactPageModel.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
     
    serializer_class = ContactPageSerializer
    
    
class MainPageSliderViewSet(generics.ListAPIView):
    queryset = MainSliderModel.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = MainPageSliderSerializer
    
    
