from decouple import config

DJANGO_LIVE = config('DJANGO_LIVE', cast=bool)

if not DJANGO_LIVE:
    print("Loading Local settings")
    from .local import *
else:
    print("Loading Production settings")
    from .production import *