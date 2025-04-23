from django.urls import path
from .views import HomeView, RoomView


urlpatterns = [
    path("", HomeView, name="login"),
    path("<str:room_name>/<str:user_name>/", RoomView, name="room")
]