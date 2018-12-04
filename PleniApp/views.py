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
    navlinkid_list = list()
    for selected_lecture in selected_lectures:
        selected_lecture.navlinkid += str(selected_lecture.lecture_index_number)
        navlinkid_list.append(selected_lecture.navlinkid)
    unit = str(id)
    context = {
        'lectures': selected_lectures,
        'navlinkid_list': navlinkid_list,
        'unit': unit,
    }
    return render(request, 'pleniapp/index_selected_unit.html', context)

def index_selected_type(request, id):
    selected_lectures = Lecture.objects.filter(lecture_type_index=id)
    navlinkid_list = list()
    for selected_lecture in selected_lectures:
        selected_lecture.navlinkid += str(selected_lecture.lecture_index_number)
        navlinkid_list.append(selected_lecture.navlinkid)
    unit = str(id)
    context = {
        'lectures': selected_lectures,
        'navlinkid_list': navlinkid_list
    }
    return render(request, 'pleniapp/index_selected_type.html', context)


def details(request, id):
    lecture = Lecture.objects.get(id=id)
    context = {
        'lecture': lecture
    }

    return render(request, 'pleniapp/details.html', context)
