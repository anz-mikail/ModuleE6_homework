from django.urls import path
from .views import MessengerId, MessengerList, MessengerCreate, UserCreate


urlpatterns = [
    path('messenger/', MessengerList.as_view(), name='messenger_list'),
    path('messenger/<int:pk>', MessengerId.as_view(), name='messenger'),
    path('messenger/create/', MessengerCreate.as_view(), name='messenger_create'),
    path('user/create/', UserCreate.as_view(), name='user_create'),

]
