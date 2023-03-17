from django.urls import path
from proyecto.views import index, profesores, entregables, estudiantes, cursos


urlpatterns = [
    path('', index),
    path('profesores/', profesores),
    path('entregables/', entregables),
    path('estudiantes/', estudiantes),
    path('cursos/', cursos),
]