#!/usr/bin/env python3

import os, re
from setuptools import setup, find_packages

import versioneer


here = os.path.abspath(os.path.dirname(__file__))


with open(os.path.join(here, 'README.md')) as f:
    README = f.read()

if __name__ == "__main__":
    setup(
        name = 'jasmin-slcs',
        version = versioneer.get_version(),
        cmdclass = versioneer.get_cmdclass(),
        description = 'Service for issuing short-lived JASMIN user certificates.',
        long_description = README,
        classifiers = [
            "Programming Language :: Python",
            "Framework :: Django",
            "Topic :: Internet :: WWW/HTTP",
            "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
        author = 'Matt Pryor',
        author_email = 'matt.pryor@stfc.ac.uk',
        url = 'https://github.com/cedadev/jasmin-slcs',
        keywords = 'django jasmin slcs certificate',
        packages = find_packages(),
        include_package_data = True,
        zip_safe = False,
        install_requires = [
            'django',
            'django-oauth-toolkit',
            'dot-dynamic-scopes',
            'django-onlineca',
            'psycopg2',
            'requests',
            'jasmin-django-utils',
        ],
    )
