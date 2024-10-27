import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_group_name = 'test'

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept()

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        username = text_data_json['username']  # Get the username from the message
        message = text_data_json['message']

        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'username': username,  # Include the username in the event
                'message': message
            }
        )

    def chat_message(self, event):
        message = event['message']
        username = event['username']  # Get the username from the event

        self.send(text_data=json.dumps({
            'type': 'chat',
            'username': username,  # Include the username in the message sent to the client
            'message': message
        }))

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )
