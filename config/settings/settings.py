import environ

ROOT_DIR = environ.Path(__file__) - 3
APPS_DIR = ROOT_DIR.path('app')

env = environ.Env()

READ_DOT_ENV_FILE = env.bool('DJANGO_READ_DOT_ENV_FILE', default=True)

if READ_DOT_ENV_FILE:
    env_file = str(ROOT_DIR.path('.env'))
    env.read_env(env_file)

DJANGO_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'django.contrib.admin',
    'django_admin_json_editor',
    'import_export',
]

THIRD_PARTY_APPS = [
    'crispy_forms',
    'rest_framework',
    'rest_framework_swagger',
    'django_extensions',
    'django_filters',
    'storages',
    'django.contrib.gis',
]

LOCAL_APPS = [
    'app.users'
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

FIXTURE_DIRS = (
    str(APPS_DIR.path('fixtures')),
)

ADMINS = [
    ("""Evgeny Rubanenko""", 'erubanenko@gmail.com'),
]

MANAGERS = ADMINS

TIME_ZONE = 'Europe/Moscow'

LANGUAGE_CODE = 'ru-RU'

SITE_ID = 1

USE_I18N = True

USE_L10N = True

USE_TZ = True

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            str(APPS_DIR.path('templates')),
        ],
        'OPTIONS': {
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            ],
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

CRISPY_TEMPLATE_PACK = 'bootstrap4'

STATIC_ROOT = env('DJANGO_STATIC_ROOT', default=str(ROOT_DIR('staticfiles')))

STATIC_URL = '/collected_static/'

STATICFILES_DIRS = [
]

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

MEDIA_ROOT = str(APPS_DIR('media'))

MEDIA_URL = '/media/'

ROOT_URLCONF = 'config.urls'

WSGI_APPLICATION = 'config.wsgi.application'

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
    'django.contrib.auth.backends.ModelBackend',
]

LOGIN_REDIRECT_URL = '/'

AUTOSLUG_SLUGIFY_FUNCTION = 'slugify.slugify'

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

CELERY_ALWAYS_EAGER = True

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'DEFAULT_FILTER_BACKENDS': ['rest_framework_filters.backends.RestFrameworkFilterBackend'],
    'PAGE_SIZE': 15
}

CKEDITOR_UPLOAD_PATH = "uploads_ck/"

DEBUG = True
TEMPLATES[0]['OPTIONS']['debug'] = DEBUG

SECRET_KEY = '}Ft=26Vc:otWU@5u`VQb?J:!dz_rZX7f_p=@7;}g%208iJ7#)`'

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'postgres',
        'PORT': '5432',
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_SSL = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 465
EMAIL_HOST_USER = 'erubanenko@gmail.com'
EMAIL_HOST_PASSWORD = 'diht2015'
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
