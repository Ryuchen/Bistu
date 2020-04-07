#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ==================================================
# @Time : 2019-04-02 10:46 
# @Author : ryuchen
# @Site :  
# @File : urls.py 
# @Desc : 
# ==================================================
from . import views

from django.conf.urls import url

urlpatterns = [
    url(r"^login/$", views.login_view, name="login"),
    url(r"^reset/$", views.reset_view, name="reset"),
    url(r"^logout/$", views.logout_view, name="logout"),
    url(r"^profile/$", views.profile_view, name="profile"),
    url(r"^register/$", views.register_view, name="register"),
]

app_name = 'accounts'
