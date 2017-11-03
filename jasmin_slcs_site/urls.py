"""
Root URL configuration for the jasmin-slcs project.
"""

from django.conf import settings
from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt

from oauth2_provider.decorators import protected_resource

from onlineca.views import trustroots, certificate


CERTIFICATE_SCOPE = getattr(settings, 'JASMIN_SLCS', {})['CERTIFICATE_SCOPE']

urlpatterns = [
    url(r'^trustroots/$', trustroots, name = 'trustroots'),
    # Protect the certificate endpoint with OAuth
    url(r'^certificate/$',
        protected_resource(scopes = [CERTIFICATE_SCOPE])(csrf_exempt(certificate)),
        name = 'certificate'),
]
