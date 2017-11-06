"""
Root URL configuration for the jasmin-slcs project.
"""

from django.conf.urls import url, include


urlpatterns = [
    url(r'^', include('jasmin_slcs.urls', namespace = 'slcs')),
]
