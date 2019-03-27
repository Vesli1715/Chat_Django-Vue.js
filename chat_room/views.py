from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions

from chat_room.models import Room, Chat
from chat_room.serializers import RoomSerializers, ChatSerializers

class Rooms(APIView):

	def get(self, request):
		rooms = Room.objects.all()
		serializer = RoomSerializers(rooms, many=True)
		return Response({'DATA': serializer.data})


class Dialog(APIView):
	'''Chat dialog, messages'''

	def get(self, request):
		room = request.GET.get('room')
		chat = Chat.objects.filter(room=room)

		serializer = ChatSerializers(chat, many=True)
		return Response({'data': serializer.data})


	def post(self, request):
		#room = request.data.get('room')
		dialog = ChatSerializers(data=request.data)
		if dialog.is_valid():
			dialog.save(user=request.user)
			return Response({'status': 'Add '})
		else:
			return Response({'status': 'Error'})