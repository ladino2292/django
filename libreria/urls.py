from django.urls import path
from . import views

urlpatterns = [

    path('',views.inicio,name ='inicio'),
    path('nosotros',views.nosotros, name='nosotros'),
    path('estudiantes',views.estudiantes, name='estudiantes'),
    path('estudiantes/crear',views.crear, name='crear'),
    path('estudiantes/editar',views.editar, name='editar'),

    path('salas',views.salas, name='salas'),
]