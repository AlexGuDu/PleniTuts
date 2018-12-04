from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.index, name='indexroot'),
    path('index/', views.index, name='index'),
    path('details/<int:id>/', views.details, name='details'),
    path('lectureblock/<int:id>/', views.index_selected_unit, name='index_selected_unit'),
    path('lecturetype/<int:id>/', views.index_selected_type, name='index_selected_type'),
]
