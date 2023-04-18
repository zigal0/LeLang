"""
ASGI config for lelang project.
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lelang.settings')

application = get_asgi_application()
