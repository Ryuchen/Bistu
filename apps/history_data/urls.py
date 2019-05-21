#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ==================================================
# @Time : 2019-05-20 17:38 
# @Author : libin
# @Site :  
# @File : urls.py 
# @Desc : 
# ==================================================
from django.conf.urls import url

from . import views

urlpatterns = [
	url(r"^upload/$", views.upload_history_data, name="history_data-upload"),
]