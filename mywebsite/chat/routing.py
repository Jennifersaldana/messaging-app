
'''
In order to use a consumer we need to set up routing. (routing.py)
'''
from django.urls import re_path # using re_path due to limitation in url router
from . import consumers # importing our consumers into the routing.py file


# Setting up the websocket url patterns list
# in the websocket url patterns use the repath method and set the route to 
# the new chat consumer. Set the endpoint as what we specificed in the frontend
# whenever we try to make that initial socket connection
websocket_urlpatterns = [
    re_path(r'ws/socket-server/', consumers.ChatConsumer.as_asgi())
]
