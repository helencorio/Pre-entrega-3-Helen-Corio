from django.urls import path
from proyecto.views import guardar_profesores, entregables, guardar_estudiantes, guarda_curso, buscar_camada


urlpatterns = [
    path('', buscar_camada, name= "buscar_camada"),
    path('profesores/', guardar_profesores, name= "profesores"),
    path('entregables/', entregables, name= "entregables"),
    path('estudiantes/', guardar_estudiantes, name= "estudiantes"),
    path('cursos/', guarda_curso, name= "cursos"),

]