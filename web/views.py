#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ==================================================
# @Time : 2020/4/1-22:03
# @Author : Ryuchen
# @Site : https://ryuchen.github.io
# @File : views.py
# @Desc : 
# ==================================================
from django.shortcuts import render, redirect

from core.decorators.excepts import excepts


@excepts
def index(request):
    """
    登录页面router
    :param request:
    :return:
    """
    if request.user.is_authenticated:
        return render(request, "client/index.html")
    else:
        return redirect("/accounts/login")
