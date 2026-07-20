from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from config.mixin import DetailMixin
from inventory.models import Product
from inventory.serializers import ProductSerializer


class ProductListCreateAPIView(APIView):
    def get(self, request: Request) -> Response:
        s = ProductSerializer(Product.objects.all(), many=True)

        return Response(s.data)

    def post(self, request: Request) -> Response:
        print(request.data)
        s = ProductSerializer(data=request.data)

        if s.is_valid():
            s.save()

            return Response(s.data, HTTP_201_CREATED)

        return Response(s.errors, HTTP_400_BAD_REQUEST)


class ProductRetrieveUpdateDestroyAPIView(DetailMixin, APIView):
    model_name = Product
    serializer_name = ProductSerializer

    def get(self, request: Request, pk: int) -> Response:
        s = ProductSerializer(self._get_object_or_404(pk))

        return Response(s.data)

    def put(self, request: Request, pk: int) -> Response:
        return self._update_product(pk)

    def patch(self, request: Request, pk: int) -> Response:
        return self._update_product(pk, partial=True)

    def delete(self, request: Request, pk: int) -> Response:
        self._get_object_or_404(pk).delete()

        return Response()
