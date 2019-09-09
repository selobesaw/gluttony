from gluttony.settings.common import *

SECRET_KEY = 'SECRET_KEY'

API_TOKEN = 'API_TOKEN'

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'postgres',
        'PORT': '5432',
    }
}
