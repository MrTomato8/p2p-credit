__author__ = "hsk81"
__date__ = "$Apr 23, 2012 10:15:15 AM$"

################################################################################
################################################################################

import os
SITE_ROOT = os.path.realpath (os.path.dirname (__file__))
SITE_NAME = 'p2p-credit'
SITE_HOST = 'blackhan.ch'

import socket
DEBUG = socket.gethostname () != SITE_HOST
TEMPLATE_DEBUG = DEBUG

if DEBUG:
    SITE_HOST = 'localhost'

ADMINS = (('admin', 'admin@mail.net'),)
MANAGERS = ADMINS

DATABASES = {
    'default' : {
        'ENGINE' : 'django.db.backends.sqlite3',
        'NAME' : os.path.join (SITE_ROOT, 'sqlite.db'),
    }
}

TIME_ZONE = 'Europe/Zurich'
LANGUAGE_CODE = 'en-us'
SITE_ID = 1
USE_I18N = True
USE_L10N = True

ROOT_URLCONF = '%s.urls' % SITE_NAME

MEDIA_ROOT = os.path.join (SITE_ROOT, 'media/')
MEDIA_URL = 'http://media.%s/%s/' % (SITE_HOST, SITE_NAME)
ADMIN_MEDIA_PREFIX = '/media/'

SECRET_KEY = 'x3)plrdnktt6lfqclllhl2jvzd%@1_il8dr$wn$lq(7mwu(k+&'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
 ## 'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'raven.contrib.django.middleware.SentryResponseErrorIdMiddleware',

    'django.middleware.common.CommonMiddleware',
    'django.middleware.transaction.TransactionMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
 ## 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',

    'raven.contrib.django.middleware.Sentry404CatchMiddleware',
)

if DEBUG:
    MIDDLEWARE_CLASSES += ('django_pdb.middleware.PdbMiddleware',)

CACHES = {
    'default' : {
        'BACKEND' : 'django.core.cache.backends.memcached.PyLibMCCache',
        'LOCATION' : '127.0.0.1:11211',
        'TIEMOUT' : 180, #[s]
    }
}

SESSION_ENGINE = 'django.contrib.sessions.backends.db'
SESSION_FILE_PATH = os.path.join (SITE_ROOT, 'session/')
SESSION_COOKIE_AGE = 365 * 24 * 60 * 60 ## secs: a year
SESSION_COOKIE_NAME = 'sid.'
SESSION_COOKIE_SECURE = False

TEMPLATE_DIRS = (os.path.join (SITE_ROOT, 'templates/'),)
FIXTURE_DIRS = (
    os.path.join (SITE_ROOT, 'fixtures/'),
    os.path.join (SITE_ROOT, 'fixtures/apps'),
)

## SENTRY_DSN = 'http://%s:%s@localhost:9000/1' % (
##    '...', '...'
## )

INSTALLED_APPS = (
    'raven.contrib.django',
    'django_pdb',

    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.admindocs',

    'svc', 'people', 'org', 'com', 'edu', 'prj', 'auction',
)

################################################################################
################################################################################

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'root': {
        'level': 'WARNING',
        'handlers': ['sentry'],
    },
    'formatters': {
        'verbose': {
            'format': '[%(asctime)s] %(levelname)s -- ' \
                '%(module)s (pid:%(process)d,tid:%(thread)d): %(message)s'
        },
    },
    'handlers': {
        'sentry': {
            'level': 'ERROR',
            'class': 'raven.contrib.django.handlers.SentryHandler',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        }
    },
    'loggers': {
        'django.db.backends': {
            'level': 'ERROR',
            'handlers': ['console'],
            'propagate': False,
        },
        'raven': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False,
        },
        'sentry.errors': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False,
        },
    },
}

################################################################################
################################################################################
