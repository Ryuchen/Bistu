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
	url(r"^application/$", views.application, name="settings-application"),
	url(r"^translation/$", views.translation, name="settings-translation"),
	url(r"^definitions/$", views.definitions, name="common-settings"),
]
