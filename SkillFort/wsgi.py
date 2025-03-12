"""
WSGI config for SkillFort project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application
from asgiref.wsgi import WsgiToAsgi  # Use asgiref for WSGI to ASGI conversion

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SkillFort.settings")

application = get_wsgi_application()

# Convert WSGI to ASGI for Vercel
app = WsgiToAsgi(application)
