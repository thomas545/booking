from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .serializers import ReservationSerializer
from .models import Reservation

class ReserveRoomView(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = ReservationSerializer
    queryset = Reservation.objects.all()
