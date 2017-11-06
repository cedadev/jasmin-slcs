"""
Settings helpers for the ``jasmin_slcs`` Django app.
"""

from django.conf import settings

from jasmin_django_utils.appsettings import SettingsObject, Setting


class AppSettings(SettingsObject):
    """
    Settings object for the ``jasmin_slcs`` app.
    """
    #: The scope to use for OAuth-authenticated requests for a certificate
    CERTIFICATE_SCOPE = Setting()

    #: URL of the authorisation server token endpoint
    AUTH_SERVER_TOKEN_URL = Setting()
    #: Client ID to use for the resource owner password grant flow
    PASSWORD_GRANT_CLIENT_ID = Setting()
    #: Client secret to use for the resource owner password grant flow
    PASSWORD_GRANT_CLIENT_SECRET = Setting()


app_settings = AppSettings('JASMIN_SLCS', getattr(settings, 'JASMIN_SLCS', {}))
