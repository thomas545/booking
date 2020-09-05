from rest_framework.permissions import BasePermission, SAFE_METHODS
from .models import Realty, RealtyImage, Room, RoomImage

CHANGE_METHODS = ["PUT", "PATCH"]


class CRUDRealtyPermission(BasePermission):
    """
    The request is authenticated as a user, or is a read-only request.
    """

    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS
            or request.user
            and request.user.is_authenticated
        )

    def has_object_permission(self, request, view, obj):
        if isinstance(obj, Realty) and request.method in CHANGE_METHODS:
            return obj.realtor == request.user
        return False

