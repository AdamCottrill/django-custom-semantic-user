"""Settings to be used for running tests.

usage: python manage.py test myusers --settings=config.settings.test

or

py.test

"""





import logging
import os

from config.settings.base import *


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '!y5c572%wm%+_skad5=2ck%bkts4ei=2acir3%z$^jm%foh-m&'

DEBUG = True


USE_TZ = False

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    }
}

PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.MD5PasswordHasher',
)




logging.getLogger("factory").setLevel(logging.WARN)
