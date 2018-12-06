from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Lecture, User, Comment
from .forms import UserSignInForm, CreateLectureForm
import json


# REGULAR USER STARTS #
# REGULAR USER STARTS #

def sign_in_valid(request):
    if 'username' in request.session:
        return True
    else:
        return False


def register_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        User.objects.create(
            username = username,
            password = password
        )
        return HttpResponse('')

def signin_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        users = User.objects.filter(user_type="regular")
        for user in users:
            if (username == user.username) and (password == user.password):
                request.session['username'] = user.username
                return JsonResponse({
                    'username': request.session['username']
                })

    return JsonResponse({
        'username': "no_match"
    })

def signout_user(request):
    request.session.flush()
    return redirect('sign_in')

# REGULAR USER ENDS #
# REGULAR USER ENDS #


# ADMIN USER STARTS #
# ADMIN USER STARTS #
def sign_in_valid_admin(request):
    if 'username_admin' in request.session:
        return True
    else:
        return False

def register_user_admin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        User.objects.create(
            username = username,
            password = password,
            user_type = "admin"
        )
        return HttpResponse('')

def signin_user_admin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        users = User.objects.filter(user_type="admin")
        for user in users:
            if (username == user.username) and (password == user.password):
                request.session['username_admin'] = user.username
                return JsonResponse({
                    'username': request.session['username_admin']
                })

    return JsonResponse({
        'username': "no_match"
    })


def signout_user_admin(request):
    request.session.flush()
    return redirect('sign_in_admin')

# ADMIN USER ENDS #
# ADMIN USER ENDS #





# Create your views here.

def sign_in(request):
    if sign_in_valid(request):
        return redirect('index')
    else:
        form = UserSignInForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

        return render(request, 'pleniapp/sign_in.html', {"form":form})

def sign_in_admin(request):
    if sign_in_valid_admin(request):
        return redirect('index_admin')
    else:
        form = UserSignInForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

        return render(request, 'pleniapp/sign_in_admin.html', {"form":form})

def index(request):
    if sign_in_valid(request):
        lectures = Lecture.objects.all()
        imgbtnindex_list = [1,2,3,4,5,6,7,8,9]
        context = {
            'user': request.session['username'],
            'title': 'Lectures and shiet',
            'lectures': lectures,
            'imgbtnindex_list': imgbtnindex_list,
        }
        return render(request, 'pleniapp/index.html', context)
    else:
        return redirect('sign_in')


def index_admin(request):
    if sign_in_valid_admin(request):
        lectures = Lecture.objects.all()
        navlinkid_list = list()
        i=1
        for lecture in lectures:
            lecture.navlinkid += str(i)
            navlinkid_list.append(lecture.navlinkid)
            i+=1
        context = {
            'user': request.session['username_admin'],
            'title': 'Lectures and shiet',
            'lectures': lectures,
            'navlinkid_list': navlinkid_list,
        }
        return render(request, 'pleniapp/index_admin.html', context)
    else:
        return redirect('sign_in_admin')


def index_selected_unit(request, id):
    if sign_in_valid(request):
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
            'user': request.session['username'],
            'lectures': selected_lectures,
            'navlinkid_list': navlinkid_list,
            'unit': unit,
            'unit_description': unit_description
        }
        return render(request, 'pleniapp/index_selected_unit.html', context)
    else:
        return redirect('sign_in')


def index_selected_type(request, id):
    if sign_in_valid(request):
        selected_lectures = Lecture.objects.filter(lecture_type_index=id)
        navlinkid_list = list()
        i=1
        exception = "empty_queryset"
        for selected_lecture in selected_lectures:
            exception = "none"
            selected_lecture.navlinkid += str(i)
            navlinkid_list.append(selected_lecture.navlinkid)
            i+=1
        if id==1:
            type = "Correo Gmail"
            type_description = "En este tema de Gmail aprenderemos desde cero todo lo que puede hacerse con esta fantástica herramienta de Google para aumentar nuestra productividad, en el trabajo, escuela o en nuestra vida cotidiana, Gmail es sin duda la aplicación de correo electrónico más completa, flexible y versátil en la actualidad ya que casi la mayoría de las aplicaciones puedes ingresar un correo Gmail."
        if id==2:
            type = "Explorador de Internet"
            type_description = "En este tema del Explorador de internet aprenderemos desde cero todo lo que puede hacerse con esta fantástica herramienta que nos promociona muchos beneficios para poder estar conectados siempre a la red, donde podemos buscar información, usar mapas, ver videos, ingresar a nuestros correos y entre otros beneficios que podremos tener con esta valiosa herramienta."
        if id==3:
            type = "Windows"
            type_description = "En este tema de Windows podremos aprender todo lo necesario para poder abrir las distintas aplicaciones con la que cuenta nuestra computadora, de igual forma a poder navegar dentro de nuestros archivos y de esta forma poder copiar, borra o guardar lo que no necesitemos, también podremos saber cómo conectar a internet desde las opciones de wifi que tiene nuestra computadora."
        if id==4:
            type = "Facebook"
            type_description = "En este tema de Facebook podremos ver cómo crear una cuenta de Facebook, como configurarla para tener mayor privacidad, también a realizar búsquedas avanzadas de amigos, a poder añadir contenido a nuestro perfil, enviar mensajes por esta plataforma, también se mostrará la forma de cómo realizar una página que nos podrá ser útil para una pequeña empresa que tengamos."
        if id==5:
            type = "Youtube"
            type_description = "En este tema de YouTube aprenderemos a poder ingresar a una aplicación muy útil desde registro si es necesario hasta la búsqueda de un video en la aplicación, aparte en este servicio podremos encontrar literalmente millones de videos de todo tipo, subidos por usuarios y empresas, incluyendo videos humorísticos, videos de Hágalo Ud. Mismo, cine, televisión, y cientos de categorías más. Aparte no es la única función de YouTube no es esta, ya que también podremos subir nuestros propios videos en forma sencilla para poderlos compartir con los millones de usuarios del sitio."
        if id==6:
            type = "Microsoft Office"
            type_description = "En este curso de Office básico aprenderás a utilizar las herramientas de Microsoft Word, Excel y Power Point. Microsoft Word, te servirá para desarrollar, dar formato y corregir textos, en Microsoft Excel, un programa de hojas de cálculo, te ayudará a calcular tareas financieras y contables, con fórmulas y gráficos, y en Microsoft Power, herramienta diseñada para hacer presentaciones con texto, así como presentaciones en diapositivas, animaciones de texto e imágenes prediseñadas o importadas desde imágenes e la computadora, donde se pueden aplicar distintos diseños de fuente, plantilla y animación."
        if id==7:
            type = "Equipo de Computo"
            type_description = "Bueno en el tema siguiente se explicará la forma de como se utilizan ciertas partes de la computadora desde el monitor, teclado mause, bocinas, impresoras, veremos cómo se usan que necesitamos para conectarlas que información nos va a arrojar como tenemos que mover o usarlas de forma correcta entre otras cosas básicas para el uso de nuestra computadora."
        if id==8:
            type = "Juegos"
            type_description = "Bueno en el tema siguiente podremos ver como se ingresan a los juegos con los que cuenta la computadora, y ya estando dentro poder ver las instrucciones de cada juego que usemos."
        if id==9:
            type = "Paint"
            type_description = "Bueno en este curso vamos a ver el programa que viene con todas las versiones de Windows, y cuya principal utilidad es crear dibujos sencillos o modificar imágenes de una manera básica."
        context = {
            'user': request.session['username'],
            'lectures': selected_lectures,
            'navlinkid_list': navlinkid_list,
            'exception': exception,
            'type': type,
            'type_description': type_description,
        }
        return render(request, 'pleniapp/index_selected_type.html', context)
    else:
        return redirect('sign_in')


