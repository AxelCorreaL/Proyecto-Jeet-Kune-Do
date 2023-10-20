from django.urls import path
from . import views

urlpatterns = [

    	path('', views.index, name='home'),
        #path('hello/<str:username>', views.hello),
        path('login/', views.signin, name='login'),
        path('signup/', views.signup, name='signup'),
        path('profile/', views.profile, name='profile'),
        path('logout/', views.signout, name='logout'),
        path('sedes/', views.sedes, name='sedes'),
        path('sedes/<int:id_sede>', views.edit_sede, name='edit_sede'),
        path('sedes/<int:id_sede>/delete_sede', views.delete_sede, name='delete_sede'),
        path('usuarios/', views.usuarios, name='usuarios'),
        path('usuarios/<int:id_usuario>', views.edit_usuario, name='edit_usuario'),
        path('usuarios/<int:id_usuario>/delete_usuario', views.delete_usuario, name='delete_usuario')
]