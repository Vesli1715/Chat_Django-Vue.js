from rest_framework import serializers
from django.contrib.auth.models import User

from chat_room.models import Room, Chat

class UserSerializers(serializers.ModelSerializer):
	'''Serializers for user model'''

	class Meta:
		model = User
		fields = ('id', 'username')

class RoomSerializers(serializers.ModelSerializer):
	"""Serializer for chat model data"""

	creater = UserSerializers()
	invited = UserSerializers(many=True)
	class Meta:
		model = Room
		fields = ('creater', 'invited', 'date')


class ChatSerializers(serializers.ModelSerializer):

	user = UserSerializers()
	class Meta:
		model = Chat
		fields = ('user', 'text', 'date')


class ChatPostSerializers(serializers.ModelSerializer):

	class Meta:
		model = Chat
		fields = ('room', 'text')