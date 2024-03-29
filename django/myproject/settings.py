"""
Django settings for myproject project.

Generated by 'django-admin startproject' using Django 3.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

from pathlib import Path

import environ
import email.utils

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False),
    TIME_ZONE=(str, "UTC"),
)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# reading .env file
environ.Env.read_env(str(BASE_DIR.parent / ".env"))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# Raises django's ImproperlyConfigured exception if SECRET_KEY not in
# os.environ
SECRET_KEY = env("SECRET_KEY")

# False if not in os.environ
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env("DEBUG")

ALLOWED_HOSTS = ["localhost"] + env("ALLOWED_HOSTS").split(",")
CSRF_TRUSTED_ORIGINS = env("CSRF_TRUSTED_ORIGINS").split(",")


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # Add gis module for geospatial projects
    #'django.contrib.gis',
    # Include this to build REST APIs
    "rest_framework",
    # Include this to build on top of Boostrap 5
    "django_bootstrap5",
    # Include this to add history to models
    "simple_history",
    # Include extras to make working with Django's CLI etc easier
    "django_extensions",
    # Uncomment the below line and replace 'myapp' with the name of your app
    #'myapp',
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    # Include this to add history to models
    "simple_history.middleware.HistoryRequestMiddleware",
]

ROOT_URLCONF = "myproject.urls"

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

WSGI_APPLICATION = "myproject.wsgi.application"


LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {"class": "logging.StreamHandler"},
    },
    "loggers": {
        "root": {"handlers": ["console"], "level": "INFO"},
    },
}

# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

DATABASES = {
    "default": {
        # Use sqlite by default
        "ENGINE": env("DB_ENGINE", default="django.db.backends.sqlite3"),
        # Use spatialite for spatial projects
        #'ENGINE': env("DB_ENGINE", default='django.contrib.gis.db.backends.spatialite'),
        # Use regular Postgres in production
        #'ENGINE': env("DB_ENGINE", default='django.db.backends.postgresql_psycopg2'),
        # Use PostGIS in production for spatial projects
        #'ENGINE': env("DB_ENGINE", default='django.contrib.gis.db.backends.postgis'),
        "NAME": env(
            "POSTGRES_DB",
            default=env("DB_NAME", default=str(BASE_DIR.parent / "db/db.sqlite3")),
        ),
        "USER": env("POSTGRES_USER", default="nobody"),
        "PASSWORD": env("POSTGRES_PASSWORD", default="insecure"),
        "HOST": env("POSTGRES_HOST", default="localhost"),
        "PORT": env("POSTGRES_PORT", default="5432"),
    }
}


# Password validation
# https://docs.djangoproject.com/en/dev/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = env("TIME_ZONE")

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/

STATIC_URL = "/static/"
STATIC_ROOT = str(BASE_DIR.parent / "static")
MEDIA_URL = "/media/"
MEDIA_ROOT = str(BASE_DIR.parent / "media")

# Default primary key field type
# https://docs.djangoproject.com/en/dev/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

EMAIL_BACKEND = env(
    "EMAIL_BACKEND", default="django.core.mail.backends.console.EmailBackend"
)
EMAIL_HOST = env("EMAIL_HOST", default="mail")
EMAIL_PORT = env("EMAIL_PORT", default="587")
EMAIL_HOST_USER = env("EMAIL_HOST_USER", default="")
EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD", default="")
EMAIL_USE_TLS = env("EMAIL_USE_TLS", default=False)
EMAIL_USE_SSL = env("EMAIL_USE_SSL", default=False)
EMAIL_TIMEOUT = env("EMAIL_TIMEOUT", default=None)
EMAIL_SSL_KEYFILE = env("EMAIL_SSL_KEYFILE", default=None)
EMAIL_SSL_CERTFILE = env("EMAIL_SSL_CERTFILE", default=None)
DEFAULT_FROM_EMAIL = env("DEFAULT_FROM_EMAIL", default="webmaster@localhost")
SERVER_EMAIL = env("SERVER_EMAIL", default=DEFAULT_FROM_EMAIL)
EMAIL_FILE_PATH = env("EMAIL_FILE_PATH", default="/tmp/django-messages")

ADMINS = email.utils.getaddresses(["To: %s" % (env("ADMINS", default=""))])
