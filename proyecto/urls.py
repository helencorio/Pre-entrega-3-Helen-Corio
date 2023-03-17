from django.urls import path
from proyecto.views import index, profesores, entregables, estudiantes, cursos


urlpatterns = [
    path('', index, name= "index"),
    path('profesores/', profesores, name= "profesores"),
    path('entregables/', entregables, name= "entregables"),
    path('estudiantes/', estudiantes, name= "estudiantes"),
    path('cursos/', cursos, name= "cursos"),
]