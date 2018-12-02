from django.shortcuts import render
from django.http import HttpResponse
from .models import Lecture

# Create your views here.

def index(request):
    lectures = Lecture.objects.all()
    context = {
        'title': 'Lectures and shiet',
        'lectures': lectures
    }
    return render(request, 'pleniapp/index.html', context)

def index_selected_unit(request, id):
    selected_lectures = Lecture.objects.filter(unit_index=id)
    context = {
        'lectures': selected_lectures
    }
    return render(request, 'pleniapp/index_selected_unit.html', context)


def details(request, id):
    lecture = Lecture.objects.get(id=id)
    context = {
        'lecture': lecture
    }

    return render(request, 'pleniapp/details.html', context)
