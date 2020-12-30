from mysite.settings.base import *

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'djangogirls',
        'USER': 'emanoel',
        'PASSWORD': os.environ['DATABASES_PASSWORD'],
        'HOST': 'localhost',
        'PORT': '',
    }
}

DATABASES['default'].update(db_from_env)
