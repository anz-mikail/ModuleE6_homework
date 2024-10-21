from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from .models import User_id, Messenger, Chat
from .forms import MessengerForm, UserForm


class MessengerList(ListView):
    model = Messenger
    template_name = 'messenger_list.html'
    context_object_name = 'messenger_list'


class MessengerId(DetailView):
    model = Messenger
    template_name = 'messenger.html'
    context_object_name = 'messenger'


class MessengerCreate(CreateView):
    form_class = MessengerForm
    model = Messenger
    template_name = 'messenger_create.html'
    success_url = '/messenger/'


class UserCreate(CreateView):
    form_class = UserForm
    model = User_id
    template_name = 'user_create.html'
    success_url = '/messenger/'

