from django.shortcuts import render
from django.http import HttpResponse
from proyecto.models import Curso, Professor , Entregable , Student
from proyecto.forms import BuscarCursosForm

# Create your views here.

def guardar_profesores(request):
    
    if request.method == "POST":
        print("\n\n\n")
        nombre = request.POST["nombre"]
        apellido = request.POST["apellido"]
        correo = request.POST["correo"]

        profe = Professor(nombre= nombre, apellido= apellido, correo = correo)
        profe.save()


    return render(request, "proyecto/profesores.html")

def guardar_entregables(request):

    if request.method == "POST":
        print("\n\n\n")
        nombre = request.POST["nombre"]
        num = request.POST["num"]
        entrega = Entregable(nombre=nombre, num=num )
        entrega.save()

    return render(request, 'proyecto/entregables.html')

def guardar_estudiantes(request):
        
    if request.method == "POST":
        print("\n\n\n")
        nombre = request.POST["nombre"]
        apellido = request.POST["apellido"]
        correo = request.POST["correo"]

        student = Student(nombre= nombre, apellido= apellido, correo = correo)
        student.save()

    return render(request, "proyecto/estudiantes.html")

def guarda_curso(request):

    if request.method == "POST":
        print("\n\n\n")
        name = request.POST["curso"]
        camada = request.POST["camada"]
        curso = Curso(name=name, camada=camada )
        curso.save()


    return render(request, "proyecto/cursos.html")



def buscar_camada(request):

    if request.method == "POST":

            camadas = Curso.objects.filter(camada=int(request.POST["camada"]))

            return render(request, "proyecto/buscar_camada.html", {"data": [camadas]})
    else:
        miFormulario = BuscarCursosForm()

    return render(request, "proyecto/buscar_camada.html", {"miFormulario": miFormulario})
