#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ==================================================
# @Time : 2019-04-16 17:20 
# @Author : libin
# @Site :  
# @File : urls.py 
# @Desc : 
# ==================================================
from django.conf.urls import url
from . import views

urlpatterns = [
	url(r"^accesslimit/$", views.accesslimit, name="accesslimit"),
	url(r"^application/$", views.application, name="application"),
	url(r"^translation/$", views.translation, name="translation"),
	url(r"^definitions/$", views.definitions, name="definitions"),
]

app_name = 'settings'
