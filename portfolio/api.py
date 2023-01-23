from rest_framework import permissions, generics
from rest_framework.response import Response
from .serializer import PortfolioSerializer
from .models import PortfolioPhoto


class PortfolioAllViewAPI(generics.ListAPIView):
    queryset = PortfolioPhoto.objects.all().order_by('?')
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = PortfolioSerializer

    def list_photos(self):
        queryset = self.get_queryset()
        serializer = PortfolioSerializer(queryset, many=True)
        return Response(serializer.data)


class PortfolioCategoryViewAPI(generics.ListAPIView):
    serializer_class = PortfolioSerializer
    permission_classes = [
        permissions.AllowAny
    ]

    def get_queryset(self):
        queryset = PortfolioPhoto.objects.filter(active=self.kwargs['pk']).order_by('?')
        return queryset

    def retrieve(self):
        queryset = self.get_queryset()
        serializer = PortfolioSerializer(queryset, many=True)
        return Response(serializer.data)
