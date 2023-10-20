from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Sedes, UserProfile
from django.db import models

class Login(forms.Form):
    username = forms.CharField(label="Nombre de usuario", max_length=200)
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput)

class Create_Sede(ModelForm):
    class Meta:
        model = Sedes
        fields = ['nombre', 'ubicacion', 'codigo_postal']


class Create_Usuario(ModelForm):
    class Meta():
        model = UserProfile
        fields =['rol', 'nombre', 
                  'apellido_paterno', 'apellido_materno', 'fecha_nacimiento']
    
        '''
    def save(self, commit=True):
        user_profile = super().save(commit=False)
        user = User.objects.create_user(username=self.cleaned_data['username'], password=self.cleaned_data['password1'])
        user_profile.user = user

                user_profile.rol = self.cleaned_data['rol']
        user_profile.nombre = self.cleaned_data['nombre']
        user_profile.apellido_paterno = self.cleaned_data['apellido_paterno']
        user_profile.apellido_materno = self.cleaned_data['apellido_materno']
        user_profile.fecha_nacimiento = self.cleaned_data['fecha_nacimiento']
        

        if commit:
            user_profile.user.save()
            user_profile.save()

        return user_profile
        '''