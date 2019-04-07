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
from .views import MajorList, MajorDetail, AcademyList, AcademyDetail, ResearchList


urlpatterns = [
    url(r"^researches$", ResearchList.as_view(), name="research-list"),
    url(r"^majors$", MajorList.as_view(), name="major-list"),
    url(r"^major/(?P<pk>[0-9a-z]{8}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{12})$", MajorDetail.as_view(),
        name="major-detail"),
    url(r"^academies$", AcademyList.as_view(), name="academy-list"),
    url(r"^academy/(?P<pk>[0-9a-z]{8}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{12})$", AcademyDetail.as_view(),
        name="academy-detail"),
]
