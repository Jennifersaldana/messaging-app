"""
ASGI config for mywebsite project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter # import URLRounter method
from channels.auth import AuthMiddlewareStack
# AuthMiddleware and channels support standard django authentication 
# where the user details are stored in a session. AuthMiddleware requires
# SessionMiddleware to funCtion. SessionMiddleware requires CookiesMiddleware.
# These are all combined in the AuthMiddlewareStack. 


import chat.routing  # import routing.py file


'''
intergrate channels: 
1. start by creating the routin configuration
- A channels routing configuration is an asgi application that is similar to a django connfiguration.
It tell channels what code to run when an http request is received by a channel server.
'''

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mywebsite.settings')



application = ProtocolTypeRouter({ # added ProtocolTypeRouter to use the newly portal 
    'http': get_asgi_application(), # added to use the newly imported protocal type router
    # Add other protocols like websocket here when needed
    'websocket' : AuthMiddlewareStack( # add websocket to the list of protocols and use the stack
        URLRouter(
            chat.routing.websocket_urlpatterns # pass in the websocket url patterns list from routing.py
        )
    )
})