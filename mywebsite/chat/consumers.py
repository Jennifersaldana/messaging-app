'''
Consumers are the channel's version of Django views except they do more than just respond to requests from the client 
They initiate requests to the client while keeping an open connection
'''

## This is what our consumers inherit from 
import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync

# Create the 1st consumer and inherit from the websocket consumer object
# This is called ChatConsumer since it's responsible for incoming messages 
# from the client and broadcasting out to anyone who has a connection to this consumer in real time
class ChatConsumer(WebsocketConsumer):

    # Consumers structure our code into a series of functions (connect, receive, disconnect)

    # This is the respond method
    def connect(self):  # Connect method for the initial request that comes in from the client
        self.room_group_name = 'test'  # Dynamic value from a user or URL

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept()  # Send a message to the client that the connection was made

    def receive(self, text_data):  # Receive messages from the client
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    def chat_message(self, event):
        message = event['message']

        self.send(text_data=json.dumps({
            'type': 'chat',  # Specify the message type for the client
            'message': message
        }))

    # Optionally, you might want to implement a disconnect method
    def disconnect(self, close_code):
        # Leave the room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )
