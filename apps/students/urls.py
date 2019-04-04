#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ==================================================
# @Time : 2019-04-03 20:11
# @Author : libin
# @Site :
# @File : views.py
# @Desc :
# ==================================================
from django.conf.urls import url
from apps.students.views import StudentDetail, StudentList

urlpatterns = [
	url(r"^students$", StudentList.as_view(), name="student-list"),
	url(r"^student/(?P<pk>\d+)$", StudentDetail.as_view(), name="student-detail")
]