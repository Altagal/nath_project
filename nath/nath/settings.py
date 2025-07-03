import os
from pathlib import Path
from django.contrib import messages
from dotenv import load_dotenv
load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY'),

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DEBUG'),

ALLOWED_HOSTS = ["*"]
# ALLOWED_HOSTS = ['nath.ictb.fiocruz.br', 'www.nath.ictb.fiocruz.br']
# CSRF_TRUSTED_ORIGINS = ['https://www.nath.ictb.fiocruz.br']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    "crispy_forms",

    'accounts',
    'home',
    'gestao',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'django.middleware.locale.LocaleMiddleware',
    'django_session_timeout.middleware.SessionTimeoutMiddleware',
]

ROOT_URLCONF = 'nath.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            "nath/templates",
            "nath/templates/nath/crispy",
        ],
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

WSGI_APPLICATION = 'nath.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv('DATABASE_NAME'),
        'USER': os.getenv('DATABASE_USER'),
        'PASSWORD': os.getenv('DATABASE_PASSWORD'),
        'HOST': os.getenv('DATABASE_HOST'),
        'PORT': os.getenv('DATABASE_PORT'),
    },
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

# USE_I18N = True
# USE_L10N = False

LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'
MEDIA_URL = '/media/'
STATIC_ROOT = os.path.join(BASE_DIR, 'nath/staticfiles')
MEDIA_ROOT = os.path.join(BASE_DIR, 'nath/media')

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'nath/static'),
)

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap4"
CRISPY_TEMPLATE_PACK = "bootstrap4"

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MESSAGE_TAGS = {
    messages.SUCCESS: 'success',
    messages.WARNING: 'warning',
    messages.ERROR: 'error',
    messages.DEBUG: 'secondary',
    messages.INFO: 'info',
}

# classe usuario modificada
AUTH_USER_MODEL = 'accounts.Account'

# sobreescreve verificação de username para permitir username e email.
AUTHENTICATION_BACKENDS = ['accounts.backends.CustomEmailBackend']

LOGIN_URL = 'account_login'
LOGIN_REDIRECT_URL = 'account_login'

DEFAULT_PASSWORD = 'Ictb@1234'

# SESSION_EXPIRE_SECONDS = 60 * 30  # 30 MINUTES
SESSION_EXPIRE_AFTER_LAST_ACTIVITY = os.getenv('SESSION_EXPIRE'),



# CONEXÃO COM ONEDRIVE APARTIR DE UMA CONTA CONSUMER

# error: The grant was obtained for a different tenant.
# I found the solution, for my case i had to use this url : https://login.microsoftonline.com/common/
# For organizations only the url must be : https://login.microsoftonline.com/organizations
# And only for the same tenant of the organization : https://login.microsoftonline.com/{tenantId}

# nao funciona com o @fiocruz.br, limitado pelo administrador
# funcionando melhor com o gustavojordao@outlook.com


#CREDENCIAIS ONENOTE
MICROSOFT_ONLINE_URL = "https://login.microsoftonline.com/"
AUTHORITY_URL = MICROSOFT_ONLINE_URL + "consumers/"

BASE_URL = "https://graph.microsoft.com/v1.0/"
GRAPH_API_ENDPOINT = BASE_URL + "me/"

SCOPES = [
    "User.Read",
    "User.Export.all",
    "Files.ReadWrite",
]

