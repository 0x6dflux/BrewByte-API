from typing import Callable

from django.http.response import Http404
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST


class DetailMixin:
    model_name: Callable
    serializer_name: Callable

    # what is the return type hint? it returns an object of a class
    def _get_object_or_404(self, pk: int):
        try:
            return self.model_name.objects.get(id=pk)
        except self.model_name.DoesNotExist:
            raise Http404(f"Product Not Found, Invalid `pk={pk}`")

    def _update_product(self, pk: int, *, partial: bool = False) -> Response:
        s = self.serializer_name(
            self._get_object_or_404(pk),
            self.request.data,
            partial=partial,
        )

        if s.is_valid():
            s.save()

            return Response(s.data)

        return Response(s.errors, HTTP_400_BAD_REQUEST)
