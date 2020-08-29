"""
Django settings for metaeducator project.

Generated by 'django-admin startproject' using Django 3.0.9.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os


# import pymysql
# pymysql.version_info = (1, 3, 13, "final", 0)
# pymysql.install_as_MySQLdb()

from django.contrib.messages import constants as messages
from django.core.mail import send_mail                                                                                                                                                                      

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '1$%=i(h0b8x_aau1kz^v_*u&22c6qeawwv#-z)d3)=)9a(y!-g'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
# APPEND_SLASH=False
ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'home.apps.HomeConfig',
    'blog.apps.BlogConfig',
    'youtube.apps.YoutubeConfig',
    'django.contrib.humanize',
]
                                                                        
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'metaeducator.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
             'libraries':{
            'extras': 'blog.templatestags.extras',
            'extra': 'youtube.templatestags.extra',

            }
        },
    },
]

WSGI_APPLICATION = 'metaeducator.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        #'ENGINE': 'django.db.backends.sqlite3',
        #'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'meta',
        'USER': 'root',
        'PORT': '3306',
        'PASSWORD': '',
        'HOST': 'localhost'

    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/
#Managing Media

STATIC_URL = '/static/'
MEDIA_ROOT=os.path.join(BASE_DIR, 'media')
MEDIA_URL='/media/'


MESSAGE_TAGS = {
    messages.ERROR : 'danger'
}


STATICFILES_DIRS=[
    os.path.join(BASE_DIR,"static")
]

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = os.environ.get('EMAIL_HOST')
# EMAIL_PORT = 587
# EMAIL_HOST_USER =os.environ.get('EMAIL_HOST_USER')
# EMAIL_HOST_PASSWORD =os.environ.get('EMAIL_HOST_PASSWORD')
# DEFAULT_FROM_EMAIL =os.environ.get('EMAIL_HOST_USER')
# EMAIL_USE_TLS = True


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER ='metaeducatorshubu@gamil.com'
EMAIL_HOST_PASSWORD ='shreyaji07'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

# DEFAULT_FROM_EMAIL= 'metaeducatorshubu@gmail.com'

# EMAIL_USE_SSL = False

# STATICFILES_DIRS=[
#     "static/"
# ]