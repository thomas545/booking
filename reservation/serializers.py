from rest_framework import serializers


class ReservationSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    realty_id = serializers.IntegerField()
    room_numbers = serializers.IntegerField(default=1)
    total_price = serializers.DecimalField(max_digits=12, decimal_places=2, default=0)
    check_in = serializers.DateTimeField(required=False)
    check_out = serializers.DateTimeField(required=False)
