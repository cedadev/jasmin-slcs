"""
Django authentication backends for the ``jasmin_slcs`` app.
"""

from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

import requests

from .settings import app_settings


UserModel = get_user_model()


class OAuthPasswordGrantBackend(ModelBackend):
    """
    Django authentication backend that uses the OAuth 2.0 Resource Owner
    Password Credentials grant type to authenticate a user.
    """
    def authenticate(self, request, username = None, password = None, **kwargs):
        # If either username or password are not given, defer
        if not (username and password):
            return None
        # If we have a username and password, ask the authz server if they are valid
        response = requests.post(
            app_settings.AUTH_SERVER_TOKEN_URL,
            data = {
                'grant_type': 'password',
                'client_id': app_settings.PASSWORD_GRANT_CLIENT_ID,
                'client_secret': app_settings.PASSWORD_GRANT_CLIENT_SECRET,
                'username': username,
                'password': password,
            }
        )
        if response.status_code == 200:
            # Username/password are valid - create and return a user record
            return UserModel.objects.get_or_create(username = username)[0]
        elif response.status_code in [400, 401, 403]:
            # Authentication failed. Let the next backend try.
            return None
        else:
            # For any other response code, raise the error
            response.raise_for_status()
