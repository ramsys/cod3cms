from settings import *

DEBUG = True
INTERNAL_IPS = ("127.0.0.1",)
DEBUG_TOOLBAR_CONFIG = {"INTERCEPT_REDIRECTS": False}
ROOT_URLCONF = "urls"


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_ROOT, '../../data/sqlite3.db'),
    }
}

SECRET_KEY = 'development-key'


#MEDIA_URL = '/static/media/'
#MEDIA_ROOT = os.path.join(PROJECT_ROOT, '../../data/media/')
#MEDIA_ROOT = os.path.join(PROJECT_ROOT,'media')
