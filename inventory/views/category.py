from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from config.mixin import GeneralMixin
from inventory.models import Category
from inventory.serializers import CategorySerializer


class CategoryViewSet(GeneralMixin, ViewSet):
    query_set = Category.objects.all()
    serializer_class = CategorySerializer

    def list(self, request: Request) -> Response:
        return self._list()

    def create(self, request: Request) -> Response:
        return self._create()

    def retrieve(self, request: Request, pk: int) -> Response:
        return self._retrieve(pk)

    def update(self, request: Request, pk: int) -> Response:
        return self._update(pk)

    def partial_update(self, request: Request, pk: int) -> Response:
        return self._update(pk, partial=True)

    def destroy(self, request: Request, pk: int) -> Response:
        return self._destroy(pk)
