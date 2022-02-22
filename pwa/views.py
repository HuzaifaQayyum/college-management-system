from django.shortcuts import render
from django.conf import settings

from core.settings.pwa import PWA_CONFIG


def service_worker(request, *args, **kwargs):
    return render(request, [ 'sw.js', 'pwa/sw.js' ], 
                 { 'PWA_START_URL': settings.PWA_CONFIG and settings.PWA_CONFIG.get("start_url", "/") }, 
                 content_type="application/javascript")

def manifest(request):
    PWA_CONFIG = (settings.PWA_CONFIG.items())
    
    return render(request, 'pwa/manifest.webmanifest', { 'PWA_CONFIG': PWA_CONFIG, 'total_items': len(PWA_CONFIG) - 1 }, 
                  content_type='application/manifest+json')
    
def offline(request):
    return render(request, ['offline.html', 'pwa/offline.html'])