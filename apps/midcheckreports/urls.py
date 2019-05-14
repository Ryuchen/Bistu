#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ==================================================
# @Time : 2019-05-06 15:30 
# @Author : libin
# @Site :  
# @File : urls.py 
# @Desc : 
# ==================================================
from django.conf.urls import url
from .views import MidCheckReportList, MidCheckReportUpload

urlpatterns = [
	url(r"^mid_check_reports/$", MidCheckReportList.as_view(), name="mid_check_report_list"),
	url(r"^mid_check_report_upload/$", MidCheckReportUpload.as_view(), name="mid_check_report-upload"),
]
