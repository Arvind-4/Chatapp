import json
from channels.generic.websocket import AsyncWebsocketConsumer
from django.contrib.auth import get_user_model
from channels.db import database_sync_to_async

from .models import ChatRoom, Chat

User = get_user_model()


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'Chat-{self.room_name}'
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name,
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name,
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data['message']
        username = data['username']
        room = data['room']

        await self.save_messages(username, room, message)

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'username': username,
            }
        )

    async def chat_message(self, event):
        message = event['message']
        username = event['username']

        await self.send(
            text_data=json.dumps(
                {
                    'message': message,
                    'username': username,
                }
            )
        )

    @database_sync_to_async
    def save_messages(self, username, room, message):
        user_instance = User.objects.get(username=username)
        if message != '':
            obj = Chat.objects.get_or_create(
                user=User.objects.get(username=username),
                room=ChatRoom.objects.get(name=room),
                content=message
            )
