from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.index, name='indexroot'),
    path('index/', views.index, name='index'),
    path('details/<int:id>/', views.details, name='details'),
]
