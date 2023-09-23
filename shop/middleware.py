from django.db.models import F
from django.shortcuts import get_object_or_404

from shop.models import ProductModel


class ProductViewMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if request.resolver_match and 'product_slug' in request.resolver_match.kwargs:
            print(request.resolver_match.kwargs)
            product = get_object_or_404(ProductModel, product_slug=request.resolver_match.kwargs['product_slug'])
            ProductModel.objects.filter(pk=product.pk).update(view_count=F('view_count') + 1)

        return response
