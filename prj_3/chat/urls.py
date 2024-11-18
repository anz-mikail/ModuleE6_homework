from django.urls import path
from . import views

urlpatterns = [
    path('chat/', views.index, name='index'),
    path('chat/<str:room_name>/', views.create_room, name='create_room'),
    path('create_private_chat/<int:user_id>/', views.create_private_chat, name='create_private_chat'),
    path('users/', views.UserList.as_view(), name='user_list'),
    path('rooms/', views.RoomList.as_view(), name='room_list'),
    path('room/edit/<int:pk>/', views.RoomUpdate.as_view(), name='room_edit'),
    path('room/<int:pk>/delete/', views.RoomDelete.as_view(), name='room_delete'),
    path('profile/<int:pk>/', views.CreateProfile.as_view(), name='create_profile'),
    path('profile/<int:pk>/delete/', views.ProfileDelete.as_view(), name='profile_delete'),
]
