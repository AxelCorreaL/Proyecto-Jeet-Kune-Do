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
        path('usuarios/<int:id_usuario>/delete_usuario', views.delete_usuario, name='delete_usuario'),
        path('grupos/', views.grupos, name='grupos'),
        path('grupos/<int:id_grupo>', views.edit_grupo, name='edit_grupo'),
        path('grupos/<int:id_grupo>/delete_grupo', views.delete_grupo, name='delete_grupo'),
        path('list_alumnos/<int:grupo_id>', views.list_alumnos, name='list_alumnos'),
        path('add_alumno/<int:grupo_id>/<int:alumno_id>', views.add_alumno, name='add_alumno'),
        path('remove_alumno/<int:grupo_id>/<int:alumno_id>', views.remove_alumno, name='remove_alumno')


]