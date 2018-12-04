from django.shortcuts import render
from django.http import HttpResponse
from .models import Lecture

# Create your views here.

def index(request):
    lectures = Lecture.objects.all()
    imgbtnindex_list = [1,2,3,4,5,6,7,8,9]
    context = {
        'title': 'Lectures and shiet',
        'lectures': lectures,
        'imgbtnindex_list': imgbtnindex_list,
    }
    return render(request, 'pleniapp/index.html', context)

def index_selected_unit(request, id):
    selected_lectures = Lecture.objects.filter(unit_index=id)
    navlinkid_list = list()
    for selected_lecture in selected_lectures:
        selected_lecture.navlinkid += str(selected_lecture.lecture_index_number)
        navlinkid_list.append(selected_lecture.navlinkid)
    if id==1:
        unit_description = "En la primera unidad se nos presentan conceptos básicos de la computadora, dispositivos de entrada y salida que nos ayudan para poder manejar la computadora a introducir la información, también vamos a empezar a manejar ciertos programas que nos ayudaran a familiarizar con la computadora y el usuario, como lo es Paint, calculadora y Word, también tendremos una introducción sobre internet, como realizar búsquedas, usar correo y redes sociales para que se puedan mantener conectados."
    if id==2:
        unit_description = "En la segunda unidad se nos presentan conceptos ya avanzados de Word donde podremos usar más opciones que nos permitan hacer mayor énfasis en nuestros textos dando un mejor resultado en ellos agregando títulos, imágenes, figuras, cuadros y más textos coloridos. Posterior a esto empezamos con conceptos básicos de Excel, como son sumas, restas, multiplicaciones y divisiones, también a poder darle formato a secuencias de números para llevar un mejor control sobre nuestra información, y para finalizar veremos un poco de fórmulas en Excel para tener mayor contacto con la información que ingresemos."
    if id==3:
        unit_description = "En la tercera unidad veremos conceptos de PowerPoint y Publisher, donde se podrán aplicar conceptos de la unidad 1 y 2 que nos apoyarán en realizar presentaciones básicas y bien hechas para que los adultos las presenten durante la clase. "
    unit = str(id)
    context = {
        'lectures': selected_lectures,
        'navlinkid_list': navlinkid_list,
        'unit': unit,
        'unit_description': unit_description
    }
    return render(request, 'pleniapp/index_selected_unit.html', context)

def index_selected_type(request, id):
    selected_lectures = Lecture.objects.filter(lecture_type_index=id)
    navlinkid_list = list()
    exception = "empty_queryset"
    for selected_lecture in selected_lectures:
        exception = "none"
        selected_lecture.navlinkid += str(selected_lecture.lecture_index_number)
        navlinkid_list.append(selected_lecture.navlinkid)
    if id==1:
        type = "Correo Gmail"
    if id==2:
        type = "Explorador de Internet"
    if id==3:
        type = "Windows"
    if id==4:
        type = "Facebook"
    if id==5:
        type = "Youtube"
    if id==6:
        type = "Microsoft Office"
    if id==7:
        type = "Equipo de Computo"
    if id==8:
        type = "Juegos"
    if id==9:
        type = "Paint"
    context = {
        'lectures': selected_lectures,
        'navlinkid_list': navlinkid_list,
        'exception': exception,
        'type': type,
    }
    return render(request, 'pleniapp/index_selected_type.html', context)


def details(request, id):
    lecture = Lecture.objects.get(id=id)
    context = {
        'lecture': lecture,
        'ytlink': 'tgbNymZ7vqY',
    }

    return render(request, 'pleniapp/details.html', context)
