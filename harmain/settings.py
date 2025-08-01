"""
Django settings for harmain project.

Generated by 'django-admin startproject' using Django 5.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-%x%eh#oai(1b1knwq_!nw7v+b^=*ywa$9_u(9wwy3#01_w&3t3'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["0.0.0.0","*"]

# DMQTT expects these FLAT settings:
MQTT_HOST = '129.212.141.20'
MQTT_PORT = 1883
MQTT_KEEPALIVE = 60
MQTT_USER = ''
MQTT_PASS = ''

# Optional topic prefix
MQTT_TOPIC_PREFIX = '#'

# Application definition

INSTALLED_APPS = [
    'baton',
    'daphne',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'auditlog', 
    'rest_framework',
    'django_filters',
    'import_export',
    'dmqtt',
    'channels',
    'smartlift',
    'baton.autodiscover',
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

REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend']
}

ROOT_URLCONF = 'harmain.urls'

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

WSGI_APPLICATION = 'harmain.wsgi.application'
ASGI_APPLICATION = 'harmain.asgi.application' 

# (Optional) Channel layer backend (for multi-instance or production use):
# CHANNEL_LAYERS = {
#     "default": {
#         "BACKEND": "channels.layers.InMemoryChannelLayer"
#     }
# }

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('127.0.0.1', 6379)],
        },
    },
}


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

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

BATON = {
    'SITE_HEADER': 'SmartLift Admin',
    'SITE_TITLE': 'SmartLift',
    'INDEX_TITLE': 'SmartLift Control Panel',
    'SUPPORT_HREF': 'https://tektronixllc.ae/contact/',
    'COPYRIGHT': 'copyright © 2025 <a href="https://tektronixllc.ae">Tektronix</a>', # noqa
    'POWERED_BY': '<a href="https://tektronixllc.ae">Tektronix</a>',
    'CONFIRM_UNSAVED_CHANGES': True,
    'SHOW_MULTIPART_UPLOADING': True,
    'ENABLE_IMAGES_PREVIEW': True,
    'CHANGELIST_FILTERS_IN_MODAL': True,
    'CHANGELIST_FILTERS_ALWAYS_OPEN': False,
    'CHANGELIST_FILTERS_FORM': True,
    'CHANGEFORM_FIXED_SUBMIT_ROW': True,
    'COLLAPSABLE_USER_AREA': False,
    'MENU_ALWAYS_COLLAPSED': False,
    'MENU_TITLE': 'Menu',
    'MESSAGES_TOASTS': False,
    'GRAVATAR_DEFAULT_IMG': 'retro',
    'GRAVATAR_ENABLED': True,
    'FORCE_THEME': None,
    'LOGIN_SPLASH': '/static/core/img/login-splash.png',
    'SEARCH_FIELD': {
        'label': 'Search contents...',
        'url': '/search/',
    },
    'BATON_CLIENT_ID': 'xxxxxxxxxxxxxxxxxxxx',
    'BATON_CLIENT_SECRET': 'xxxxxxxxxxxxxxxxxx',
    'IMAGE_PREVIEW_WIDTH': 200,
    # 'AI': {
    #     'MODELS': "myapp.foo.bar", # alternative to the below for lines, a function which returns the models dictionary
    #     'IMAGES_MODEL': AIModels.BATON_DALL_E_3,
    #     'VISION_MODEL': AIModels.BATON_GPT_4O_MINI,
    #     'SUMMARIZATIONS_MODEL': AIModels.BATON_GPT_4O_MINI,
    #     'TRANSLATIONS_MODEL': AIModels.BATON_GPT_4O,
    #     'ENABLE_TRANSLATIONS': True,
    #     'ENABLE_CORRECTIONS': True,
    #     'CORRECTION_SELECTORS': ["textarea", "input[type=text]:not(.vDateField):not([name=username]):not([name*=subject_location])"],
    #     'CORRECTIONS_MODEL': AIModels.BATON_GPT_3_5_TURBO,
    # },
    'MENU': (
        { 'type': 'title', 'label': 'main', 'apps': ('auth', ) },
        {
            'type': 'app',
            'name': 'auth',
            'label': 'Authentication',
            'icon': 'lock',
            'default_open': True,
            'models': (
                {
                    'name': 'user',
                    'label': 'Users'
                },
                {
                    'name': 'group',
                    'label': 'Groups'
                },
            )
        },
        { 'type': 'title', 'label': 'smartlift', 'apps': ('auth', ) },
        {
            'type': 'app',
            'name': 'smartlift',
            'label': 'SmartLift Logs',
            'icon': 'elevator',  # You can change this to any FontAwesome or Baton icon
            'models': (
                {
                    'icon': 'thermometer-half',
                    'name': 'liftenvironmentlog',
                    'label': 'Environment Logs'
                },
                {
                    'icon': 'sliders-h',
                    'name': 'liftcontrollog',
                    'label': 'Control Logs'
                },
                {
                    'icon': 'door-open',
                    'name': 'liftdooreventlog',
                    'label': 'Door Events'
                },
                {
                    'icon': 'users',
                    'name': 'liftoccupancylog',
                    'label': 'Occupancy Logs'
                },
                {
                    'icon': 'bolt',
                    'name': 'energymeterlog',
                    'label': 'Energy Meter'
                },
                {
                    'icon': 'level-up-alt',
                    'name': 'liftflooreventlog',
                    'label': 'Floor Events'
                },
            )
        },
        { 'type': 'title', 'label': 'auditlog', 'apps': ('auth', ) },
        {
            'type': 'app',
            'name': 'auditlog',
            'label': 'Audit Log',
            'icon': 'lock',
            'models': (
                {
                    'icon': 'clipboard-check',
                    'name': 'logentry',
                    'label': 'Log Entries'
                },
            )
        },
        { 'type': 'title', 'label': 'extras', 'apps': ('auth', ) },
        { 'type': 'title', 'label': 'Contents', 'apps': ('flatpages', ) },
        { 'type': 'model', 'label': 'Pages', 'name': 'flatpage', 'app': 'flatpages' },
        { 'type': 'free', 'label': 'Custom Link', 'url': 'http://www.google.it', 'perms': ('flatpages.add_flatpage', 'auth.change_user') },
        { 'type': 'free', 'label': 'My parent voice', 'children': [
            { 'type': 'model', 'label': 'A Model', 'name': 'mymodelname', 'app': 'myapp', 'icon': 'fa fa-gavel' },
            { 'type': 'free', 'label': 'Another custom link', 'url': 'http://www.google.it' },
        ] },
    )
}



# Internationalization
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Dubai'
USE_TZ = True

USE_I18N = True



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
