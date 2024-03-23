from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ROLES = [('guardian', 'Guardian'), 
             ('director', 'Director'),
             ('secretario', 'Secretario'),
             ('instructor', 'Instructor'),
             ('alumno', 'Alumno')
             ]
    rol = models.CharField(max_length=25, choices=ROLES, default='director')
    nombre = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, null=True)
    apellido_paterno = models.CharField(max_length=200)
    apellido_materno= models.CharField(max_length=200)
    fecha_nacimiento = models.DateField(default='2023-10-18')

    def get_full_name(self):
        full_name = (f'{self.nombre} {self.apellido_paterno}')
        return full_name

class Sedes(models.Model):
    nombre = models.CharField(max_length=200)
    ubicacion = models.CharField(max_length=200)
    codigo_postal  = models.IntegerField()
    director = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True)

class Dias_Semana(models.Model):
    dia = models.PositiveSmallIntegerField(choices=[
        (1, 'Lunes'),
        (2, 'Martes'), 
        (3, 'Miércoles'), 
        (4, 'Jueves'), 
        (5, 'Viernes'), 
        (6, 'Sábado'), 
        (7, 'Domingo')])
    
    def __str__(self):
        return self.get_dia_display()

class Grupos(models.Model):
    CURSOS = [('jiu jitsu', 'Jiu Jitsu'), 
              ('karete do','Karate Do'), 
              ('taido', 'Taido'), 
              ('taekwondo', 'Taekwondo'),
              ('capoeira', 'Capoeira'), 
              ('kickboxing', 'Kickboxing'),
              ('tai chi', 'Tai Chi')]

    grupo = models.CharField(max_length=6, default='000')
    curso = models.CharField(max_length=200, choices=CURSOS, default='Jiu Jitsu')
    dias_semana = models.ManyToManyField('Dias_Semana', through='GruposDias')
    hora_inicio = models.PositiveSmallIntegerField()
    duracion = models.PositiveSmallIntegerField()
    sede = models.ForeignKey(Sedes, on_delete=models.CASCADE)
    instructor = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True)

class GruposDias(models.Model):
    grupo = models.ForeignKey(Grupos, on_delete=models.CASCADE)
    dia_semana = models.ForeignKey(Dias_Semana, on_delete=models.CASCADE)

class Inscripciones(models.Model):
    alumno = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='inscripciones' ,null=True)
    grupo = models.ForeignKey(Grupos, on_delete=models.CASCADE)
    fecha_inscripcion = models.DateField()