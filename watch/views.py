from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    return render(request,'watch/watch.html')

def room(request, room_name):
    return render(request, 'watch/room.html', {
        'room_name': room_name
    })
