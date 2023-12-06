from django.shortcuts import render

from django.http import HttpResponse
from .models import Estudiante
# Create your views here.

def inicio(request):
    return render(request,'paginas/inicio.html')
def nosotros(request):
    return render(request, 'paginas/nosotros.html')    

def salas(request):
    return render(request,'salas/index.html')

def crear(request):
    return render(request,'estudiantes/crear.html')
def editar(request):
    return render(request,'estudiantes/editar.html')
def estudiantes(request):
    estudiantes =Estudiante.objects.all()
    print(estudiantes)
    return render(request,'estudiantes/index.html',{'estudiantes': estudiantes})