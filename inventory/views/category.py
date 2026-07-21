from rest_framework.viewsets import ModelViewSet

from inventory.models import Category
from inventory.serializers import CategorySerializer


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
