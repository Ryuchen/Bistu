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

from django.contrib.sessions.models import Session
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt

from core.decorators.excepts import excepts
from core.exceptions.errors import *

log = logging.getLogger('default')


@csrf_exempt
@excepts
def login_view(request):
    res = {
        "code": "00000000",
        "data": {
            "status": 200,
            "type": "account",
        }
    }
    if request.method != "POST":
        raise NotImplementedError

    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        user = User.objects.filter(username=username).first()
        if user.is_superuser:
            res["data"]["currentAuthority"] = "admin"
        elif user.is_staff:
            res["data"]["currentAuthority"] = "staff"
        else:
            res["data"]["currentAuthority"] = "teacher"
        return JsonResponse(res)
    else:
        raise AuthenticateError("Username or Password is incorrect!")


@csrf_exempt
@excepts
def logout_view(request):
    res = {
        "code": "00000000",
        "data": {
            "status": 200,
        }
    }
    logout(request)
    return JsonResponse(res)


@csrf_exempt
@excepts
def current_user_view(request):
    res = {
        "code": "00000000",
        "data": {
            "status": 200,
        }
    }
    if request.method != "GET":
        raise NotImplementedError

    if request.user.is_authenticated:
        if request.user.is_superuser:
            res["data"]["profile"] = {
                "name": request.user.username,
                "email": request.user.email,
                "avatar": 'https://gw.alipayobjects.com/zos/antfincdn/XAosXuNZyF/BiazfanxmamNRoxxVxka.png',
                "title": "你是当前系统的最高管理员",
                "group": "超级管理员"
            }
        else:
            if request.user.is_staff:
                res["data"]["profile"] = {
                    "name": request.user.username,
                    "email": request.user.email,
                    "avatar": 'https://gw.alipayobjects.com/zos/antfincdn/XAosXuNZyF/BiazfanxmamNRoxxVxka.png',
                    "title": "你是当前学院的管理员",
                    "group": "学院管理人员"
                }
            else:
                res["data"]["profile"] = {
                    "name": request.user.username,
                    "email": request.user.email,
                    "avatar": 'https://gw.alipayobjects.com/zos/antfincdn/XAosXuNZyF/BiazfanxmamNRoxxVxka.png',
                    "title": "研究生导师",
                    "group": "教师"
                }
        return JsonResponse(res)
    else:
        raise ForbiddenError("You need login first!")

