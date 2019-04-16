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
	url(r"^settings/$", views.common_settings, name="common-settings"),
]