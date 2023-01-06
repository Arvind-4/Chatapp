from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()


class ChatRoom(models.Model):
    user = models.ManyToManyField(User)
    name = models.CharField(max_length=225)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def chat_room_url(self, *args, **kwargs):
        name = self.name
        endpoint = f'/chat/{name}/'
        return endpoint


class Chat(models.Model):
    user = models.ForeignKey(User, models.CASCADE)
    room = models.ForeignKey(ChatRoom, models.CASCADE)
    content = models.TextField(max_length=1000)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content
