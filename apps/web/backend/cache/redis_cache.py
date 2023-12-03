from decouple import config

DJANGO_REDIS_AVAILABLE = config('DJANGO_REDIS_AVAILABLE', cast=bool)

if DJANGO_REDIS_AVAILABLE:
    print("Redis is available using Docker.")
    DJANGO_REDIS_HOST = config('DJANGO_REDIS_HOST', cast=str)
    DJANGO_REDIS_PORT = config('DJANGO_REDIS_PORT', cast=int)
    CHANNEL_LAYERS = {
        "default": {
            "BACKEND": "channels_redis.core.RedisChannelLayer",
            "CONFIG": {
                "hosts": [(
                    DJANGO_REDIS_HOST,
                    DJANGO_REDIS_PORT,
                )],
            },
        },
    }
else:
    print("Redis is not available using Docker. Using InMemoryChannelLayer.")
    CHANNEL_LAYERS = {
        "default": {
            "BACKEND": "channels.layers.InMemoryChannelLayer"
       }
    }