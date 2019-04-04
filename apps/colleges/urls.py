#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ==================================================
# @Time : 2019-04-02 20:11 
# @Author : ryuchen
# @Site :  
# @File : urls.py 
# @Desc : 
# ==================================================
from django.conf.urls import url
from .views import MajorList, MajorDetail, AcademyList, AcademyDetail

urlpatterns = [
    url(r"^majors$", MajorList.as_view(), name="major-list"),
    url(r"^major/(?P<pk>\d+)$", MajorDetail.as_view(), name="major-detail"),
    url(r"^academies$", AcademyList.as_view(), name="academy-list"),
    url(r"^academy/(?P<pk>\d+)$", AcademyDetail.as_view(), name="academy-detail"),
]