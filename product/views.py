from rest_framework import filters, viewsets
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


# class ProductViewSet(viewsets.ViewSet):
#     """
#     A simple ViewSet for listing or retrieving products.
#     """

#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer

#     def list(self, request):
#         serializer = ProductSerializer(self.queryset, many=True)
#         return Response(serializer.data)

#     @action(detail=False, methods=["get"], url_path="(?P<category>[^/.]+)")
#     def list_product_by_category(self, request, category=None):
#         serializer = ProductSerializer(
#             self.queryset.filter(category__name=category), many=True
#         )
#         return Response(serializer.data)


class ProductViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for do CRUD operations on products.
    This will be generate all the endpoints for the model.
    """

    queryset = Product.objects.select_related("brand", "category")
    serializer_class = ProductSerializer
    lookup_field = "slug"
    filter_backends = [filters.SearchFilter]
    search_fields = ["name", "category__name", "brand__name"]
