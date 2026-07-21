from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST

from config.utils import get_object_or_404, update_model
from inventory.models import Category
from inventory.serializers import CategorySerializer


@api_view(["GET", "POST"])
def category_list_create(request: Request) -> Response:
    match request.method:
        case "GET":
            s = CategorySerializer(Category.objects.all(), many=True)

            return Response(s.data)

        case "POST":
            s = CategorySerializer(data=request.data)

            if s.is_valid():
                s.save()

                return Response(s.data, HTTP_201_CREATED)

            return Response(s.errors, HTTP_400_BAD_REQUEST)

        case _:
            # the api_view decorator returns `"detail": "Method \"PATCH\" not allowed."`
            # but, this case has been inserted to prevent the mypy missing return
            return Response({"Detail": "Method Not Allowed"}, HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "PATCH", "DELETE"])
def category_retrieve_update_destroy(request: Request, pk: int) -> Response:
    match request.method:
        case "GET":
            s = CategorySerializer(get_object_or_404(Category, pk))

            return Response(s.data)

        case "PUT":
            return update_model(CategorySerializer, Category, request, pk)

        case "PATCH":
            return update_model(CategorySerializer, Category, request, pk, partial=True)

        case "DELETE":
            get_object_or_404(Category, pk).delete()

            return Response()

        case _:
            # the api_view decorator returns `"detail": "Method \"POST\" not allowed."`
            # this case has been inserted to prevent the mypy missing return
            return Response({"Detail": "Method Not Allowed"}, HTTP_400_BAD_REQUEST)
