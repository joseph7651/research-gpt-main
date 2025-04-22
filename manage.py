#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'research_gpt.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

# touched on 2025-08-14T20:06:56.237936Z
# touched on 2025-08-14T20:07:05.354142Z
# touched on 2025-08-14T20:07:09.887785Z
# touched on 2025-08-14T20:07:11.969318Z
# touched on 2025-08-14T20:07:14.253879Z
# touched on 2025-08-14T20:07:26.243033Z
# touched on 2025-08-14T20:07:35.229961Z
# touched on 2025-08-14T20:07:48.577934Z