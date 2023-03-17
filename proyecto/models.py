from django.db import models

# Create your models here.

class Person:
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    correo = models.EmailField()

class Professors(models.Model, Person):
    pass

class Students(models.Model, Person):
    pass

class Entregables(models.Model, Person):
    pass

class Cursos(models.Model, Person):
    pass

