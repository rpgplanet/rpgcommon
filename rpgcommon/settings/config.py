# -*- coding: utf-8 -*-
from tempfile import gettempdir
from os.path import dirname, join, pardir, abspath

import rpgcommon

DEBUG = True
TEMPLATE_DEBUG = DEBUG
ENABLE_DEBUG_URLS = DEBUG

DATABASE_ENGINE = 'sqlite3'
DATABASE_NAME = join(gettempdir(), 'rpgplanet.db')
TEST_DATABASE_NAME = join(gettempdir(), 'rpgplanetdb.db')
DATABASE_USER = ''
DATABASE_PASSWORD = ''
DATABASE_HOST = ''
DATABASE_PORT = ''

FILE_ROOT = dirname(rpgcommon.__file__)


# Make this unique, and don't share it with anybody.
SECRET_KEY = '88b-01f^x$%&^*&(&$)^*(U(8798756786(*bbbBBBndasdf)93!0#k(=mfv$'


MEDIA_ROOT = join(FILE_ROOT, 'media')
MEDIA_URL = '/media/'

STATIC_ROOT = join(FILE_ROOT, 'static')
STATIC_URL = '/static/'


ADMIN_MEDIA_PREFIX = '/static/admin_media/'


# init logger
LOGGING_CONFIG_FILE = join(FILE_ROOT, 'settings', 'logging.ini')

CACHE_BACKEND = 'dummy://'

TEST_MEDIA_ROOT = abspath(join(FILE_ROOT, pardir, 'tests', 'data'))

# should be set to None for production
TEST_MEDIA_URL = "/test/media/"

NEWMAN_MEDIA_PREFIX = '/settings/newman_media/'
