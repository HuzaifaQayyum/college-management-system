from .base import *
import os
import dj_database_url

DEBUG = os.environ.get('DEBUG', False)
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS').split(', ')

SECRET_KEY = os.environ['SECRET_KEY']

DATABASES = {
    'default': dj_database_url.config()
}

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    # 'cloudinary_storage',
    'django.contrib.staticfiles',
    'cloudinary',
    'constance',

    'modeladmin_reorder',
    'categories',
    'library',
    'accounts',
    'pwa',
    'core',
    'quiz'
]

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': os.environ['CLOUDINARY_NAME'],
    'API_KEY': os.environ['CLOUDINARY_API_KEY'],
    'API_SECRET': os.environ['CLOUDINARY_API_SECRET'],
}

# SECURE_SSL_REDIRECT = True
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'