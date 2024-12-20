from pathlib import Path
import os
# import re
import dj_database_url
from corsheaders.defaults import default_headers, default_methods

# Load environment variables from env.py if it exists
if os.path.exists('env.py'):
    import env

# Cloudinary storage settings
CLOUDINARY_STORAGE = {
    'CLOUDINARY_URL': os.environ.get('CLOUDINARY_URL')
}
MEDIA_URL = '/media/'
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

# Base directory path for the project
BASE_DIR = Path(__file__).resolve().parent.parent

# Django REST framework settings
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [(
        'rest_framework.authentication.SessionAuthentication'
        if 'DEV' in os.environ
        else 'dj_rest_auth.jwt_auth.JWTCookieAuthentication'
    )],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
    'DATETIME_FORMAT': '%d %b %Y',
}

# If not in DEV, set JSONRenderer as the default renderer
if 'DEV' not in os.environ:
    REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'] = [
        'rest_framework.renderers.JSONRenderer',
    ]

# JWT and REST authentication settings
REST_USE_JWT = True
JWT_AUTH_SECURE = True
JWT_AUTH_COOKIE = 'my-app-auth'
JWT_AUTH_REFRESH_COOKIE = 'my-refresh-token'
JWT_AUTH_SAMESITE = 'None'

REST_AUTH_SERIALIZERS = {
    'USER_DETAILS_SERIALIZER': 'drf_api.serializers.CurrentUserSerializer'
}


# Security settings
SECRET_KEY = os.environ.get('SECRET_KEY')
DEBUG = 'DEBUG' in os.environ

# Allowed hosts configuration
ALLOWED_HOSTS = [
    os.environ.get('ALLOWED_HOST'),  # Allow host from environment variable
    'localhost',                     # Allow local development
    'drf-api-sam-c8393f26fa4b.herokuapp.com',  # <-- Add your Heroku domain here
    '8000-samgree-drfapi-ro0lht4dv2x.ws-eu116.gitpod.io'
]

# CORS settings
if 'CLIENT_ORIGIN' in os.environ:
    CORS_ALLOWED_ORIGINS = [
        os.environ.get('CLIENT_ORIGIN')
    ]
# Configure CORS for dynamic subdomains in CLIENT_ORIGIN_DEV
if 'CLIENT_ORIGIN_DEV' in os.environ:    
    CORS_ALLOWED_ORIGIN_REGEXES = [r"^https://.*\.codeinstitute-ide\.net$",]
CORS_ALLOW_CREDENTIALS = True


CORS_ALLOW_HEADERS = list(default_headers)
CORS_ALLOW_METHODS = list(default_methods)
# CSRF_TRUSTED_ORIGINS = [os.environ.get('CLIENT_ORIGIN_DEV', 'CLIENT_ORIGIN')]
CSRF_TRUSTED_ORIGINS = [
    'https://8000-samgree-drfapi-ro0lht4dv2x.ws-eu116.gitpod.io',  # Gitpod URL
    'https://drf-api-sam-c8393f26fa4b.herokuapp.com',  # Heroku URL
]



# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cloudinary_storage',
    'cloudinary',
    'rest_framework',
    'django_filters',
    'rest_framework.authtoken',
    'dj_rest_auth',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'dj_rest_auth.registration',
    'corsheaders',

    'profiles',
    'posts',
    'comments',
    'likes',
    'followers',
]

SITE_ID = 1

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'drf_api.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'staticfiles', 'build')],
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

WSGI_APPLICATION = 'drf_api.wsgi.application'


# Database configuration
DATABASES = {
    'default': ({
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    } if 'DEV' in os.environ else dj_database_url.parse(
        os.environ.get('DATABASE_URL')
    ))
}


# Password validation
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
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
WHITENOISE_ROOT = BASE_DIR / 'staticfiles' / 'build'


# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
