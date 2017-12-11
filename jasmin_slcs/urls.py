"""
Root URL configuration for the jasmin-slcs project.
"""

from django.conf.urls import url

from onlineca.views import trustroots

from .views import certificate

app_name = 'jasmin_slcs'
urlpatterns = [
    url(r'^trustroots/$', trustroots, name = 'trustroots'),
    url(r'^certificate/$', certificate, name = 'certificate'),
]
