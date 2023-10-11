from django import forms

class Login(forms.Form):
    username = forms.CharField(label="Nombre de usuario", max_length=200)
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput)