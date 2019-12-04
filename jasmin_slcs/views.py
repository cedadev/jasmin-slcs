"""
Django views for the JASMIN SLCS project.
"""

import functools

from django.http import HttpResponse
from django.views.decorators.http import require_POST
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


@require_POST
@protected_resource_if_oauth(scopes = [app_settings.CERTIFICATE_SCOPE])
@csrf_exempt
def certificate(request):
    """
    Wrapper for the onlineca certificate view that sends back a 401 if no authentication
    was provided.
    """
    if not request.user.is_authenticated:
        # If there is no authenticated user, send back a challenge indicating the
        # authentication methods we accept
        response = HttpResponse(
            status = 401,
            content = 'Authentication required.',
            content_type = 'text/plain'
        )
        response['WWW-Authenticate'] = 'Basic realm="{realm}", Bearer realm="{realm}"'.format(
            realm = app_settings.AUTH_CHALLENGE_REALM
        )
        return response
    return onlineca_certificate(request)
