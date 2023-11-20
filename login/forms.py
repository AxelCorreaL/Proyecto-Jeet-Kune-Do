from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Sedes, UserProfile, Grupos, Dias_Semana
from django.db import models

class InstructorChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.get_full_name()

class SedeChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.nombre

class UserCreateForm(UserCreationForm):
    username = forms.CharField(label="Nombre de usuario", max_length=200)
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirma Contraseña", widget=forms.PasswordInput)

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        if commit:
            user.save()
        return user

    class Meta:
        model = User
        fields = ("username", "password1", "password2")
        help_texts = {'username':None, 'password1':None, 'password2':None}

class Login(forms.Form):
    username = forms.CharField(label="Nombre de usuario", max_length=200)
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput)


class Create_Sede(ModelForm):
    directores = [(director.id, director.get_full_name) for director in UserProfile.objects.filter(rol='director')]
    id_Director = forms.ChoiceField(label="Director de Sede", choices= directores)

    class Meta:
        model = Sedes
        fields = ['nombre', 'ubicacion', 'codigo_postal', 'id_Director']


class Create_Usuario(ModelForm):
    class Meta():
        model = UserProfile
        fields =['rol', 'nombre', 
                  'apellido_paterno', 'apellido_materno', 'fecha_nacimiento']
    
class Create_Grupo(ModelForm):
    #Instructores = [(instructor.id, instructor.get_full_name) for instructor in UserProfile.objects.filter(rol='instructor')]
    #id_Instructor = forms.ChoiceField(label="Instructor de Curso", choices= Instructores)
    
    #Sedes = [(sede, sede.nombre) for sede in Sedes.objects.all()]
    #id_Sede = forms.ChoiceField(label="Sede ", choices= Sedes)

    instructor = InstructorChoiceField(
        label='Intructor del curso',
        queryset=UserProfile.objects.filter(rol='instructor'),
        empty_label=None
    )

    sede = SedeChoiceField(
        label='Sede',
        queryset= Sedes.objects.all(),
        empty_label=None
    )

    dias_semana = forms.ModelMultipleChoiceField(
        queryset=Dias_Semana.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = Grupos
        fields = ['grupo', 'curso', 'hora_inicio', 'duracion', 'sede', 'instructor', 'dias_semana']

class DiasSemanaForm(ModelForm):
    class Meta:
        model = Dias_Semana
        fields = ['dia']
        widgets = {
            'dia': forms.CheckboxSelectMultiple,
        }