import os
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
else:
    # For key=value format (e.g., dbname=mydb user=myuser password=mypassword host=myhost)
    parameters = {pair.split('=')[0]: pair.split('=')[1] for pair in connection_string.split(' ')}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': parameters['dbname'],
        'USER': parameters['user'],
        'PASSWORD': parameters['password'],
        'HOST': parameters['host'],
    }
}
