from rest_framework import permissions, generics
from rest_framework.response import Response
from .serializer import PortfolioPhotoSerializer, PortfolioCategorySerializer
from .models import PortfolioPhoto, Portfolio


class PortfolioAllViewAPI(generics.ListAPIView):
    permission_classes = [
        permissions.AllowAny
    ]

    def list(self, request, *args, **kwargs):
        files = PortfolioPhoto.objects.all().order_by('?')
        serializer = PortfolioPhotoSerializer(files, many=True, context={'request': request})
        category = Portfolio.objects.all()
        category_serializer = PortfolioCategorySerializer(category, many=True)
        return Response({
            'files': serializer.data,
            'category': category_serializer.data
        })


class PortfolioCategoryViewAPI(generics.ListAPIView):
    serializer_class = PortfolioPhotoSerializer
    permission_classes = [
        permissions.AllowAny
    ]

    def get_queryset(self):
        queryset = PortfolioPhoto.objects.filter(active=self.kwargs['pk']).order_by('?')
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = PortfolioPhotoSerializer(queryset, many=True, context={'request': request})
        category = Portfolio.objects.all()
        category_serializer = PortfolioCategorySerializer(category, many=True)
        return Response({
            'files': serializer.data,
            'category': category_serializer.data
        })
