from rest_framework import serializers
from django.contrib.auth.models import User

from chat_room.models import Room

class UserSerializers(serializers.ModelSerializer):
	'''serializers for user model'''

	class Meta:
		model = User
		fields = ('id', 'username')

class RoomSerializers(serializers.ModelSerializer):
	"""serializer for chat model data"""

	creater = UserSerializers()
	invited = UserSerializers(many=True)
	class Meta:
		model = Room
		fields = ('creater', 'invited', 'date')