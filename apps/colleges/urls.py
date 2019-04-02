#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ==================================================
# @Time : 2019-04-02 20:11 
# @Author : ryuchen
# @Site :  
# @File : urls.py 
# @Desc : 
# ==================================================
from . import views

from django.conf.urls import url

urlpatterns = [
    url(r"^research/$", views.research_view, name="research"),
    url(r"^researches/$", views.researches_view, name="researches"),
    url(r"^major/$", views.major_view, name="major"),
    url(r"^majors/$", views.majors_view, name="majors"),
    url(r"^academy/$", views.academy_view, name="academy"),
    url(r"^academies/$", views.academies_view, name="academies"),
]
