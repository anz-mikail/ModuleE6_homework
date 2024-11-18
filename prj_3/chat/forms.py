from django import forms

from .models import UserProfile, Room


class UserForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['nick', 'avatar']


class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['name', 'host', 'current_users']
