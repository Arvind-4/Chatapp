from decouple import config

DJANGO_REDIS_HOST = config('DJANGO_REDIS_HOST', cast=str)
DJANGO_REDIS_PORT = config('DJANGO_REDIS_PORT', cast=str)
DJANGO_REDIS_PASSWORD = config('DJANGO_REDIS_PASSWORD', cast=str)
DJANGO_REDIS_USERNAME = config('DJANGO_REDIS_USERNAME', cast=str)

DJANGO_REDIS_URL = f'redis://{REDIS_USER}:{REDIS_PASSWORD}@{REDIS_HOST}:{REDIS_PORT}'

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [str(DJANGO_REDIS_URL)],
        },
    },
}