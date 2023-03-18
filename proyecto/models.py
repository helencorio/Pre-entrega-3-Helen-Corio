from django.db import models

# Create your models here.

class Person:
    nombre = models.CharField(max_length=30, default='0000', editable=False)
    apellido = models.CharField(max_length=30, default='0000', editable=False)
    correo = models.EmailField(default='0000', editable=False)

class Professor(models.Model, Person):

    nombre = models.CharField(max_length=30, default='0000', editable=False)
    apellido = models.CharField(max_length=30, default='0000', editable=False)
    correo = models.EmailField(default='0000', editable=False)

    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.correo}"

class Student(models.Model, Person):
    
    nombre = models.CharField(max_length=30, default='0000', editable=False)
    apellido = models.CharField(max_length=30, default='0000', editable=False)
    correo = models.EmailField(default='0000', editable=False)

    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.correo}"

class Entregable(models.Model, Person):
    nombre = models.CharField(max_length=20, default='0000', editable=False)
    num = models.IntegerField(default='0000', editable=False)

    def __str__(self):
        return f"{self.nombre} - {self.num}"


class Curso(models.Model):
    name = models.CharField(max_length=20)
    camada = models.IntegerField()

    def __str__(self):
        return f"{self.name} - {self.camada}"
