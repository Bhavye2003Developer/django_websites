from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Room, Message

# Create your views here.

def home(request):
    if request.method == 'POST':
        room_name = request.POST['roomName']
        username = request.POST['username']
        # print(room_name, username)
        if (Room.objects.filter(room_name = room_name).exists()==False):
            print("does not exists")
            room = Room(room_name = room_name)
            room.save()
        return redirect("room", roomName=room_name, user=username)

    return render(request, 'index.html', {})

def room(request, roomName, user):

    room = Room.objects.get(room_name = roomName)
    all_messages = Message.objects.filter(room = room)

    if request.method=="POST":
        message = request.POST["message"]
        new_message = Message(room = room, username = user, message = message)
        new_message.save()

        return redirect("room", roomName=roomName, user = user)
    return render(request, "room.html", {"messages":all_messages, 'user':user, "roomName":roomName})