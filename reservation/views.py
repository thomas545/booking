from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import ReservationSerializer
from .services import create_reservation


class ReservationAPIView(generics.GenericAPIView):
    serializer_class = ReservationSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        reservation = create_reservation(**serializer.validated_data)
        return Response(
            {"message": "Reservation done successfully!", "id": reservation.pk}
        )
