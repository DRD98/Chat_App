from django.shortcuts import render, redirect

from .models import Room, Message


def HomeView(request):
    print("\n ------------------ request = ", request)
    if request.method == 'POST':
        username = request.POST['username']
        room_name = request.POST['room_name']
        try:
            exists = Room.objects.get(room_name__iexact=room_name)
        except Room.DoesNotExist:
            Room.objects.create(room_name=room_name)
        redirect("room", room_name=room_name, username=username)
    return render(request, "home.html")


def RoomView(request, room_name, user_name):
    room_exists = Room.objects.get(room_name__iexact=room_name)
    previous_messages = Message.objects.filter(room=room_exists)
    context = {
        "messages": previous_messages,
        "user": user_name,
        "room_name": room_exists.room_name
    }
    return render(request, "room.html", context)
