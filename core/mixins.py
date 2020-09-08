from rest_framework import status, settings
from rest_framework.response import Response
from django.utils.translation import ugettext_lazy as _u


__all__ = [
    "BulkListModelMixin",
    "BulkCreateModelMixin",
    "BulkDestroyModelMixin",
    "BulkUpdateModelMixin",
]


class BulkListModelMixin:
    """
    Bulk List a queryset.
    """

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class BulkCreateModelMixin:
    """
    Create a model instances.
    Either create a single or many model instances in bulk by using the
    Serializers ``many=True``.

    .. note::
        This mixin uses the same method to create model instances
        as ``CreateModelMixin`` because both non-bulk and bulk
        requests will use ``POST`` request method.
    """

    def create(self, request, *args, **kwargs):
        if not isinstance(request.data, list):
            return super(BulkCreateModelMixin, self).create(request, *args, **kwargs)

        serializer = self.get_serializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )

    def perform_create(self, serializer):
        serializer.save()

    def get_success_headers(self, data):
        try:
            return {"Location": str(data[settings.api_settings.URL_FIELD_NAME])}
        except (TypeError, KeyError):
            return {}


class BulkUpdateModelMixin:
    def get_object(self):
        lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field

        if lookup_url_kwargs in self.kwargs:
            return super(BulkUpdateModelMixin, self).get_object()

        return

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop("partial", False)
        serializer = self.get_serializer(
            self.filter_queryset(self.get_queryset()),
            data=request.data,
            many=True,
            partial=partial,
        )
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def perform_update(self, serializer):
        serializer.save()

    def perform_partial_update(self, request, *args, **kwargs):
        kwargs["partial"] = True
        return self.update(request, *args, **kwargs)


class BulkDestroyModelMixin:
    def destroy(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        self.perform_destroy(queryset)
        return Response(status=status.HTTP_204_NO_CONTENT,)

    def perform_destroy(self, queryset):
        queryset.delete()
