import socket

from django_core.settings.base import *

DEBUG = True

INSTALLED_APPS += [
    "debug_toolbar",
]

MIDDLEWARE += [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
INTERNAL_IPS = [ip[: ip.rfind(".")] + ".1" for ip in ips] + ["127.0.0.1", "10.0.2.2"]


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ROOT_DIR / "db.sqlite3",
    }
}

# Email
# https://docs.djangoproject.com/pt-br/5.0/topics/email/

EMAIL_HOST = "0.0.0.0"

EMAIL_PORT = 1025

# EMAIL_USE_TLS = False

# EMAIL_HOST_USER = ""

# EMAIL_HOST_PASSWORD = ""
