from django.urls import path
from . import views

urlpatterns = [

    	path('', views.index),
        #path('hello/<str:username>', views.hello),
        path('login/', views.login, name='login'),
        path('signup/', views.signup, name='signup')

]