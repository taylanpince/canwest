import os

DEBUG = False
TEMPLATE_DEBUG = DEBUG

SERVER_EMAIL = 'errors@canwest.vortexmobile.ca'
DEFAULT_FROM_EMAIL = 'no-reply@canwest.vortexmobile.ca'

ADMINS = (
    ('Taylan Pince', 'taylanpince@gmail.com'),
)

MANAGERS = ADMINS

TIME_ZONE = 'Canada/Eastern'

USE_I18N = True
LANGUAGE_CODE = 'en'

SITE_ID = 1

MEDIA_ROOT = os.path.join(os.path.realpath(os.path.dirname(__file__)), 'media/')
MEDIA_URL = '/media/'

SECRET_KEY = 'w8x-%@cm#8&ve7ef&-ep7r9dxmayyy-9!n1!zt+rpiu^qbm2&-'

CACHE_BACKEND = 'memcached://127.0.0.1:11211/'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'admob.middleware.AdMobMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'devices.middleware.DeviceDetectMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.core.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "devices.context_processors.device",
)

ROOT_URLCONF = 'canwest.urls'

TEMPLATE_DIRS = (
    os.path.join(os.path.realpath(os.path.dirname(__file__)), 'templates/'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.markup',
    
    'admob',
    'django_extensions',
    'sorl.thumbnail',
    'south',
    
    'contests',
    'devices',
    'schedules',
    'shows',
    'twitter',
)

TWITTER_CONSUMER_KEY = 'Qi0PXu0ZBrSwYv2ERDb45g'
TWITTER_CONSUMER_SECRET = 'RZrqynBZwhewuhpZx3nkTvAKnawjTBYMVNPI73BdHU'

ADMOB_PUBLISHER_ID = 'a14beda375ab4fa'
ADMOB_ANALYTICS_ID = 'a14beda375ab4fa'
ADMOB_TEST = False

DEVICE_ATLAS_PATH = os.path.join(os.path.realpath(os.path.dirname(__file__)), 'devices/devices.json')

try:
    from settings_local import *
except:
    pass

ADMIN_MEDIA_PREFIX = MEDIA_URL + 'admin/'
