from django.db import models

# Create your models here.

class Person:
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=20)
    correo = models.EmailField()

class Professors(models.Model):

    nombre = models.CharField(max_length=30, default='0000', editable=False)
    apellido = models.CharField(max_length=30, default='0000', editable=False)
    correo = models.EmailField(default='0000', editable=False)

    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.correo}"

class Students(models.Model, Person):
    
    nombre = models.CharField(max_length=30, default='0000', editable=False)
    apellido = models.CharField(max_length=30, default='0000', editable=False)
    correo = models.EmailField(default='0000', editable=False)

    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.correo}"

class Entregables(models.Model, Person):
    pass

class Cursos(models.Model, Person):
    pass

class Curso(models.Model):
    name = models.CharField(max_length=20)
    camada = models.IntegerField()

    def __str__(self):
        return f"{self.name} - {self.camada}"
