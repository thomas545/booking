from django.db import models
from django.contrib.auth import get_user_model
from core.models import TimeStampedModel, UUIDModel
from django_countries.fields import CountryField
from core.compress_img import compress_image

User = get_user_model()


def category_image_path(instance, filename):
    return f"category/{instance.name}/{filename}"


def realty_image_path(instance, filename):
    return f"realty/{instance.realty.name}/{filename}"


def room_image_path(instance, filename):
    return f"realty/room-{instance.room.room_number}/{filename}"


class Category(UUIDModel, TimeStampedModel):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to=category_image_path, blank=True, null=True)
    parent = models.ForeignKey(
        "self", related_name="children", on_delete=models.CASCADE, blank=True, null=True
    )

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Realty(UUIDModel, TimeStampedModel):
    realtor = models.ForeignKey(User, related_name="realty", on_delete=models.CASCADE)
    category = models.ForeignKey(
        Category, related_name="realty", on_delete=models.CASCADE
    )
    name = models.CharField(max_length=250)
    description = models.TextField(blank=True)
    street = models.CharField(max_length=100)
    country = CountryField(blank=True)
    city = models.CharField(max_length=100)
    apartments = models.IntegerField(blank=True, null=True)
    building_number = models.CharField(max_length=50, blank=True, null=True)
    price = models.DecimalField(max_digits=20, decimal_places=2, blank=True)

    class Meta:
        verbose_name_plural = "Realty"

    def __str__(self):
        return self.name


class Room(UUIDModel, TimeStampedModel):
    realty = models.ForeignKey(Realty, related_name="rooms", on_delete=models.CASCADE)
    room_number = models.PositiveIntegerField(blank=True)
    floor = models.PositiveIntegerField(blank=True)
    beds = models.PositiveIntegerField(default=1)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=20, decimal_places=2, blank=True)
    busy = models.BooleanField(default=False)

    def __str__(self):
        return self.realty.name + "-" + str(self.room_number)


class RealtyImage(UUIDModel):
    realty = models.ForeignKey(Realty, related_name="images", on_delete=models.CASCADE)
    image = models.ImageField(upload_to=realty_image_path)

    def __str__(self):
        return self.realty.name

    def save(
        self,
        force_insert=False,
        force_update=False,
        using=None,
        update_fields=None,
        *args,
        **kwargs,
    ):
        # if size greater than 300kb then it will send to compress image function
        image = self.image
        if image and image.size > (0.3 * 1024 * 1024):
            self.image = compress_image(image)
        super(RealtyImage, self).save(*args, **kwargs)


class RoomImage(UUIDModel):
    room = models.ForeignKey(Room, related_name="images", on_delete=models.CASCADE)
    image = models.ImageField(upload_to=room_image_path)

    def __str__(self):
        return str(self.room.room_number)

    def save(
        self,
        force_insert=False,
        force_update=False,
        using=None,
        update_fields=None,
        *args,
        **kwargs,
    ):
        # if size greater than 300kb then it will send to compress image function
        image = self.image
        if image and image.size > (0.3 * 1024 * 1024):
            self.image = compress_image(image)
        super(RoomImage, self).save(*args, **kwargs)
