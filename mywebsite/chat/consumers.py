''''
Consumers are the channel's version of dijango views execpt they do more than just respond to request from the client 
Initiate requests to the client while keeping an open connection
'''

## This is what our consumers inherit from 
import json
from channels.generic.websocket import WebsocketConsumer

# create 1st consumer and inherit from the websocket consumer object
# This is called ChatConsumer since its responsible for incoming messages 
# from the client and broadcasting out to anyone who has a connection to this consumer in real time
class ChatConsumer(WebsocketConsumer):

# Consumers strcuture our code into a series of functions (connect, recieve, disconnect)

    # this is respond
    def connect(self): # connect method for the initial requestion that comes in from the client
        self.accept() # send a message to client that the connection was made
        self.send(text_data = json.dumps({ # receieve the message from the client side
            'type' : 'connection_established', #stringified values
            'message' : 'you are now connected!'
        }))
    
    # def receive(self, text_data=None, bytes_data=None): # receieve messages from the client
    #     return super().receive(text_data, bytes_data)
    
    # def disconnect(self, code): # disconnect method for handle what happens when a client disconnects from the consumer
    #     return super().disconnect(code)