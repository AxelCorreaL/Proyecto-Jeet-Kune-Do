from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from .forms import Create_Sede, Create_Usuario
from .models import Sedes, UserProfile

# Create your views here.
def index(request):
    return render(request, "index.html")

'''def hello(request, username):
    print(username)
    return HttpResponse('<h1>Hello %s</h1>' % username)
'''

def signin(request):
    if request.method == 'GET': 
        return render(request, 'login.html', {
            'form': AuthenticationForm
        })
    
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        #print(request.POST)
        if user is None:
            return render(request, 'login.html', {
            'form': AuthenticationForm,
            'error': 'El usuario o la contraseña es incorrecta'
        })
        else:
            login(request, user)
            return redirect('profile')
            
def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {
        'form': UserCreationForm
        })
    else:
        if(request.POST['password1'] == request.POST['password2']):
            try:
                # register user
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('profile')
            except:
                return render(request, 'signup.html', {
                'form': UserCreationForm,
                'error': 'Username already exists'
                })
                
        else:
            return render(request, 'signup.html', {
                'form': UserCreationForm,
                'error': 'Passwords do not match'
                })

def signout(request):
    logout(request)
    return redirect('home')

def profile(request):
    return render(request, 'profile.html')

def sedes(request):
    sedes = Sedes.objects.all()
    # sede = Sedes(instance=sede)
    if request.method == 'GET':
        return render(request, 'sedes.html', {
            'form': Create_Sede,
            'sedes' : sedes
        })
    else:
        form = Create_Sede(request.POST)
        # new_sede = form.save(commit=False)
#        form.id_Administrador = request.user
        form.save()
        return render(request, 'sedes.html', {
            'form': Create_Sede,
            'sedes' : sedes
        })

def edit_sede(request, id_sede):
    if request.method == 'GET':
        sede = get_object_or_404(Sedes, pk=id_sede)
        form = Create_Sede(instance=sede)
        return render(request, 'edit_sede.html', {
            'sede': sede,
            'form' : form
        })
    else:
        try:
            sede = get_object_or_404(Sedes, pk=id_sede)
            form = Create_Sede(request.POST, instance= sede)
            form.save()
            return render(request, 'edit_sede.html', {
            'sede': sede,
            'form' : form,
            'message': 'Datos actualizados'
        })
        except ValueError:
            return render(request, 'edit_sede.html', {
            'sede': sede,
            'form' : form,
            'error': 'Problema al actualizar la sede'
        })

def delete_sede(request, id_sede):
    sede = get_object_or_404(Sedes, pk=id_sede)
    if request.method == 'POST':
        # Código para eliminar la sede
        sede.delete()
        return redirect('sedes')

def usuarios(request):
    usuarios = UserProfile.objects.all()
    directores = UserProfile.objects.filter(rol='director')
    secretarios = UserProfile.objects.filter(rol='secretario')
    if request.method == 'GET':
        return render(request, 'usuarios.html', {
                'user_form': UserCreationForm,
                'profile_form' : Create_Usuario,
                'directores' : directores,
                'secretarios' : secretarios
            })
    
    else:
        user_form = UserCreationForm(request.POST)
        profile_form = Create_Usuario(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            return render(request, 'usuarios.html', {
                'user_form': UserCreationForm,
                'profile_form': Create_Usuario,
                'directores' : directores,
                'secretarios' : secretarios,
                'error': 'Usuario creado exitosamente'
            })
        else:
            return render(request, 'usuarios.html', {
            'user_form': user_form,
            'profile_form': profile_form,
            'directores' : directores,
            'secretarios' : secretarios
    })  

def edit_usuario(request, id_usuario):
    if request.method == 'GET':
        usuario = get_object_or_404(UserProfile, pk=id_usuario)
        form = Create_Usuario(instance=usuario)
        return render(request, 'edit_usuario.html', {
            'usuario': usuario,
            'form' : form
        })
    else:
        try:
            usuario = get_object_or_404(UserProfile, pk=id_usuario)
            form = Create_Usuario(request.POST, instance=usuario)
            form.save()
            return render(request, 'edit_usuario.html', {
            'usuario': usuario,
            'form' : form,
            'message': 'Datos actualizados'
        })
        except ValueError:
            return render(request, 'edit_usuario.html', {
            'usuario': usuario,
            'form' : form,
            'error': 'Problema al actualizar el usuario'
        })

def delete_usuario(request, id_usuario):
    usuario = get_object_or_404(UserProfile, pk=id_usuario)
    if request.method == 'POST':
        # Código para eliminar la sede
        usuario.delete()
        return redirect('usuarios')