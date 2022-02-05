from django.urls import path, include
from . import views, viewsets


urlpatterns = [
    path("reserve/", views.ReservationAPIView.as_view(), name="reserve"),
]