from decouple import config

DJANGO_LIVE = config('DJANGO_LIVE', default=False, cast=bool)

if DJANGO_LIVE:
    from .local import *
else:
    from .production import *