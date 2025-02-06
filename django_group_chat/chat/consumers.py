import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async

from .models import GroupChat, Message

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user = self.scope['user']
        self.chat_id = self.scope['url_route']['kwargs']['chat_id']
        self.chat = await self.get_chat()
        self.chat_room_id = f'chat_{self.chat_id}'
        
        if self.chat:
            # Join room group
            await self.channel_layer.group_add(
                self.chat_room_id,
                self.channel_name
            )
            
            await self.accept()
        else:
            await self.close(code=400)
            
    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.chat_room_id,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['text']

        await self.save_message(message)

        # Send message to room group
        await self.channel_layer.group_send(
            self.chat_room_id,
            {
                'type': 'chat_message',
                'message': json.dumps({
                    'type': 'msg',
                    'sender': self.user.username,
                    'text': message
                }),
                'sender_channel_name': self.channel_name
            }
        )

    async def chat_message(self, event):
        # Send message to WebSocket
        if self.channel_name != event['sender_channel_name']:
            await self.send(text_data=event['message'])

    async def chat_activity(self, event):
        # Send activity to WebSocket
        await self.send(text_data=event['message'])


    @database_sync_to_async
    def get_chat(self):
        try:
            chat = GroupChat.objects.get(unique_code = self.chat_id)
            return chat
        except GroupChat.DoesNotExist:
            return None

    @database_sync_to_async
    def save_message(self, message):
        Message.objects.create(
            chat=self.chat,
            author_id=self.user.id,
            text=message
        )