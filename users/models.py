from django.db import models
from django.dispatch import receiver
from django.utils.translation import ugettext_lazy as _u
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from core.models import UUIDModel, TimeStampedModel
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField
from realty.models import Realty

User = get_user_model()


def profile_photo_path(instance, filename):
    return f"profile/{instance.user.username}_{instance.user.id}/{filename}"


class Profile(UUIDModel):
    MALE = "m"
    FEMALE = "f"
    OTHER = "o"

    GENDER_CHOICES = (
        (MALE, "Male"),
        (FEMALE, "Female"),
        (OTHER, "Other"),
    )

    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    photo = models.ImageField(upload_to=profile_photo_path, blank=True, null=True)
    phone_number = PhoneNumberField(blank=True, null=True)
    abount = models.TextField(blank=True, null=True)
    gender = models.CharField(
        max_length=1, choices=GENDER_CHOICES, blank=True, null=True
    )
    birth_date = models.DateTimeField(blank=True, null=True)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, *args, **kwargs):
    if created:
        Profile.objects.create(user=instance)


class Address(UUIDModel, TimeStampedModel):
    user = models.ForeignKey(User, related_name="addresses", on_delete=models.CASCADE)
    street = models.CharField(max_length=100)
    country = CountryField(default="EG")
    city = models.CharField(max_length=100)
    apartment = models.IntegerField(blank=True, null=True)
    building_number = models.CharField(max_length=50, blank=True, null=True)


class Feedback(UUIDModel, TimeStampedModel):
    HAPPY = 1
    GOOD = 0
    SAD = -1

    SERVICE_CHOICES = ((HAPPY, _u("Happy")), (GOOD, _u("Good")), (SAD, _u("Sad")))

    user = models.ForeignKey(
        User, related_name="user_feedbacks", on_delete=models.CASCADE
    )
    realty = models.ForeignKey(
        Realty, related_name="realty_feedbacks", on_delete=models.CASCADE
    )
    service_rate = models.CharField(max_length=1, choices=SERVICE_CHOICES, default=GOOD)
    rating = models.IntegerField(
        validators=[
            MinValueValidator(1, message=_u("Minimun rate is 1")),
            MaxValueValidator(5, message=_u("Maximum rate is 5")),
        ]
    )
    review = models.TextField(max_length=300)

    def __str__(self):
        return self.user.username + "-" + self.realty.name