# Generated by Django 4.2.5 on 2023-10-05 01:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alumnos',
            name='id_Alumno',
        ),
        migrations.RemoveField(
            model_name='directores',
            name='id_Director',
        ),
        migrations.RemoveField(
            model_name='grupos',
            name='id_Grupo',
        ),
        migrations.RemoveField(
            model_name='guardian',
            name='id_Guardian',
        ),
        migrations.RemoveField(
            model_name='inscripciones',
            name='id_Inscripcion',
        ),
        migrations.RemoveField(
            model_name='instructores',
            name='id_Instructor',
        ),
        migrations.RemoveField(
            model_name='secretarios',
            name='id_Secretario',
        ),
        migrations.RemoveField(
            model_name='sedes',
            name='id_Sede',
        ),
    ]
