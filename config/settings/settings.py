"""
Django settings for app project.
"""
import environ

ROOT_DIR = environ.Path(__file__) - 3
APPS_DIR = ROOT_DIR.path('app')

env = environ.Env()

READ_DOT_ENV_FILE = env.bool('DJANGO_READ_DOT_ENV_FILE', default=True)
if READ_DOT_ENV_FILE:
    env_file = str(ROOT_DIR.path('.env'))
    env.read_env(env_file)

SECRET_KEY = env('DJANGO_SECRET_KEY', default='}Ft=26Vc:otWU@5u`VQb?J:!dz_rZX7f_p=@7;}g%208iJ7#)`')

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
]

THIRD_PARTY_APPS = [
    'rest_framework',
    'django_extensions',
    'django_filters',
    'django.contrib.gis',
    'social_django',
]

LOCAL_APPS = [
    'app.users',
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS


class AllSameOriginMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        response['Access-Control-Allow-Origin'] = "http://localhost:4200"
        response['Access-Control-Allow-Credentials'] = "true"
        response["Access-Control-Allow-Headers"] = "Origin, X-Requested-With, Content-Type, Accept, X-CSRFToken, Cookie"
        return response


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'config.settings.settings.AllSameOriginMiddleware',
]

TIME_ZONE = 'Europe/Moscow'

LANGUAGE_CODE = 'ru-RU'

SITE_ID = 1

USE_I18N = True

USE_L10N = True

USE_TZ = True

ROOT_URLCONF = 'config.urls'

WSGI_APPLICATION = 'config.wsgi.application'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',
            ],
        },
    },
]

PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    'django.contrib.auth.hashers.BCryptPasswordHasher',
]

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

AUTHENTICATION_BACKENDS = [
    'social_core.backends.vk.VKOAuth2',
    'django.contrib.auth.backends.ModelBackend',
]

AUTH_USER_MODEL = 'users.User'

LOGIN_REDIRECT_URL = '/'

ADMIN_URL = r'^admin/'

ALLOWED_HOSTS = ["*"]

DEFAULTS = {
    'USE_SESSION_AUTH': False,
    'SECURITY_DEFINITIONS': {
        'basic': {
            'type': 'basic'
        }
    }
}

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'DEFAULT_FILTER_BACKENDS': ['rest_framework_filters.backends.RestFrameworkFilterBackend'],
    'PAGE_SIZE': 15
}

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': env('DATABASE_NAME'),
        'USER': env('DATABASE_USER'),
        'PASSWORD': env('DATABASE_PASSWORD'),
        'HOST': env('DATABASE_URL'),
        'PORT': '5432',
    }
}

SOCIAL_AUTH_POSTGRES_JSONFIELD = True

SOCIAL_AUTH_VK_OAUTH2_KEY = '6746864'
SOCIAL_AUTH_VK_OAUTH2_SECRET = 'I20xwVOuvGUWBSjdIQZa'

SOCIAL_AUTH_VK_OAUTH2_SCOPE = ['email']