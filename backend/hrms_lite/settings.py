import os
from pathlib import Path
from urllib.parse import parse_qs, urlparse

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-assignment-secret-key'
DEBUG = True
ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'rest_framework',
    'hr',
    'attendance',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'hrms_lite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'hrms_lite.wsgi.application'
ASGI_APPLICATION = 'hrms_lite.asgi.application'

NEON_DATABASE_URL = (
    'postgresql://neondb_owner:npg_Frl6VHRjaL1z@'
    'ep-purple-sound-aifudf4j-pooler.c-4.us-east-1.aws.neon.tech/'
    'neondb?sslmode=require&channel_binding=require'
)


def _postgres_from_url(db_url: str) -> dict:
    parsed = urlparse(db_url)
    query_options = {k: v[-1] for k, v in parse_qs(parsed.query).items()}
    return {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': parsed.path.lstrip('/'),
        'USER': parsed.username or '',
        'PASSWORD': parsed.password or '',
        'HOST': parsed.hostname or '',
        'PORT': str(parsed.port or 5432),
        'OPTIONS': query_options,
        'CONN_MAX_AGE': 60,
    }

DATABASE_URL = os.getenv('DATABASE_URL', NEON_DATABASE_URL)
DATABASES = {
    'default': _postgres_from_url(DATABASE_URL)
}

AUTH_PASSWORD_VALIDATORS = []

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CORS_ALLOW_ALL_ORIGINS = True

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
    ],
    'EXCEPTION_HANDLER': 'hrms_lite.utils.custom_exception_handler',
}
