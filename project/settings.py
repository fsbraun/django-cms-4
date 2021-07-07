"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 3.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os

from .utils.sanitize import sanitize


def gettext(s):
    """
    i18n passthrough
    """
    return s


env = os.environ.get

# ***** PATHS *****

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.abspath(os.path.join(PROJECT_DIR, '../'))

# ***** PROJECT BASICS *****

SITE_ID = 1
PROJECT_NAME = 'cms demo'
RELEASE_NUMBER = __import__('project').VERSION
VERSION = RELEASE_NUMBER

DEBUG = sanitize(env('DEBUG', 'no'), bool)
BUILD_ENV = sanitize(env('BUILD_ENV', 'no'), bool)
WSGI_APPLICATION = 'project.wsgi.application'
ROOT_URLCONF = 'project.urls'

LOCAL_NETWORK = env('LOCAL_NETWORK', '127.0.0.0/8')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env(
    'DJANGO_SECRET_KEY',
    'django-insecure-ikx3n9+1m7@^qe$5n&#k3e6)pl2)#v(9q-3i^!uauszk6dk09p'
)

ALLOWED_HOSTS = []

REFERRER_POLICY = 'strict-origin'

CSRF_COOKIE_SECURE = sanitize(env('CSRF_COOKIE_SECURE', False), bool)
SESSION_COOKIE_SECURE = sanitize(env('SESSION_COOKIE_SECURE', False), bool)

SECURE_BROWSER_XSS_FILTER = sanitize(
    env('SECURE_BROWSER_XSS_FILTER', False), bool
)
SECURE_CONTENT_TYPE_NOSNIFF = sanitize(
    env('SECURE_CONTENT_TYPE_NOSNIFF', False), bool
)
SECURE_HSTS_SECONDS = sanitize(env('SECURE_HSTS_SECONDS', 31536000), int)
SECURE_HSTS_INCLUDE_SUBDOMAINS = sanitize(
    env('SECURE_HSTS_INCLUDE_SUBDOMAINS', False), bool
)

# Application definition

INSTALLED_APPS = [

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.flatpages',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'django.contrib.staticfiles',

    'cms',
    'django_extensions',
    'djangocms_alias',
    'djangocms_pageadmin',
    'djangocms_text_ckeditor',
    'djangocms_url_manager',
    'djangocms_versioning',
    'djangocms_version_locking',
    'filer',
    'easy_thumbnails',
    'menus',
    'parler',
    'sekizai',
    'storages',
    'treebeard',

    'project',
]


MIDDLEWARE = [
    'cms.middleware.utils.ApphookReloadMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
]

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASE_ENGINE = env(
    'DATABASE_ENGINE',
    'django.db.backends.postgresql'
)
DATABASE_HOST = env('DATABASE_HOST')
DATABASE_PORT = env('DATABASE_PORT')
DATABASE_USER = env('DATABASE_USER')
DATABASE_PASSWORD = env('DATABASE_PASSWORD')
DATABASE_NAME = env('DATABASE_NAME')

DATABASES = {
    'default': {
        'ENGINE': DATABASE_ENGINE,
        'HOST': DATABASE_HOST,
        'PORT': DATABASE_PORT,
        'USER': DATABASE_USER,
        'PASSWORD': DATABASE_PASSWORD,
        'NAME': DATABASE_NAME,
        'CONN_MAX_AGE': 0,
        'ATOMIC_REQUESTS': False,
    }
}

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# ***** AUTH *****

SESSION_COOKIE_AGE = 14400  # 4 hr
SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'
MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.' + validator
    }
    for validator in (
        'UserAttributeSimilarityValidator',
        'MinimumLengthValidator',
        'CommonPasswordValidator',
        'NumericPasswordValidator',
    )
]


# ***** STATIC FILES *****

STATIC_ROOT = os.path.join(BASE_DIR, 'static-collection')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STATIC_URL = env('STATIC_URL', '/static/')  # allow CloudFront override
LOCAL_STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(PROJECT_DIR, 'static'),
)
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

# ***** MEDIA FILES / UPLOADS *****

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

S3_BUCKET = env('S3_BUCKET', '')
S3_SUB_BUCKET = env('S3_SUB_BUCKET', '')
S3_REGION = env('S3_REGION', 'eu-west-2')
AWS_REGION = env('AWS_REGION', 'eu-west-2')
S3_USE_SIGV4 = True

AWS_S3_PATH_SEPARATOR = '/'
AWS_STORAGE_BUCKET_NAME = S3_BUCKET
AWS_S3_HOST = f'{S3_BUCKET}.s3.{S3_REGION}.amazonaws.com'
AWS_S3_SIGNATURE_VERSION = 's3v4'
AWS_S3_ADDRESSING_STYLE = 'virtual'
AWS_DEFAULT_ACL = 'private'
AWS_LOCATION = S3_SUB_BUCKET
AWS_S3_FILE_OVERWRITE = False

# ALIAS S3 settings
AWS_S3_BUCKET = S3_BUCKET
AWS_S3_PRIVATE_BUCKET = S3_BUCKET
AWS_S3_REGION_NAME = S3_REGION
AWS_S3_SUB_BUCKET = S3_SUB_BUCKET
AWS_S3_PRIVATE_SUB_BUCKET = S3_SUB_BUCKET

AWS_S3_BUCKET_URL = f'https://{AWS_S3_HOST}'
AWS_S3_SUB_BUCKET_URL = f'{AWS_S3_BUCKET_URL}/{AWS_S3_SUB_BUCKET}'

MEDIA_URL = AWS_S3_BUCKET_URL + '/'

# ***** TEMPLATES *****

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'project', 'templates'),
        ],
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.media',
                'django.template.context_processors.csrf',
                'django.template.context_processors.tz',
                'sekizai.context_processors.sekizai',
                'django.template.context_processors.static',
                'cms.context_processors.cms_settings',
            ],
            'loaders': [
                'apptemplates.Loader',
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader'
            ],
        },
    },
]

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ***** CMS *****

CMS_PAGE_CACHE = False
CMS_PLUGIN_CACHE = False

CMS_PERMISSION = True
CMS_TOOLBAR_ANONYMOUS_ON = False

CMS_LANGUAGES = {
    1: [
        {
            'code': 'en',
            'name': gettext('English'),
        },
    ],
    'default': {
        'fallbacks': ['en', ],
        'redirect_on_fallback': True,
        'public': True,
        'hide_untranslated': False,
    },
}

CMS_PAGE_TEMPLATE = 'page.html'

CMS_TEMPLATES = (
    (CMS_PAGE_TEMPLATE, 'Page'),
)

X_FRAME_OPTIONS = 'SAMEORIGIN'

CMS_PLACEHOLDER_CONF = {}

# ***** DEBUG TOOLBAR *****

DEBUG_TOOLBAR = DEBUG and env('DEBUG_TOOLBAR', 'no') == 'yes'

if DEBUG_TOOLBAR:
    INTERNAL_IPS = [
        '127.0.0.1',
    ]
    INSTALLED_APPS += [
        'debug_toolbar',
    ]
    MIDDLEWARE += [
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    ]
    DEBUG_TOOLBAR_PATCH_SETTINGS = False
    DEBUG_TOOLBAR_CONFIG = {
        'SHOW_TOOLBAR_CALLBACK': lambda request: not request.is_ajax(),
    }
