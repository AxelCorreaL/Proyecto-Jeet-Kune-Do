from functools import wraps
from django.shortcuts import redirect

def role_required(allowed_roles=[]):
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):
            user_profile = request.user.userprofile
            if user_profile.rol not in allowed_roles:
                # Si el usuario no tiene el rol permitido, redirigir a algún lugar o mostrar un mensaje de error.
                return redirect('profile')
            return view_func(request, *args, **kwargs)
        return wrapper
    return decorator
