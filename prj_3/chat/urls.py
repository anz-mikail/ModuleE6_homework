from django.urls import path
from . import views

urlpatterns = [
    path('chat/', views.index, name='index'),
    path('chat/<str:room_name>/', views.room, name='room'),
    path('users/', views.UserList.as_view(), name='user_list'),
    path('rooms/', views.RoomList.as_view(), name='room_list'),
    # path('create_chat/', create_chat_view, name='create_chat'),
    # path('chat/<int:chat_id>/', chat_room_view, name='chat_room'),
    # path('', views.index, name='ind'),
    # path('room/<int:pk>/', views.room, name='room'),
]
