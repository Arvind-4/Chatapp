from decouple import config

DJANGO_REDIS_HOST = config('DJANGO_REDIS_HOST', cast=str)
DJANGO_REDIS_PORT = config('DJANGO_REDIS_PORT', cast=str)
DJANGO_REDIS_PASSWORD = config('DJANGO_REDIS_PASSWORD', cast=str)
DJANGO_REDIS_USER = config('DJANGO_REDIS_USER', cast=str)

DJANGO_REDIS_URL = f'redis://{DJANGO_REDIS_USER}:{DJANGO_REDIS_PASSWORD}@{DJANGO_REDIS_HOST}:{DJANGO_REDIS_PORT}'

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [str(DJANGO_REDIS_URL)],
        },
    },
}