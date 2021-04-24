"""
Django settings for django_api project.

Generated by 'django-admin startproject' using Django 3.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from django.http import JsonResponse
from django.utils.translation import ugettext_lazy as _
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'vn5iga)cc=i6n$w&zz45u)$@(#c&oal%77w77b8y0b)bs1o#t6'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

# Application startapp

INSTALLED_APPS += [
    'rest_framework',
    'rest_framework.authtoken',
    'drf_yasg',  # swagger
    # 'django_celery_beat', # https://github.com/celery/django-celery-beat
    'app',
    'api',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

MIDDLEWARE += [
    # How the language is determined
    # https://www.django-rest-framework.org/topics/internationalization/#how-the-language-is-determined
    'django.middleware.locale.LocaleMiddleware',
    'drf_yasg.middleware.SwaggerExceptionMiddleware',
    # DataFlair #Caching Middleware

    # Cache
    # 'django.middleware.cache.UpdateCacheMiddleware', # Lỗi đăng nhập đăng xuất Rest Framework
    'django.middleware.cache.FetchFromCacheMiddleware',
    'corsheaders.middleware.CorsMiddleware', # https://github.com/adamchainz/django-cors-headers
]

ROOT_URLCONF = 'django_api.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # 'DIRS': [], # Default
        'DIRS': [os.path.join(BASE_DIR, 'templates')], # {root_project}\templates
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'django_api.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE' : 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3')
    }
}

# dashboard.heroku.com -> app -> Overview -> Heroku Postgres -> Settings -> View Credentials...

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'deu3juvfppit7r',
        'USER': 'myuzqvhmocqgrv',
        'PASSWORD': '2b6f0dce8891bc60ea0341ba6bf9e0f651335a426c25788ff1e68e1f3747f8b2',
        'HOST': 'ec2-18-215-111-67.compute-1.amazonaws.com',
        'PORT': '',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Ho_Chi_Minh'  # TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR, "files")
STATIC_ROOT = "var/www/static/"
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'django_api', 'static'),
]


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# REST framework's Settings
# https://www.django-rest-framework.org/api-guide/settings/

REST_FRAMEWORK = {

    # API version
    'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.NamespaceVersioning',
    # 'DEFAULT_VERSION': 'v1', # comment tren swagger se hien nhieu phien ban
    # 'ALLOWED_VERSIONS': ('v1', 'v2'),

    # Unix timestamp, only on Docker/Linux
    # 'DATETIME_FORMAT': '%s.%f',

    # 'DATETIME_FORMAT': '%Y-%m-%dT%H:%M:%S.%fZ',

    # Timestamp for Js
    # 'DATETIME_FORMAT': '%s000.%f',

    # 'DATE_FORMAT': '%s000.%f',

    # Render https://www.django-rest-framework.org/api-guide/renderers/

    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
        'drf_renderer_xlsx.renderers.XLSXRenderer',
    ],

    # Authentication
    # 'DEFAULT_AUTHENTICATION_CLASSES': [
        # 'rest_framework_simplejwt.authentication.JWTAuthentication',
        # 'rest_framework.authentication.SessionAuthentication',
        # 'rest_framework.authentication.BasicAuthentication',
        # 'rest_framework.authentication.TokenAuthentication',
    # ],
    # 'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.CursorPagination',
    # 'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
    'EXCEPTION_HANDLER': 'app.utils.custom_exception_handler',

    # 'EXCEPTION_HANDLER': 'django_api.ultils.exception.custom_exception_handler', # Thông báo lỗi

    # https://www.django-rest-framework.org/api-guide/metadata/
    # 'DEFAULT_METADATA_CLASS': 'rest_framework.metadata.SimpleMetadata',

    # https://www.django-rest-framework.org/api-guide/settings/#default_authentication_classes
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ],
}




# Set path('api-auth/', include('rest_framework.urls')) in urls.py

LOGIN_URL = 'rest_framework:login'
LOGOUT_URL = 'rest_framework:logout'


# Swagger Settings
# https://drf-yasg.readthedocs.io/en/stable/settings.html

SWAGGER_SETTINGS = {
    # 'USE_SESSION_AUTH': False,
    # 'SECURITY_DEFINITIONS': {
    #     'basic': {
    #         'type': 'basic'
    #     },
    #     'api_key': {
    #         'type': 'apiKey',
    #         'in': 'header',
    #         'name': 'Authorization'
    #     }
    # },
    # 'APIS_SORTER': 'alpha',
    'SUPPORTED_SUBMIT_METHODS': ['get', 'post', 'put', 'delete', 'patch'],
    'OPERATIONS_SORTER': 'alpha',
    'SECURITY_DEFINITIONS': {
        'basic': {
            'type': 'basic'
        },
        'api_key': {
            'type': 'apiKey',
            'name': 'Authorization',
            'in': 'header'
        }
    },

    # Hidden model in swagger docs
    'DEFAULT_FIELD_INSPECTORS': [
        'drf_yasg.inspectors.CamelCaseJSONFilter',
        'drf_yasg.inspectors.InlineSerializerInspector',
        'drf_yasg.inspectors.RelatedFieldInspector',
        'drf_yasg.inspectors.ChoiceFieldInspector',
        'drf_yasg.inspectors.FileFieldInspector',
        'drf_yasg.inspectors.DictFieldInspector',
        'drf_yasg.inspectors.SimpleFieldInspector',
        'drf_yasg.inspectors.StringDefaultFieldInspector',
    ],

}


# LANGUAGES
# https://docs.djangoproject.com/en/3.1/ref/settings/#std:setting-LANGUAGES

LANGUAGES = [
    ('de', _('German')),
    ('en', _('English')),
    ('vi-vn', _('Vietnamese')),
    ('ja-JP', _('Japanese')),
]

# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
#         'LOCATION': 'my_cache_table',
#         'TIMEOUT': 604800
#     }
# }


# CACHES = {
#     "default": {
#         "BACKEND": "django_redis.cache.RedisCache",
#         "LOCATION": "redis://" + os.getenv('REDIS_CONTAINER_NAME', '127.0.0.1') + ":6379/1",
#         "OPTIONS": {
#             "CLIENT_CLASS": "django_redis.client.DefaultClient",
#             "SOCKET_CONNECT_TIMEOUT": 5,  # seconds
#             "SOCKET_TIMEOUT": 5,  # seconds
#         },
#         "KEY_PREFIX": "example",
#         "TIMEOUT": 5,
#         "TTL": 5,
#     }
# }

# SESSION_ENGINE = "django.contrib.sessions.backends.cache" # Lỗi admin re-login khi reloading code
# SESSION_CACHE_ALIAS = "default"


# Locale
# https://docs.djangoproject.com/en/3.1/ref/settings/#std:setting-LOCALE_PATHS

LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale')
]


def custom404(request, exception=None):
    return JsonResponse({
        'status_code': 404,
        'error': 'The resource was not found'
    })


handler404 = custom404

# https://docs.djangoproject.com/en/3.1/ref/settings/#std:setting-AUTH_USER_MODEL

# AUTH_USER_MODEL = 'app.User'


# Email configuration
# https://docs.djangoproject.com/en/3.1/ref/settings/#std:setting-EMAIL_BACKEND

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'tanphongtr@gmail.com'
EMAIL_HOST_PASSWORD = 'ucnditvoiovkzawu'  # past the key or password app here
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'default from email'


# For heroku.com

import django_heroku
django_heroku.settings(locals())

APPEND_SLASH = True  # dấu / cuối URL

# Djano Cors Header configuration
# https://github.com/adamchainz/django-cors-headers

CORS_ALLOWED_ORIGINS = [
    # "https://example.com",
    # "https://sub.example.com",
    # "http://localhost:8080",
    "http://localhost:3000",
    # "http://127.0.0.1:9000"
]

# Celery configuration
# https://docs.celeryproject.org/en/stable/userguide/configuration.html

CELERY_BROKER_URL = ':pce43805469edf62c5f0b1e116c51f706d740b990019fdd6aa25178e3f65e4c15@ec2-18-215-9-210.compute-1.amazonaws.com:28040'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_BACKEND = ':pce43805469edf62c5f0b1e116c51f706d740b990019fdd6aa25178e3f65e4c15@ec2-18-215-9-210.compute-1.amazonaws.com:28040'
