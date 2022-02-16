from .base import *

SECRET_KEY = 'django-insecure-2=xr6=ilyoe*40s_gnnmi3zp!j@9teqmlwn9p5a6*1ozn3em47'

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
