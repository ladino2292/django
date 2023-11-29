from django.shortcuts import render

from django.http import HttpResponse
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
    return render(request,'estudiantes/index.html')