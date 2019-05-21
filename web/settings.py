"""
Django settings for web project.

Generated by 'django-admin startproject' using Django 2.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '48&)+x#5l9v^5#f10$ebbb77%0q-&3de%lr8v6&it*ts6ql^2-'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition
INSTALLED_APPS = [
    'simpleui',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'contrib.accounts.apps.AccountConfig',
    'contrib.colleges.apps.CollegeConfig',
    'contrib.education.apps.CultivateConfig',
    'core',
    'django_filters',
    'import_export',
]

MIDDLEWARE = [
    'core.middleware.disableCSRFToken.DisableCSRF',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
]

ROOT_URLCONF = 'web.urls'

WSGI_APPLICATION = 'web.wsgi.application'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

CSRF_COOKIE_SECURE = True

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'zh-Hans'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

# Media files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/media-files/

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Logging config
# https://docs.djangoproject.com/en/2.1/topics/logging/

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(threadName)s:%(thread)d] [%(name)s:%(lineno)d] [%(levelname)s]- %(message)s'
        },
    },
    'handlers': {
        'default': {
            'level': 'INFO',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': os.path.join(BASE_DIR, "logs", "web.log"),
            'when': 'MIDNIGHT',
            'interval': 1,
            'backupCount': 7,
            'formatter': 'standard',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'standard',
        }
    },
    'loggers': {
        'default': {
            'handlers': ['default', 'console'],
            'level': 'DEBUG',
            'propagate': True,
        }
    }
}

REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend',),
    'DEFAULT_PAGINATION_CLASS': ('rest_framework.pagination.LimitOffsetPagination',),
    'PAGE_SIZE': 20,
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.MultiPartParser',
        'rest_framework.parsers.FileUploadParser'
    ),
}

SESSION_EXPIRE_AT_BROWSER_CLOSE = True


# SimpleUI settings
# https://github.com/newpanjing/simpleui/blob/master/QUICK.md
SIMPLEUI_HOME_INFO = False

SIMPLEUI_CONFIG = {
    'system_keep': False,
    'menus': [
        {
            'app': 'auth',
            'name': '账户管理',
            'icon': 'fas fa-user-shield',
            'models': [
                {
                    'name': '用户',
                    'icon': 'fa fa-user',
                    'url': 'auth/user/'
                },
                {
                    'name': '用户组',
                    'icon': 'fa fa-users-cog',
                    'url': 'auth/group/'
                }
            ]
        },
        {
            'app': 'accounts',
            'name': '学生管理',
            'icon': 'fa fa-graduation-cap',
            'url': 'accounts/student/'
        },
        {
            'app': 'accounts',
            'name': '教师管理',
            'icon': 'fa fa-id-card',
            'url': 'accounts/tutor/'
        },
        {
            'app': 'colleges',
            'name': '学院管理',
            'icon': 'fa fa-university',
            'models': [
                {
                    'name': '学院',
                    'icon': 'fa fa-university',
                    'url': 'colleges/academy/'
                },
                {
                    'name': '专业',
                    'icon': 'fa fa-university',
                    'url': 'colleges/major/'
                },
                {
                    'name': '班级',
                    'icon': 'fa fa-university',
                    'url': 'colleges/class/'
                },
                {
                    'name': '教改',
                    'icon': 'fa fa-university',
                    'url': 'colleges/reform/'
                },
                {
                    'name': '统计',
                    'icon': 'fa fa-university',
                    'url': 'colleges/reformresults/'
                }
            ]
        },
        {
            'app': 'education',
            'name': '教学管理',
            'icon': 'fas fa-book',
            'models': [
                {
                    'name': '论文',
                    'icon': 'fa fa-book',
                    'url': 'education/thesis/'
                },
                {
                    'name': '论文查重',
                    'icon': 'fa fa-book',
                    'url': 'education/thesisplacheck/'
                },
                {
                    'name': '论文盲审',
                    'icon': 'fa fa-book',
                    'url': 'education/thesisblindreview/'
                },
            ]
        }
    ]
}
