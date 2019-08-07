#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ==================================================
# @Time : 2019-08-03 22:10
# @Author : ryuchen
# @File : views.py.py
# @Desc :
# ==================================================
from django.contrib.admin import AdminSite
from django.template.response import TemplateResponse


def index(request):
    """
    用于账户登录接口
    :param request:
    :return:
    """
    site = AdminSite()
    app_list = site.get_app_list(request)

    context = {
        **site.each_context(request),
        'title': site.index_title,
        'app_list': app_list,
        **({}),
    }

    request.current_app = site.name

    print(context)

    return TemplateResponse(request, 'web/index.html', context)
