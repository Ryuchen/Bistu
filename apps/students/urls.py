#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ==================================================
# @Time : 2019-04-02 20:21 
# @Author : ryuchen
# @Site :  
# @File : urls.py 
# @Desc : 
# ==================================================

from . import views

from django.conf.urls import url

urlpatterns = [
    url(r"^student/$", views.student_view, name="student"),
    url(r"^students/$", views.students_view, name="students"),
]
