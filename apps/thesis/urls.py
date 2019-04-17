#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ==================================================
# @Time : 2019-04-16 20:35 
# @Author : libin
# @Site :  
# @File : urls.py 
# @Desc : 
# ==================================================
from django.conf.urls import url
from .views import ThesisList, ThesisDetail


urlpatterns = [
    url(r"^thesises/$", ThesisList.as_view(), name="thesis-list"),
    url(r"^thesis/(?P<pk>[0-9a-z]{8}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{12})$", ThesisDetail.as_view(),
        name="thesis-detail"),
]