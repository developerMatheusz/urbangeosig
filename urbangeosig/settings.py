from pathlib import Path
from decouple import config, Csv
from dj_database_url import parse as db_url

BASE_DIR = Path(__file__).resolve().parent.parent

CELERY_BROKER_URL = "amqp://user:password@localhost/"

CELERY_TIMEZONE = "America/Cuiaba"

CELERY_TASK_TRACK_STARTED = True

CELERY_RESULT_BACKEND = "rpc://"

CELERY_RESULT_PERSISTENT = True

SECRET_KEY = config("SECRET_KEY")

DEBUG = config("DEBUG", default=False, cast=bool)

ALLOWED_HOSTS = config("ALLOWED_HOSTS", default=[], cast=Csv())

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.gis",
    "bootstrap5",
    "core",
    "register",
    "sigweb",
    "account",
    "django_extensions",
    "channels",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "urbangeosig.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "urbangeosig.wsgi.application"

DATABASES = {"default": config("DATABASE_URL", cast=db_url)}

DATABASES["default"]["ENGINE"] = "django.contrib.gis.db.backends.postgis"

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

LANGUAGE_CODE = "pt-br"

TIME_ZONE = "America/Cuiaba"

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

LOGIN_URL = "account:login"

LOGIN_REDIRECT_URL = "register:property_list"

LOGOUT_REDIRECT_URL = "core:index"

GEOSERVER = config("GEOSERVER")
