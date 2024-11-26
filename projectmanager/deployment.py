import os
from pathlib import Path
from urllib.parse import urlparse

BASE_DIR = Path(__file__).resolve().parent.parent

# SECRET_KEY and Debug settings should be properly managed for different environments
DEBUG = os.getenv('DEBUG', 'True') == 'True'  # Default to True for local development
SECRET_KEY = os.getenv('MY_SECRET_KEY', 'django-insecure-c^4%i(7u4!y#i2&7%0(@qny*v43i2a!3f+s%*m16uli)^-4h6=')

ALLOWED_HOSTS = [os.getenv('WEBSITE_HOSTNAME', 'localhost')]  # Use environment variable or fallback to localhost

# Database configuration
if DEBUG:  # Local development uses SQLite
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
else:  # Production uses PostgreSQL
    connection_string = os.getenv('AZURE_POSTGRESQL_CONNECTIONSTRING')
    parsed_url = urlparse(connection_string)
    parameters = {
        'dbname': parsed_url.path[1:],  # Remove the leading '/'
        'user': parsed_url.username,
        'password': parsed_url.password,
        'host': parsed_url.hostname,
    }

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': parameters['dbname'],
            'USER': parameters['user'],
            'PASSWORD': parameters['password'],
            'HOST': parameters['host'],
        }
    }

# Static and Media settings for production
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage' if not DEBUG else 'django.contrib.staticfiles.storage.StaticFilesStorage'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Middleware for production
if not DEBUG:
    MIDDLEWARE = [
        'django.middleware.security.SecurityMiddleware',
        'whitenoise.middleware.WhiteNoiseMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
        'users.middleware.RoleRequiredMiddleware',
    ]
else:
    MIDDLEWARE = [
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
        'users.middleware.RoleRequiredMiddleware',
    ]
