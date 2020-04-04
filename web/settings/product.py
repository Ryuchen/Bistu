#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ==================================================
# @Time : 2019-07-29 15:10
# @Author : ryuchen
# @File : product.py
# @Desc :
# ==================================================
"""
Additional settings for custom project

So we can manage our settings benefit.
"""

from .base import *


INSTALLED_APPS += [
    'contrib.accounts.apps.AccountConfig',
    'contrib.colleges.apps.CollegeConfig',
    'contrib.education.apps.CultivateConfig',
    'contrib.notices.apps.NoticesConfig',
    'core',
    'django_filters',
    'import_export',
    'rest_framework',
    'corsheaders'
]


MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
] + MIDDLEWARE

# 跨域增加忽略
CORS_ORIGIN_ALLOW_ALL = True

# 默认可以使用的非标准请求头，需要使用自定义请求头时，就可以进行修改
CORS_ALLOW_HEADERS = (
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
)
# 默认请求方法
CORS_ALLOW_METHODS = (
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
)

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
    ),
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