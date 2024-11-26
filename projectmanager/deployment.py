import os 
from .settings import * 
from .settings import BASE_DIR

ALLOWED_HOSTS = [os.environ['WEBSITE_HOSTNAME']]
CSRF_TRUSTED_ORIGINS =['https://'+ os.environ['WEBSITE_HOSTNAME']]
DEBUG = False
SECRET_KEY = os.environ['MY_SECRET_KEY']


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenose.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'users.middleware.RoleRequiredMiddleware',
]


STATICFILES_STORAGE ='whitenoise.storage.CompressedManifestStaticFilesStorage'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

connection_string = os.environ['AZURE_POSTGRESQL_CONNECTIONSTRING']
parameters = {pair.split('='):pair.split('=')[1] for pair in connection_string.split(' ')}

DATABASES = {
    
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': parameters['dbname'],
        'USER': parameters['user'],
        'PASSWORD': parameters['password'],
        'HOST': parameters['host'],
    }
}

