from config.settings.base import *

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '!y5c572%wm%+_skad5=2ck%bkts4ei=2acir3%z$^jm%foh-m&'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

#these should be in settings.local
INSTALLED_APPS += ['debug_toolbar']

MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

INTERNAL_IPS = ['127.0.0.1',]
