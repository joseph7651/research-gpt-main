"""
ASGI config for research_gpt project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'research_gpt.settings')

application = get_asgi_application()

# touched on 2025-08-14T20:06:48.960783Z
# touched on 2025-08-14T20:06:54.017423Z
# touched on 2025-08-14T20:07:00.597203Z