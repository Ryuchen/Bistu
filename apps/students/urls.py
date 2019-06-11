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
from apps.students.views import StudentDetail, StudentList, StudentStatistics
from . import views

urlpatterns = [
	url(r"^students/$", StudentList.as_view(), name="student-list"),
	url(r"^student/(?P<pk>[0-9a-z]{8}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{12})$", StudentDetail.as_view(), name="student-detail"),
	url(r"^statistics/$", StudentStatistics.as_view(), name="student-statistics"),
	url(r"^create_xls/$", views.create_xls, name="create_xls"),
	url(r"^trending/$", views.academies_enroll_statistic, name="student-enroll-trending"),
]
