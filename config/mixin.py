from typing import Callable

from django.http.response import Http404
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST


class DetailMixin:
    model_class: Callable
    serializer_class: Callable

    # what is the return type hint? it returns an object of a class
    def _get_object_or_404(self, pk: int):
        try:
            return self.model_class.objects.get(id=pk)
        except self.model_class.DoesNotExist:
            raise Http404(f"{self.model_class.__name__} Not Found, Invalid `pk={pk}`")

    def _update_product(self, pk: int, *, partial: bool = False) -> Response:
        s = self.serializer_class(
            self._get_object_or_404(pk),
            self.request.data,
            partial=partial,
        )

        if s.is_valid():
            s.save()

            return Response(s.data)

        return Response(s.errors, HTTP_400_BAD_REQUEST)
