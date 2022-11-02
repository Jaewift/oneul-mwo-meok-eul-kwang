"""
WSGI config for oneul_mwo_meok_eul_kwang project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'oneul_mwo_meok_eul_kwang.settings')

application = get_wsgi_application()
