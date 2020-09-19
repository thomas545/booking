from django.urls import path, include
from . import views, viewsets


urlpatterns = [
    path('reserve-room/', views.ReserveRoomView.as_view(), name="reserve_room"),
]