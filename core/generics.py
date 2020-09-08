from rest_framework.generics import GenericAPIView
from rest_framework.viewsets import ModelViewSet
from . import mixins


class BulkListAPIView(mixins.BulkListModelMixin, GenericAPIView):
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class BulkCreateAPIView(mixins.BulkCreateModelMixin, GenericAPIView):
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class BulkUpdateAPIView(mixins.BulkUpdateModelMixin, GenericAPIView):
    def put(self, request, *args, **kwargs):
        # TODO Not completed yet!
        return self.update(request, *args, **kwargs)


class BulkDestroyView(mixins.BulkDestroyModelMixin, GenericAPIView):
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class BulkListCreateDestroyAPIView(
    mixins.BulkListModelMixin,
    mixins.BulkCreateModelMixin,
    mixins.BulkDestroyModelMixin,
    GenericAPIView,
):
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
