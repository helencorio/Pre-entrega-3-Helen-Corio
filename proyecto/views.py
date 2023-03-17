from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'proyecto/index.html')

def profesores(request):
    return render(request, 'proyecto/profesores.html')

def entregables(request):
    return render(request, 'proyecto/entregables.html')

def cursos(request):
    return render(request, 'proyecto/cursos.html')

def estudiantes(request):
    return render(request, 'proyecto/estudiantes.html')








