from django import forms
from .models import User_id, Messenger, Chat

class UserForm(forms.ModelForm):
    class Meta:
        model = User_id
        fields = ['username', 'avatar']


class MessengerForm(forms.ModelForm):
    class Meta:
        model = Messenger
        fields = ['author', 'title']


class ChatForm(forms.ModelForm):
    class Meta:
        model = Messenger
        fields = ['author', 'message']
