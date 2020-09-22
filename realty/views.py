from django.shortcuts import get_object_or_404
from rest_framework import permissions, status, generics, views, filters
from rest_framework.response import Response

from core.generics import BulkListCreateDestroyAPIView, BulkUpdateAPIView

from .serializers import CategorySerilaizer, BulkCategoryCreateSerilaizer
from .models import Category


class CategoryView(generics.ListAPIView):
    serializer_class = CategorySerilaizer
    queryset = Category.objects.all().select_related("parent")
    filter_backends = (
        filters.SearchFilter,
        filters.OrderingFilter,
    )
    search_fields = (
        "name",
        "description",
    )
    ordering_fields = (
        "created",
        "name",
    )

class BulkCategoryView(BulkListCreateDestroyAPIView):
    serializer_class = BulkCategoryCreateSerilaizer
    queryset = Category.objects.all()


class BulkUpdatecategory(BulkUpdateAPIView):
    serializer_class = BulkCategoryCreateSerilaizer
    queryset = Category.objects.all()

    def get_queryset(self, ids=None):
        if ids:
            return Category.objects.filter(id__in=ids)

        return Category.objects.all()
    
    def update(self, request, *args, **kwargs):
        ids = request.GET.getlist("ids", [])
        if not ids:
            return Response("Nooooo IDS") 
        instances = self.get_queryset(ids=ids)
        serializer = self.get_serializer(instances, data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)