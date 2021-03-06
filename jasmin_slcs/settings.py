"""
Settings helpers for the ``jasmin_slcs`` Django app.
"""

from django.conf import settings

from settings_object import SettingsObject, Setting


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
    #: The realm for authentication challenges
    AUTH_CHALLENGE_REALM = Setting()


app_settings = AppSettings('JASMIN_SLCS')
