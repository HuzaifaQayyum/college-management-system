from .base import *

SECRET_KEY = 'django-insecure-2=xr6=ilyoe*40s_gnnmi3zp!j@9teqmlwn9p5a6*1ozn3em47'

DEBUG = True

ALLOWED_HOSTS = []
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'constance',
    'constance.backends.database',
    'debug_toolbar',
    'django_media_fixtures',

    'modeladmin_reorder',
    'categories',
    'library',
    'accounts',
    'pwa',
    'core',
    'quiz'
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'modeladmin_reorder.middleware.ModelAdminReorder',
]


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


INTERNAL_IPS = [
    # ...
    "127.0.0.1",
    # ...
]