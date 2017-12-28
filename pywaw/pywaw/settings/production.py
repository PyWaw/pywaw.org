from .base import *

DEBUG = get_env_var('DEBUG') == 'true'
TEMPLATE_DEBUG = DEBUG

MEDIA_ROOT = '/media'
STATIC_ROOT = '/static'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': get_env_var('DB_NAME'),
        'USER': get_env_var('DB_USER'),
        'PASSWORD': get_env_var('DB_PASSWORD'),
        'HOST': get_env_var('DB_HOST'),
        'PORT': get_env_var('DB_PORT'),
    }
}

EMAIL_HOST = get_env_var('EMAIL_HOST')
EMAIL_PORT = int(get_env_var('EMAIL_PORT'))
EMAIL_USE_TLS = get_env_var('EMAIL_USE_TLS') == 'true'
EMAIL_HOST_USER = get_env_var('EMAIL_HOST_USER')
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
EMAIL_HOST_PASSWORD = get_env_var('EMAIL_HOST_PASSWORD')
SERVER_EMAIL = EMAIL_HOST_USER
