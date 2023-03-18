from django.shortcuts import render
from django.http import HttpResponse
from proyecto.models import Curso
from proyecto.forms import BuscarCursosForm

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

def busca_curso(request):

    if request.method == "POST":
        print("\n\n\n")
        name = request.POST["curso"]
        camada = request.POST["camada"]
        curso = Curso(name=name, camada=camada )
        curso.save()


    return render(request, "proyecto/buscar_cursos.html")


def save_form(request):
    if request.method == "POST":
        miFormulario = BuscarCursosForm(request.POST) # Aqui me llega la informacion del html
        print(miFormulario)

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            print(f"\n{informacion}\n")
            curso = Curso(name=informacion["curso"], camada=informacion["camada"])
            curso.save()
            return render(request, "proyecto/index.html")
    else:
        miFormulario = BuscarCursosForm()

    return render(request, "proyecto/save_form.html", {"miFormulario": miFormulario})



