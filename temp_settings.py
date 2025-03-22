from pathlib import Path
import os
import sentry_sdk


BASE_DIR = Path(__file__).resolve().parent.parent

# 환경 변수에서 값을 가져오도록 수정
SECRET_KEY = os.environ.get('SECRET_KEY', '14^k+a1kv#td)4fse**y$__gokotrx=kgf!lo%s04-6e)nrmg*')

SERVER_ENV = os.environ.get('SERVER_ENV', 'Main')

if SERVER_ENV == 'Local':
    DEBUG = True
    ALLOWED_HOSTS = ["*"]
else:
    DEBUG = os.environ.get('DJANGO_DEBUG', 'False') == 'True'
    ALLOWED_HOSTS = os.environ.get('DJANGO_ALLOWED_HOSTS', 'cwbeany.com').split(',')

# Database 설정
DATABASES = {
    'default': {
        'ENGINE': os.environ.get('DB_ENGINE', 'django.db.backends.mysql'),
        'NAME': os.environ.get('DB_NAME', 'blog'),
        'USER': os.environ.get('DB_USER', 'blog'),
        'PASSWORD': os.environ.get('DB_PASSWORD', 'lcw1401314!'),
        'HOST': os.environ.get('DB_HOST', 'localhost'),
        'PORT': os.environ.get('DB_PORT', '3306'),
    }
}

# Redis 설정
REDIS_HOST = os.environ.get('REDIS_HOST', 'localhost')
REDIS_PORT = int(os.environ.get('REDIS_PORT', 6379))
REDIS_DB = int(os.environ.get('REDIS_DB', 0))

# Celery 설정
CELERY_BROKER_URL = f'redis://{REDIS_HOST}:{REDIS_PORT}/1'
result_backend = f'redis://{REDIS_HOST}:{REDIS_PORT}/1'

# Redis 캐시 설정
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': f'redis://{REDIS_HOST}:{REDIS_PORT}/1',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}

# 나머지 원래 설정들... 