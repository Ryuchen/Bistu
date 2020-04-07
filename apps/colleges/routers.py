#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ==================================================
# @Time : 2020/4/6-15:18
# @Author : Ryuchen
# @Site : https://ryuchen.github.io
# @File : routers.py
# @Desc : 
# ==================================================
from django.urls import path, include

from django.views.generic import TemplateView

# Replace for vue-routers View template Routers
urlpatterns = [
    path("academy/", include([
        path("table/", TemplateView.as_view(template_name="client/pages/colleges/academy/index.html"), name="academy-table"),
        path("detail/", TemplateView.as_view(template_name="client/pages/colleges/academy/detail.html"), name="academy-detail"),
    ])),
    path("major/", include([
        path("table/", TemplateView.as_view(template_name="client/pages/colleges/major/index.html"), name="major-table"),
        path("detail/", TemplateView.as_view(template_name="client/pages/colleges/major/detail.html"), name="major-detail"),
    ])),
    path("research/", include([
        path("table/", TemplateView.as_view(template_name="client/pages/colleges/research/index.html"), name="research-table"),
        path("detail/", TemplateView.as_view(template_name="client/pages/colleges/research/detail.html"), name="research-detail"),
    ])),
    path("class/", include([
        path("table/", TemplateView.as_view(template_name="client/pages/colleges/class/index.html"), name="class-table"),
        path("detail/", TemplateView.as_view(template_name="client/pages/colleges/class/detail.html"), name="class-detail"),
    ])),
]

app_name = 'colleges'
