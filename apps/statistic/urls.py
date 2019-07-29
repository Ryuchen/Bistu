#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ==================================================
# @Time : 2019-07-24 15:22
# @Author : ryuchen
# @File : urls.py
# @Desc :
# ==================================================
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r"^total/$", views.total_view, name="statistic-application"),
]
