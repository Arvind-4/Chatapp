import pathlib
from decouple import config

DJANGO_PG_PASSWORD = config('DJANGO_PG_PASSWORD', cast=str)
DJANGO_PG_DATABASE = config('DJANGO_PG_DATABASE', cast=str)
DJANGO_PG_USER = config('DJANGO_PG_USER', cast=str)
DJANGO_PG_HOST = config('DJANGO_PG_HOST', cast=str)
DJANGO_PG_PORT = config('DJANGO_PG_PORT', cast=int)

DB_IS_AVAILABLE = all([
    DJANGO_PG_PASSWORD,
    DJANGO_PG_DATABASE,
    DJANGO_PG_USER,
    DJANGO_PG_HOST,
    DJANGO_PG_PORT,
])

if DB_IS_AVAILABLE:
    DATABASES = {
        'default': {
            'ENGINE': 'django_cockroachdb',
            'NAME': DJANGO_PG_DATABASE,
            'USER': DJANGO_PG_USER,
            'PASSWORD': DJANGO_PG_PASSWORD,
            'HOST': DJANGO_PG_HOST,
            'PORT': DJANGO_PG_PORT,
            'OPTIONS': {
                'sslmode': 'verify-full',
            },
        },
    }

    DATABASES['default']['CONN_MAX_AGE'] = None
    DATABASES['default']['ATOMIC_REQUESTS'] = True