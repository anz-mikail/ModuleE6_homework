from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.template import context
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import get_object_or_404, render, reverse
from django.http import HttpResponseRedirect

from .models import Room, UserProfile
from .forms import UserForm, RoomForm


def create_private_chat(request, user_id):
    other_user = get_object_or_404(User, id=user_id)
    a = int(f"{request.user.id}")
    b = int(f"{other_user.id}")
    if a > b:
        room_name = f"{request.user.id}{other_user.id}"
    else:
        room_name = f"{other_user.id}{request.user.id}"

    room, created = Room.objects.get_or_create(
        name=room_name,
        defaults={'host': request.user, 'is_private': True}
    )

    context['is_private'] = user_id.id in room.is_private

    room.current_users.add(request.user, other_user)
    return redirect('create_room', room_name=room.name)


def index(request):
    return render(request, 'index.html', {})


def create_room(request, room_name):

    room, created = Room.objects.get_or_create(
        name=room_name,
        defaults={'host': request.user, 'is_private': False}
    )
    room.current_users.add(request.user)

    return render(request, 'room.html', {
        'room_name': room_name
    })


class RoomUpdate(UpdateView):
    form_class = RoomForm
    model = Room
    template_name = 'room_edit.html'
    success_url = '/rooms/'


class RoomDelete(DeleteView):
    model = Room
    template_name = 'room_delete.html'
    success_url = '/chat/'


class RoomList(ListView):
    model = Room
    template_name = 'room_list.html'
    context_object_name = 'room_list'


class CreateProfile(CreateView):
    form_class = UserForm
    model = UserProfile
    template_name = 'profile_create.html'
    success_url = '/chat/'

    def form_valid(self, form):
        userprofile = form.save(commit=False)
        userprofile.user = self.request.user
        userprofile.id = self.request.user.id
        userprofile.save()
        return super().form_valid(form)


class ProfileDelete(DeleteView):
    model = UserProfile
    template_name = 'profile_delete.html'
    success_url = '/chat/'


class UserList(ListView):
    model = User
    template_name = 'user_list.html'
    context_object_name = 'user_list'



