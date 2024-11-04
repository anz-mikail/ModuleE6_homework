from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView
from django.shortcuts import get_object_or_404, render, reverse
from django.http import HttpResponseRedirect

from .models import UserProfile, Room


def index(request):
    return render(request, 'index.html', {})

def room(request, room_name):
    return render(request, 'room.html', {
        'room_name': room_name
    })


class UserList(ListView):
    model = User
    template_name = 'user_list.html'
    context_object_name = 'user_list'


class RoomList(ListView):
    model = Room
    template_name = 'room_list.html'
    context_object_name = 'room_list'



# def create_chat_view(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         participants = request.POST.getlist('participants')
#
#         participants.append(request.user.id)

        # if len(participants) >= 3:
        #     chat = Room.objects.create(name=name)
        #     chat.participants.add(*participants)
        #     return redirect('chat_room', chat_id=chat.id)
        # else:
        #     chat = Room.objects.create(name=name)
        #     chat.participants.add(*participants)
        #     return redirect('private_chat', user_id=participants[1])

#     users = User.objects.exclude(id=request.user.id)
#     return render(request, 'create_chat.html', {'users': users})
#
#
# def chat_room_view(request, chat_id):
#     chat = get_object_or_404(Room, id=chat_id)
#     room_name = chat.name
#     participants_count = chat.participants.count()
#
#     return render(request, 'chat_room.html', {
#         'chat': chat,
#         'room_name': room_name,
#         'participants_count': participants_count
#     })


# def index(request):
#     if request.method == "POST":
#         name = request.POST.get("name", None)
#         if name:
#             room = Room.objects.create(name=name, host=request.user)
#             HttpResponseRedirect(reverse("room", args=[room.pk]))
#     return render(request, 'ind.html')
#
# def room(request, pk):
#     room: Room = get_object_or_404(Room, pk=pk)
#     return render(request, 'ro.html', {
#         "room":room,
#     })