from django.urls import path
from chat_room.views import *

urlpatterns = [
	path('room/', Rooms.as_view())
]
