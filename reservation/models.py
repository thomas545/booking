import math
from django.db import models
from django.contrib.auth import get_user_model
from core.models import UUIDModel, TimeStampedModel
from realty.models import Realty, Room

User = get_user_model()


class Reservation(UUIDModel, TimeStampedModel):
    user = models.ForeignKey(
        User, related_name="user_reservations", on_delete=models.CASCADE
    )
    realty = models.ForeignKey(
        Realty, related_name="realty_reservations", on_delete=models.CASCADE
    )
    room = models.ForeignKey(
        Room,
        related_name="room_reservations",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    room_numbers = models.PositiveIntegerField(default=1)
    total_price = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    check_in = models.DateTimeField(blank=True)
    check_out = models.DateTimeField(blank=True)

    def save(self, *args, **kwargs):
        days = (self.check_out - self.check_in).days
        self.total_price = (float(self.room.price) * float(self.room_numbers)) * float(
            days
        )
        super(Reservation, self).save(*args, **kwargs)
