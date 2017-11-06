"""
Django views for the JASMIN SLCS project.
"""

import functools

from django.views.decorators.csrf import csrf_exempt

from oauth2_provider.decorators import protected_resource

from onlineca.views import certificate as onlineca_certificate

from .settings import app_settings


def protected_resource_if_oauth(scopes = None):
    """
    Applies the OAuth scopes to the wrapped view only if the authorisation
    header contains a bearer token.
    """
    def decorator(view):
        @functools.wraps(view)
        def wrapper(request, *args, **kwargs):
            if request.META.get('HTTP_AUTHORIZATION', '').startswith('Bearer'):
                return protected_resource(scopes = scopes)(view)(request, *args, **kwargs)
            else:
                return view(request, *args, **kwargs)
        return wrapper
    return decorator


_with_scope = protected_resource_if_oauth(scopes = [app_settings.CERTIFICATE_SCOPE])
certificate = _with_scope(csrf_exempt(onlineca_certificate))
