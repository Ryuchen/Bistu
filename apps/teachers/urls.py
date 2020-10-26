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
<<<<<<< HEAD
    url(r"^teachers/$", TutorList.as_view(), name="tutor-list"),
=======
    url(r"^teachers/$", TutorList.as_view(), name="teacher-list"),
>>>>>>> 9f27577387a6752b6bc33d0280deb765b5689ec5
    url(r"^teacher/(?P<pk>[0-9a-z]{8}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{12})$", TutorDetail.as_view(),
        name="tutor-detail"),
]
