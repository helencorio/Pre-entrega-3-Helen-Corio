from django.urls import path
from proyecto.views import index, profesores, entregables, estudiantes, cursos, busca_curso, save_form


urlpatterns = [
    path('', index, name= "index"),
    path('profesores/', profesores, name= "profesores"),
    path('entregables/', entregables, name= "entregables"),
    path('estudiantes/', estudiantes, name= "estudiantes"),
    path('cursos/', cursos, name= "cursos"),
    path('buscar_curso/', busca_curso, name= "buscar_curso"),
    path('guardar_form/', save_form, name = "guarda_formulario")
]