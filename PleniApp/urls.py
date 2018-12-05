from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.index, name='indexroot'),
    path('sign_in/', views.sign_in, name="sign_in"),
    path('register_user/', views.register_user, name="register_user"),
    path('signin_user/', views.signin_user, name="signin_user"),
    path('signout_user/', views.signout_user, name="signout_user"),
    path('index/', views.index, name='index'),
    path('details/<int:id>/', views.details, name='details'),
    path('lectureblock/<int:id>/', views.index_selected_unit, name='index_selected_unit'),
    path('lecturetype/<int:id>/', views.index_selected_type, name='index_selected_type'),
]
