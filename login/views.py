from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import Login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    return render(request, "index.html")

'''def hello(request, username):
    print(username)
    return HttpResponse('<h1>Hello %s</h1>' % username)
'''
    
def login(request):
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
            return render(request, 'login.html', {
            'form': AuthenticationForm
        })
    
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
                return HttpResponse('user created')
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
        