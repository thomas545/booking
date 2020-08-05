from django.db import models
from django.utils.translation import ugettext_lazy as _u
from core.models import UUIDModel, TimeStampedModel
from reservation.models import Reservation


class Transaction(UUIDModel, TimeStampedModel):
    PAY_CASH = "c"
    PAY_CREDIT = "r"

    PAYMENT_CHOICES = (
        (PAY_CASH, _u("Cash")),
        (PAY_CREDIT, _u("Credit Card")),
    )

    reservation = models.OneToOneField(
        Reservation, related_name="transaction", on_delete=models.CASCADE
    )
    payment_fees = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    paid = models.BooleanField(default=False)
    payment_method = models.CharField(
        max_length=1, choices=PAYMENT_CHOICES, default=PAY_CASH
    )
    total_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)

