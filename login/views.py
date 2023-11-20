from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from .forms import Create_Sede, Create_Usuario, UserCreateForm, Create_Grupo
from .models import Sedes, UserProfile, Grupos, Dias_Semana

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
                'error': 'El nombre de usuario ya existe'
                })
                
        else:
            return render(request, 'signup.html', {
                'form': UserCreationForm,
                'error': 'Las contraseñas no coinciden'
                })

def signout(request):
    logout(request)
    return redirect('home')

def profile(request):
    #pk = request.user.pk
    #nombre = get_object_or_404(UserProfile, pk=pk).nombre
    #return render(request, 'profile.html', {'nombre': nombre})
    return render(request, 'profile.html')

def sedes(request):
    sedes = Sedes.objects.all()
    if request.method == 'GET':
        return render(request, 'sedes.html', {
            'form': Create_Sede,
            'sedes' : sedes
        })
    else:
        form = Create_Sede(request.POST)
        if form.is_valid():
            director_id = form.cleaned_data['id_Director']
            director = UserProfile.objects.get(id=director_id)
        
            sede = form.save(commit=False)
            sede.director = director
            sede.save()
        return render(request, 'sedes.html', {
            'form': Create_Sede,
            'sedes' : sedes,
            'message' : 'Sede creada satisfactoriamente'
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
    # usuarios = UserProfile.objects.all()
    directores = UserProfile.objects.filter(rol='director')
    secretarios = UserProfile.objects.filter(rol='secretario')
    if request.method == 'GET':
        return render(request, 'usuarios.html', {
                'user_form': UserCreateForm,
                'profile_form' : Create_Usuario,
                'directores' : directores,
                'secretarios' : secretarios
            })
    
    else:
        user_form = UserCreateForm(request.POST)
        profile_form = Create_Usuario(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            return render(request, 'usuarios.html', {
                'user_form': UserCreateForm,
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
    

def grupos(request):
    grupos = Grupos.objects.all()
    
    if request.method == 'GET':
        return render(request, 'grupos.html', 
                      {
                          'grupoForm': Create_Grupo,
                          'grupos': grupos
                      })
    else:
        grupoForm = Create_Grupo(request.POST)
        
        if grupoForm.is_valid():
            # Código para guardar en la base de datos
            dia = grupoForm.cleaned_data['dia']
            sede_id = grupoForm.cleaned_data['sede'].id
            sede = Sedes.objects.get(pk=sede_id)

            nuevo_grupo = grupoForm.save(commit=False)
            nuevo_grupo.sede = sede

            #nuevo_dia = Dias_Semana.objects.create(dia=dia)
            #nuevo_grupo.dias_semana.add(nuevo_dia)

            nuevo_grupo.save()


            grupos = Grupos.objects.all()
            return render(request, 'grupos.html', {
            'grupoForm': Create_Grupo,
            'grupos': grupos,
            'message' : 'Grupo agregado exitosamente'
        })
        else:
            return render(request, 'grupos.html', {
            'grupoForm': Create_Grupo,
            'grupos': grupos,
            'error': 'No se pudo agregar'
        })

def edit_grupo(request, id_grupo):
    if request.method == 'GET':
        grupo = get_object_or_404(Grupos, pk=id_grupo)
        form = Create_Grupo(instance=grupo)
        return render(request, 'edit_grupo.html', {
            'grupo': grupo,
            'form' : form
        })
    else:
        try:
            grupo = get_object_or_404(Grupos, pk=id_grupo)
            form = Create_Grupo(request.POST, instance= grupo)
            form.save()
            return render(request, 'edit_grupo.html', {
            'grupo': grupo,
            'form' : form,
            'message': 'Datos actualizados'
        })
        except ValueError:
            return render(request, 'edit_grupo.html', {
            'grupo': grupo,
            'form' : form,
            'error': 'Problema al actualizar el grupo'
        })

def delete_grupo(request, id_grupo):
    grupo = get_object_or_404(Grupos, pk=id_grupo)
    if request.method == 'POST':
        # Código para eliminar 
        grupo.delete()
        return redirect('grupos')