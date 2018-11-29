from django.shortcuts import render
from django.http import HttpResponse
from .models import Thread

# Create your views here.

def index(request):

    threads = Thread.objects.all()
    context = {
        'title': 'Threads and shiet',
        'threads': threads
    }
    return render(request, 'pleniapp/index.html', context)


def details(request, id):
    thread = Thread.objects.get(id=id)
    context = {
        'thread': thread
    }

    return render(request, 'pleniapp/details.html', context)
