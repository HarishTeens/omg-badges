from .base import *

DEBUG = True
ALLOWED_HOSTS = ['localhost','badges.dscnitrourkela.tech']

CORS_ORIGIN_WHITELIST =['http://localhost:8080']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}