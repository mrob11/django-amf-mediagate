from django.conf import settings

GATEWAY_ROOT = getattr(settings, 'GATEWAY_ROOT', getattr(settings, 'MEDIA_ROOT', ''))
