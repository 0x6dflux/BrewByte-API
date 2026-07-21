from django.db.models import QuerySet
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework.status import (
    HTTP_201_CREATED,
    HTTP_204_NO_CONTENT,
    HTTP_400_BAD_REQUEST,
)


class GeneralMixin:
    query_set: QuerySet
    serializer_class: type[Serializer]

    def _get_query_set(self) -> QuerySet:
        return self.query_set.all()

    def _list(self) -> Response:
        serializer = self.serializer_class(self._get_query_set(), many=True)

        return Response(serializer.data)

    def _create(self) -> Response:
        serializer = self.serializer_class(data=self.request.data)  # type: ignore

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, HTTP_201_CREATED)

        return Response(serializer.errors, HTTP_400_BAD_REQUEST)

    def _retrieve(self, pk: int) -> Response:
        serializer = self.serializer_class(
            get_object_or_404(self._get_query_set(), pk=pk)
        )

        return Response(serializer.data)

    def _update(self, pk: int, *, partial: bool = False) -> Response:
        s = self.serializer_class(
            get_object_or_404(self._get_query_set(), pk=pk),
            self.request.data,  # type: ignore
            partial=partial,
        )

        if s.is_valid():
            s.save()

            return Response(s.data)

        return Response(s.errors, HTTP_400_BAD_REQUEST)

    def _destroy(self, pk: int) -> Response:
        get_object_or_404(self._get_query_set(), pk=pk).delete()

        return Response(status=HTTP_204_NO_CONTENT)
