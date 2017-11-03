"""
Django WSGI config for the jasmin-slcs project.

It exposes the WSGI callable as a module-level variable named ``application``.
"""

import os

from django.core.wsgi import get_wsgi_application


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "jasmin_slcs_site.settings")
application = get_wsgi_application()
