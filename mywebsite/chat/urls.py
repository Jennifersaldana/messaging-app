from django.urls import path
from . import views

urlpatterns = [ # url patterns list 
    path ('', views.lobby) # set url route and return lobby view
]