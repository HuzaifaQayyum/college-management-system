from django.urls import path
from .views import service_worker, manifest, offline

app_name = 'pwa'

urlpatterns = [
    path('serviceworker.js', service_worker, name='serviceworker'),
    path('manifest.webmanifest', manifest, name="manifest"),
    path('offline', offline, name="offline")
]
