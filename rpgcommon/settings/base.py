# -*- coding: utf-8 -*-

from os.path import dirname, join

import rpgcommon

ADMINS = (
    ('Almad', 'bugs@almad.net'),
)
MANAGERS = ADMINS


VERSION = rpgcommon.__versionstr__

TIME_ZONE = 'Europe/Prague'

LANGUAGE_CODE = 'cs'

SITE_ID = 1
DEFAULT_PAGE_ID = 1

USE_I18N = True
USE_L10N = True

ADMIN_MEDIA_PREFIX = '/static/admin_media/'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

ROOT_URLCONF = 'rpgcommon.urls'

TEMPLATE_DIRS = (
    join(dirname(rpgcommon.__file__), 'templates'),
)

SOUTH_AUTO_FREEZE_APP = True
SKIP_SOUTH_TESTS = True

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.media',
    'django.core.context_processors.request',
    'django.contrib.auth.context_processors.auth',
#    'ella.newman.context_processors.newman_media',
    'ella.core.context_processors.url_info',
    'rpgcommon.service.context_processors.service_tokens',
    'rpgcommon.service.context_processors.common_variables',
)

INSTALLED_APPS = (
    # core django apps
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.redirects',

    # ella-related
    'south',
    'ella',
    'ella.core',
    'ella.articles',

    #migration wtf
    'ella.photos',

    # semi-required by ella, WTF
    'ella.newman',

    # awesomeness
    'djangomarkup',

    # posts, notifications & friends
    'pagination',
    'notification',
    'postman',

    'tagging',
    'avatar',

    # gabbling & mumbling
    'esus.phorum',

    # internal shared apps
    'rpgcommon.service',
    'rpgcommon.user',

    # rpgplanet
    'rpgplanet.service',
    'rpgplanet.betainfo',

    # rpgplanet con app
    'ellaschedule',
    'rpgscheduler.convention',

    # rpghrac subdomains
    'rpghrac.service',
    'rpghrac.rpgplayer',
    'rpghrac.zapisnik',

)


# debug - find a way to pass it to local.py (how to extend previously defined settings)
INSTALLED_APPS += (
    'django_extensions',
)

AUTH_PROFILE_MODULE = 'user.UserProfile'
MESSAGE_STORAGE = "django.contrib.messages.storage.session.SessionStorage"

CHERRYPY_TEST_SERVER = True

SKIP_SOUTH_TESTS = True

DEFAULT_MARKUP = 'czechtile'
DJANGO_MARKUP_ENABLE_REGISTER_ON_IMPORT = False

DJANGO_MARKUP_REGISTERED_FIELDS = [
    ('articles', 'article', 'description'),
    ('articles', 'articlecontents', 'content'),
    ('ellaschedule', 'event', 'description'),
]

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'rpgcommon.user.backends.FacebookBackend',
)

