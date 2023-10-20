from django import forms
from django.db import models
from django.contrib.auth.models import Group, User

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ROLES = [('guardian', 'Guardian'), 
             ('director', 'Director'),
             ('secretario', 'Secretario'),
             ('instructor', 'Instructor'),
             ('alumno', 'alumno')
             ]
    rol = models.CharField(max_length=25, choices=ROLES, default='director')
    nombre = models.CharField(max_length=200)
    apellido_paterno = models.CharField(max_length=200)
    apellido_materno= models.CharField(max_length=200)
    fecha_nacimiento = models.DateField(default='2023-10-18')

class Sedes(models.Model):
    nombre = models.CharField(max_length=200)
    ubicacion = models.CharField(max_length=200)
    codigo_postal  = models.IntegerField()
    #id_Administrador = models.ForeignKey(Administradores, on_delete= models.CASCADE)

class Instructores(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    nombre = models.CharField(max_length=200)
    apellido_paterno = models.CharField(max_length=200)
    apellido_materno= models.CharField(max_length=200)
    fecha_nacimiento = models.DateField()

class Grupos(models.Model):
    curso = models.CharField(max_length=200)
    dias_semana = models.CharField(max_length=200)
    hora_inicio = models.DateTimeField()
    duracion = models.DateTimeField()
    id_Sede = models.ForeignKey(Sedes, on_delete=models.CASCADE)
    id_Instructor = models.ForeignKey(Instructores, on_delete=models.CASCADE)

class Alumnos(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    nombre = models.CharField(max_length=200)
    apellido_paterno = models.CharField(max_length=200)
    apellido_materno= models.CharField(max_length=200)
    fecha_nacimiento = models.DateField()

class Inscripciones(models.Model):
    id_Alumno = models.ForeignKey(Alumnos, on_delete=models.CASCADE)
    id_Grupo = models.ForeignKey(Grupos, on_delete=models.CASCADE)
    fecha_inscripcion = models.DateField()