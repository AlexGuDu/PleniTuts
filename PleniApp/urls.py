from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.index, name='indexroot'),
    path('index/', views.index, name='index'),
    path('index_admin/', views.index_admin, name='index_admin'),
    path('sign_in_admin/', views.sign_in_admin, name="sign_in_admin"),
    path('register_user_admin/', views.register_user_admin, name="register_user_admin"),
    path('signin_user_admin/', views.signin_user_admin, name="signin_user_admin"),
    path('signout_user_admin/', views.signout_user_admin, name="signout_user_admin"),
    path('sign_in/', views.sign_in, name="sign_in"),
    path('register_user/', views.register_user, name="register_user"),
    path('signin_user/', views.signin_user, name="signin_user"),
    path('signout_user/', views.signout_user, name="signout_user"),
    path('details/<int:id>/', views.details, name='details'),
    path('details_admin/<int:id>/', views.details_admin, name='details_admin'),
    path('lectureblock/<int:id>/', views.index_selected_unit, name='index_selected_unit'),
    path('lecturetype/<int:id>/', views.index_selected_type, name='index_selected_type'),
]
