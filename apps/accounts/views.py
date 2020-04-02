#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ==================================================
# @Time : 2019-04-02 10:46
# @Author : ryuchen
# @Site :
# @File : views.py
# @Desc :
# ==================================================
import logging

from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes

from core.exceptions.errors import *
from core.decorators.excepts import excepts

from contrib.colleges.models import Academy

log = logging.getLogger('default')


@api_view(["POST", "GET"])
@authentication_classes(())
@permission_classes(())
@excepts
def login_view(request):
    """
    用于账户登录接口
    :param request:
    :return:
    """
    if request.method == "POST":
        res = {
            "code": "00000000",
            "data": {}
        }
    
        username = request.POST.get('username')
        password = request.POST.get('password')
        remember = request.POST.get('remember')
    
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if remember:
                request.session.set_expiry(3600 * 24 * 7)
            return JsonResponse(res)
        else:
            raise AuthenticateError("Username or Password is incorrect!")
    else:
        return render(request, "client/pages/passport/login.html")


@api_view(["POST", "GET"])
@authentication_classes(())
@permission_classes(())
@excepts
def reset_view(request):
    """
    用于重置接口
    :param request:
    :return:
    """
    if request.method is "POST":
        res = {
            "code": "00000000",
            "data": {}
        }
        logout(request)
        return JsonResponse(res)
    else:
        return render(request, "client/pages/passport/reset.html")


@api_view(["GET"])
@authentication_classes(())
@permission_classes(())
@excepts
def logout_view(request):
    """
    用于账户登出接口
    :param request:
    :return:
    """
    logout(request)
    request.session.clear()
    return redirect("/")


@api_view(["POST", "GET"])
@authentication_classes(())
@permission_classes(())
@excepts
def register_view(request):
    """
    用户注册接口
    """
    if request.method is "POST":
        res = {
            "code": "00000000",
            "data": {}
        }
    else:
        return render(request, "client/pages/passport/register.html")


@api_view(["GET"])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
@excepts
def profile_view(request):
    """
    用于查询当前账户详情接口
    :param request:
    :return:
    """
    res = {
        "code": "00000000",
        "data": {}
    }

    user = User.objects.get(id=request.user.id)
    if user.is_superuser:
        res["data"]["profile"] = {
            "name": '{0}{1}'.format(user.first_name, user.last_name),
            "email": user.email,
            "avatar": 'https://gw.alipayobjects.com/zos/antfincdn/XAosXuNZyF/BiazfanxmamNRoxxVxka.png',
            "title": "你是当前系统的最高管理员",
            "group": "超级管理员",
            "academy": ""
        }
    else:
        if user.is_staff:
            academy = Academy.objects.filter(aca_user_id=user.id).first()
            res["data"]["profile"] = {
                "name": '{0}{1}'.format(user.first_name, user.last_name),
                "email": user.email,
                "avatar": 'https://gw.alipayobjects.com/zos/antfincdn/XAosXuNZyF/BiazfanxmamNRoxxVxka.png',
                "title": "你是{0}学院的管理员".format(academy.aca_cname),
                "group": "学院管理人员",
                "academy": academy.uuid
            }
        else:
            res["data"]["profile"] = {
                "name": '{0}{1}'.format(user.first_name, user.last_name),
                "email": user.email,
                "avatar": 'https://gw.alipayobjects.com/zos/antfincdn/XAosXuNZyF/BiazfanxmamNRoxxVxka.png',
                "title": "研究生导师",
                "group": "教师",
                "academy": ""
            }
    res["data"]["authority"] = list(user.groups.values_list('name', flat=True))
    res["data"]["permission"] = []
    for group in request.user.groups.all():
        res["data"]["permission"].extend(list(group.permissions.values_list('codename', flat=True)))
    res["data"]["permission"].extend(list(user.user_permissions.values_list('codename', flat=True)))

    return JsonResponse(res)
