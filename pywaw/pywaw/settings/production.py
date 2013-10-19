from .base import *

DEBUG = False
TEMPLATE_DEBUG = DEBUG

MEDIA_ROOT = os.path.join(STATIC_ROOT, 'upload')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': get_env_var('DB_NAME'),
        'USER': get_env_var('DB_USER'),
        'PASSWORD': get_env_var('DB_PASSWORD'),
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
