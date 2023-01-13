from rest_framework import viewsets
from rest_framework.response import Response

from .models import Brand, Category, Product
from .serializers import BrandSerializer, CategorySerializer, ProductSerializer


class CategoryViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving categories.
    """

    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def list(self, request):
        serializer = CategorySerializer(self.queryset, many=True)
        return Response(serializer.data)


class BrandViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving brands.
    """

    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

    def list(self, request):
        serializer = BrandSerializer(self.queryset, many=True)
        return Response(serializer.data)


class ProductViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving products.
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def list(self, request):
        serializer = ProductSerializer(self.queryset, many=True)
        return Response(serializer.data)
