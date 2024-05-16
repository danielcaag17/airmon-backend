import os
import django


def setup_django():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "airmon.settings")
    django.setup()
