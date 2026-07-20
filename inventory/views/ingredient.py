from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from inventory.models import Ingredient
from inventory.serializers import IngredientSerializer


class IngredientListCreateAPIView(APIView):
    def get(self, request: Request) -> Response:
        s = IngredientSerializer(Ingredient.objects.all(), many=True)

        return Response(s.data)

    def post(self, request: Request) -> Response:
        s = IngredientSerializer(data=request.data)

        if s.is_valid():
            s.save()

            return Response(s.data, HTTP_201_CREATED)

        return Response(s.errors, HTTP_400_BAD_REQUEST)


class IngredientRetrieveUpdateDestroyAPIView(APIView):
    def get(self, request: Request, pk: int) -> Response:
        s = IngredientSerializer(Ingredient.objects.get(id=pk))

        return Response(s.data)

    def put(self, request: Request, pk: int) -> Response:
        s = IngredientSerializer(Ingredient.objects.get(id=pk), request.data)

        if s.is_valid():
            s.save()

            return Response(s.data)

        return Response(s.errors, HTTP_400_BAD_REQUEST)

    def patch(self, request: Request, pk: int) -> Response:
        s = IngredientSerializer(
            Ingredient.objects.get(id=pk),
            request.data,
            partial=True,
        )

        if s.is_valid():
            s.save()

            return Response(s.data)

        return Response(s.errors, HTTP_400_BAD_REQUEST)

    def delete(self, request: Request, pk: int) -> Response:
        Ingredient.objects.get(id=pk).delete()

        return Response()
        # else HTTP_400_BAD_REQUEST
