from .models import Reservation


def create_reservation(**valid_fields):
    return Reservation.objects.create(**valid_fields)

