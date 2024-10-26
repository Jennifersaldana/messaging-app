from django.shortcuts import render

# Create your views here.
def lobby(request):
    return render(request, 'chat/lobby.html') # when you init the server with 'python manage.py runserver'