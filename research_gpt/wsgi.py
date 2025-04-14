"""
WSGI config for research_gpt project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'research_gpt.settings')

application = get_wsgi_application()

# touched on 2025-08-14T20:06:46.595556Z
# touched on 2025-08-14T20:06:56.237272Z