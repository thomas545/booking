from django.utils.translation import ugettext_lazy as _u
from rest_framework import serializers
from .models import Category, Realty, RealtyImage, Room, RoomImage
from core.writable_nested_serializer import WritableNestedModelSerializer


class CategoryChildrenSerilaizer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            "uuid",
            "name",
            "description",
            "image",
            "children",
        )


class CategorySerilaizer(serializers.ModelSerializer):
    children = CategoryChildrenSerilaizer(many=True)

    class Meta:
        model = Category
        fields = (
            "uuid",
            "name",
            "description",
            "image",
            "children",
        )


class RoomImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomImage
        fields = (
            "uuid",
            "room",
            "image",
        )
        read_only_fields = ("uuid",)


class RoomSerializer(WritableNestedModelSerializer):
    images = RoomImageSerializer(required=False, many=True)

    class Meta:
        model = Room
        fields = (
            "uuid",
            "realty",
            "room_number",
            "floor",
            "beds",
            "description",
            "price",
            "busy",
            "images",
        )
        read_only_fields = ("busy", "uuid",)


class RealtyImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = RealtyImage
        fields = (
            "uuid",
            "realty",
            "image",
        )
        read_only_fields = ("uuid",)

    def get_fields(self, *args, **kwargs):
        fields = super(RealtyImageSerializer, self).get_fields(*args, **kwargs)
        request = self.context.get("request", None)
        if request and getattr(request, "method", None) in ["PUT", "PATCH"]:
            fields["realty"].read_only = True
        return fields

    def validate(self, data):
        realty = data.get("realty", None)
        if realty and realty.images.select_related("realty").all().count() >= 6:
            raise serializers.ValidationError(_u("Maximum images in 6"))
        return data


class RealitySerializer(WritableNestedModelSerializer):
    images = RealtyImageSerializer(required=False, many=True)
    rooms = RoomSerializer(required=False, many=True)

    class Meta:
        model = Realty
        fields = (
            "uuid",
            "realtor",
            "category",
            "name",
            "description",
            "street",
            "country",
            "city",
            "apartments",
            "building_number",
            "price",
            "images",
            "rooms",
        )
        read_only_fields = (
            "realtor",
            "uuid",
        )

