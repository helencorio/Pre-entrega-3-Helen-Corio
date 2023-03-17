from django.db import models

# Create your models here.

class Person:
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=20)
    correo = models.EmailField()


#class Thing:
    #nombre = models.CharField(max_length=30)
    #camada = models.IntegerField()

class Professors(models.Model, Person):
    pass

class Students(models.Model, Person):
    pass

class Entregables(models.Model, Person):
    pass

class Cursos(models.Model, Person):
    pass

class Curso(models.Model):
    name = models.CharField(max_length=20)
    camada = models.IntegerField()

    def __str__(self):
        return f"{self.id} - {self.name} - {self.camada}"
