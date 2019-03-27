from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Room(models.Model):
	"""Models for chat room"""

	creater = models.ForeignKey(User, verbose_name='creater', on_delete=models.CASCADE)
	invited = models.ManyToManyField(User, verbose_name='invited users', related_name='invited_users')
	date = models.DateTimeField('date of creation', auto_now_add=True)

	class Meta:
		verbose_name = 'Chat room'
		verbose_name_plural = 'Chat rooms'


class Chat(models.Model):
	"""Model of chat"""

	room = models.ForeignKey(Room, verbose_name='chat room', on_delete=models.CASCADE)
	user = models.ForeignKey(User, verbose_name='user', on_delete=models.CASCADE)
	text = models.TextField('Message...',max_length=500)
	date = models.DateTimeField('date of writing', auto_now_add=True)


	class Meta:
		verbose_name = 'message room'
		verbose_name_plural = 'messages room'
