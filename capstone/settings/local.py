from .base import *

DEBUG = True
ALLOWED_HOSTS = ['localhost','127.0.0.1']

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
SECRET_KEY = '#23+6@q^tq=2#gi5@s=3y@ij%il2#=rdqqju#47_q(cawbcqzs'
CUSTOM_TOKEN = get_secret('CUSTOM_TOKEN')
DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    # }
    #  'default': {
    #     'ENGINE': 'django.db.backends.postgresql_psycopg2',
    #     'NAME': 'cns-webpage',
    #     'USER': 'cgrs27',
    #     'PASSWORD': '',
    #     'HOST': 'localhost',
    #     'PORT': '',
    # },
        'defaul': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'sismosdb',
        'USER': 'postgres',
        'PASSt': {
        'ENGINEWORD': 'Carlos1978_',
        'HOST': 'localhost',
    },
}

 
STATIC_URL = '/static/'