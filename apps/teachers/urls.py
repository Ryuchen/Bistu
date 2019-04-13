#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ==================================================
# @Time : 2019-04-02 20:22 
# @Author : ryuchen
# @Site :  
# @File : urls.py 
# @Desc : 
# ==================================================
from django.conf.urls import url
from .views import TutorList, TutorDetail


urlpatterns = [
    url(r"^teachers/$", TutorList.as_view(), name="tutor-list"),
    url(r"^teacher/(?P<pk>[0-9a-z]{32})$", TutorDetail.as_view(),
        name="tutor-detail"),
    # url(r"^teacher/(?P<pk>[0-9a-z]{8}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{12})$", TutorDetail.as_view(),
    #     name="tutor-detail"),
]
