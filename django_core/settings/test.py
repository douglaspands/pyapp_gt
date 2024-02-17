from django_core.settings.base import *

DEBUG = False

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ROOT_DIR / "dbtest.sqlite3",
    }
}

# Email
# https://docs.djangoproject.com/pt-br/5.0/topics/email/

EMAIL_HOST = "0.0.0.0"

EMAIL_PORT = 1025

# EMAIL_USE_TLS = False

# EMAIL_HOST_USER = ""

# EMAIL_HOST_PASSWORD = ""
