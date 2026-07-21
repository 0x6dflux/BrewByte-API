from typing import Callable

from django.http import Http404
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST


def get_object_or_404(model_name: Callable, pk: int):
    try:
        return model_name.objects.get(id=pk)
    except model_name.DoesNotExist:
        raise Http404(f"{model_name.__name__} Not Found, Invalid `pk={pk}`")


def update_model(
    serializer_name: Callable,
    model_name: Callable,
    request: Request,
    pk: int,
    *,
    partial: bool = False,
):
    s = serializer_name(
        get_object_or_404(model_name, pk),
        request.data,
        partial=partial,
    )

    if s.is_valid():
        s.save()

        return Response(s.data)

    return Response(s.errors, HTTP_400_BAD_REQUEST)
