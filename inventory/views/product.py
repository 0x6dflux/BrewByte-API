from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.generics import ListAPIView

from inventory.models import Product
from inventory.serializers import ProductSerializer


class ProductViewSet(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_fields = ["category", "ingredients"]
    search_fields = ["name", "description", "category__name"]
    ordering_fields = ["price"]
    ordering = ["-price", "inventory_stock"]
