from gluttony.settings.common import *

SECRET_KEY = 'SECRET_KEY'

API_TOKEN = 'API_TOKEN'

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
