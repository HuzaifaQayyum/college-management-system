import json

from django import template
from django.core.serializers.json import DjangoJSONEncoder
from django.utils.safestring import mark_safe
from django.conf import settings

register = template.Library()


@register.filter(is_safe=True)
def js(obj):
    """ Transform a python object so it can be safely used in javascript/JSON. """
    return mark_safe(json.dumps(obj, cls=DjangoJSONEncoder))


@register.inclusion_tag('includes/pwa.html', takes_context=True)
def progressive_web_app_meta(context):
    return {
        key: value
        for key, value in settings.PWA_CONFIG.items()
    }
    