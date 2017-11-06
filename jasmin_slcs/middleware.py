"""
Django middlewares for the ``jasmin_slcs`` app.
"""

import base64
import binascii
from urllib.parse import unquote_plus

from django.contrib.auth import authenticate
from django.utils.cache import patch_vary_headers
from django.http import HttpResponse
from django.contrib.auth.models import AnonymousUser


class BasicAuthMiddleware:
    """
    Middleware for Basic Auth authentication.

    Because it only attempts to authenticate the user with Basic Auth if
    ``request.user`` is not valid, this middleware is able to play nicely with
    other authentication middlewares.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # If the request contains a basic auth credential and the user has not
        # already been authenticated, try to authenticate
        if not hasattr(request, "user") or request.user.is_anonymous:
            auth_header = request.META.get('HTTP_AUTHORIZATION', '')
            if auth_header.startswith('Basic'):
                try:
                    credentials = auth_header.split(' ', 1)[1].strip()
                    decoded = base64.b64decode(credentials).decode('utf-8')
                    username, password = decoded.split(':', 1)
                except (IndexError, TypeError, ValueError, binascii.Error) as e:
                    # Malformed credentials should be reported as a bad request
                    return HttpResponse(
                        status = 400,
                        content = 'Malformed Basic Auth credentials.',
                        content_type = 'text/plain'
                    )
                user = authenticate(
                    request = request,
                    username = unquote_plus(username),
                    password = unquote_plus(password)
                )
                if user:
                    request.user = request._cached_user = user
        # Get the response
        response = self.get_response(request)
        # Patch the vary headers for caching
        patch_vary_headers(response, ("Authorization", ))
        return response


class AnonymousUserMiddleware:
    """
    Middleware for setting the anonymous user in the absence of the standard
    authentication middleware.

    If this middleware comes after all authentication middlewares, it allows
    many authentication methods to be chained, each setting request.user if
    appropriate.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not hasattr(request, 'user'):
            request.user = AnonymousUser()
        return self.get_response(request)
