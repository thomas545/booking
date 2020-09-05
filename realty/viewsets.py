from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from rest_framework import permissions, status, viewsets, filters
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .permissions import CRUDRealtyPermission
from .serializers import RealitySerializer, RealtyImageSerializer
from .models import Realty, RealtyImage
from .filters import RealtyFilters

class RealityViewSet(viewsets.ModelViewSet):
    permission_classes = (CRUDRealtyPermission,)
    serializer_class = RealitySerializer
    queryset = Realty.objects.all()
    lookup_field = "uuid"
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filterset_class = RealtyFilters
    search_fields = ("name",)
    ordering_fields = ('created', 'price')

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(realtor=request.user)
        return Response(serializer.data)

