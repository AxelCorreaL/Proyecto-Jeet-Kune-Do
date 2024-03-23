from django.contrib import admin
from .models import UserProfile, Sedes, Dias_Semana

# Register your models here.
admin.site.register(Sedes)
admin.site.register(UserProfile)
admin.site.register(Dias_Semana)