def details(request, id):
    if sign_in_valid(request):
        previous_lec_id = 0
        next_lec_id = 0
        lecture = Lecture.objects.get(id=id)
        comments = Comment.objects.filter(lecture_id=lecture.id)
        for comment in comments:
            comment.username = User.objects.get(id=comment.user_id).username
        partner_lectures = Lecture.objects.filter(unit_index=lecture.unit_index)
        for partner_lecture in partner_lectures:
            if (partner_lecture.lecture_index_number + 1) == lecture.lecture_index_number:
                previous_lec_id = partner_lecture.id
            if (partner_lecture.lecture_index_number - 1) == lecture.lecture_index_number:
                next_lec_id = partner_lecture.id
        context = {
            'user': request.session['username'],
            'lecture': lecture,
            'ytlink': lecture.videourl,
            'comments': comments,
            'unit_index': lecture.unit_index,
            'lecture_type_index': lecture.lecture_type_index,
            'prev_lec': previous_lec_id,
            'next_lec': next_lec_id,
        }

        return render(request, 'pleniapp/details.html', context)
    else:
        return redirect('sign_in')

def details_admin(request, id):
    if sign_in_valid_admin(request):
        lecture = Lecture.objects.get(id=id)
        comments = Comment.objects.filter(lecture_id=lecture.id)
        for comment in comments:
            comment.username = User.objects.get(id=comment.user_id).username
        context = {
            'user': request.session['username_admin'],
            'lecture': lecture,
            'ytlink': lecture.videourl,
            'comments': comments,
            'unit_index': lecture.unit_index,
            'lecture_type_index': lecture.lecture_type_index,
        }

        return render(request, 'pleniapp/details_admin.html', context)
    else:
        return redirect('sign_in_admin')

def create(request):
    if sign_in_valid_admin(request):
        context = {
            'user': request.session['username_admin'],
        }

        return render(request, 'pleniapp/create.html', context)
    else:
        return redirect('sign_in_admin')

def create_lecture(request):
    if request.method == 'POST':
        lec_title = request.POST['title']
        lec_description = request.POST['description']
        lec_unit = request.POST['unit']
        lec_type = request.POST['type']
        lec_videourl = request.POST['videourl']

        partner_lectures = Lecture.objects.filter(unit_index=lec_unit)
        latest_partner_lecture = partner_lectures.last()
        new_lec_index_num = latest_partner_lecture.lecture_index_number + 1

        Lecture.objects.create(
            title = lec_title,
            description = lec_description,
            unit_index = lec_unit,
            lecture_type_index = lec_type,
            videourl = lec_videourl,
            lecture_index_number = new_lec_index_num
        )
        return HttpResponse('')

def edit(request, id):
    if sign_in_valid_admin(request):
        lecture = Lecture.objects.get(id=id)
        context = {
            'user': request.session['username_admin'],
            'lecture': lecture
        }
        return render(request, 'pleniapp/edit.html', context)
    else:
        return redirect('sign_in_admin')


def user_submit_comment(request):
    if request.method == 'POST':
        comment = request.POST['comment']
        lecture_id = request.POST['lecture_id']
        user_id = User.objects.get(username=request.session['username'])

        comment_now = Comment.objects.create(
            body = comment,
            lecture_id = 5,
            user_id = 2
        )
        comment_now.username = User.objects.get(id=comment_now.user_id).username
        data = {
            'username': 'hey',
            'body': 'you'
        }
        return JsonResponse(data)
