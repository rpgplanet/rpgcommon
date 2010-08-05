# -*- coding: utf-8 -*-

from os.path import dirname, join

import rpgcommon

ADMINS = (
    ('Almad', 'bugs@almad.net'),
)
MANAGERS = ADMINS


VERSION = rpgcommon.__versionstr__

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/Prague'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'cs'

# Site ID
SITE_ID = 1
DEFAULT_PAGE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = join(dirname(rpgcommon.__file__), 'static')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/static/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/static/admin_media/'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

#MIDDLEWARE_CLASSES = (
#    'django.middleware.common.CommonMiddleware',
#    'django.contrib.sessions.middleware.SessionMiddleware',
#    'django.contrib.auth.middleware.AuthenticationMiddleware',
#    "django.middleware.transaction.TransactionMiddleware",
#
##    'ella.core.context_processors.url_info',
#
#    'rpghrac.rpgplayer.middleware.SetDomainOwnerMiddleware'
#)

ROOT_URLCONF = 'rpgcommon.urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    join(dirname(rpgcommon.__file__), 'templates'),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.media',
    'django.core.context_processors.auth',
    'django.core.context_processors.request',
)

SOUTH_AUTO_FREEZE_APP = True
SKIP_SOUTH_TESTS = True

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.media',
    'django.core.context_processors.request',
    'django.core.context_processors.auth',
#    'ella.newman.context_processors.newman_media',
    'ella.core.context_processors.url_info',
    'rpgcommon.service.context_processors.service_tokens',
)

INSTALLED_APPS = (
    # core django apps
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',

    # ella-related
    'south',
    'ella',
    'ella.core',
    'ella.articles',

    #migration wtf
    'ella.photos',

    'djangomarkup',
    'tagging',

    # internal shared apps
    'rpgcommon.service',
    'rpgcommon.user',

    # rpgplanet
    'rpgplanet.service',
    'rpgplanet.betainfo',

    # rpghrac subdomains
    'rpghrac.service',
    'rpghrac.rpgplayer',

)


# debug - find a way to pass it to local.py (how to extend previously defined settings)
INSTALLED_APPS += (
    'django_extensions',
)


AUTH_PROFILE_MODULE = 'user.UserProfile'
MESSAGE_STORAGE = "django.contrib.messages.storage.session.SessionStorage"

CHERRYPY_TEST_SERVER = True


