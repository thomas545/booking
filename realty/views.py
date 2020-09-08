from django.shortcuts import get_object_or_404
from rest_framework import permissions, status, generics, views, filters
from rest_framework.response import Response

from core.generics import BulkListCreateDestroyAPIView

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
