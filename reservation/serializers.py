from rest_framework import serializers
from .models import Reservation


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = (
            "uuid",
            "created",
            "total_price",
            "user",
            "realty",
            "room",
            "room_numbers",
            "check_in",
            "check_out",
        )
        read_only_fields = (
            "total_price",
            "uuid",
            "created",
        )

