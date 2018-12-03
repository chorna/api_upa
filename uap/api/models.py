from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Seccion(models.Model):
    codseccion = models.CharField(max_length=20)


class Persona(models.Model):
    nombre = models.CharField(max_length=200)
    correo = models.EmailField(blank=True, null=True)
    foto = models.ImageField(blank=True, null=True)
    usuario = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    seccion = models.ForeignKey(Seccion, null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        abstract = True


class Alumno(Persona):
    pass


class Nota(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    nota = models.FloatField()
    motivo = models.CharField(max_length=200, blank=True, null=True)
    evaluacion = models.CharField(max_length=200, blank=True, null=True)


class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    codecurso = models.CharField(max_length=20)
    cicloacademico = models.CharField(max_length=20)


class Profesor(Persona):
    pass
