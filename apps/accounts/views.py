#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ==================================================
# @Time : 2019-04-02 10:46 
# @Author : ryuchen
# @Site :  
# @File : views.py 
# @Desc : 
# ==================================================
from django.contrib.sessions.models import Session
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt

from core.decorators.excepts import excepts
from core.exceptions.errors import ForbiddenError


@csrf_exempt
@excepts
def login_view(request):
    res = {
        "code": "00000000",
        "data": {
            "status": 200,
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
        else:
            res["data"]["currentAuthority"] = "user"
        return JsonResponse(res)
    else:
        raise ModuleNotFoundError


@csrf_exempt
@excepts
def logout_view(request):
    res = {
        "code": "00000000",
        "data": {
            "status": 200,
        }
    }
    if "username" in request.session:
        Session.objects.filter(session_key=request.user.userprofile.session_key).delete()
        del request.session['username']
        request.session.clear()
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

    if request.user:
        res["data"]["profile"] = {
            "name": request.user.username,
            "email": request.user.email,
            "avatar": 'https://gw.alipayobjects.com/zos/antfincdn/XAosXuNZyF/BiazfanxmamNRoxxVxka.png'
        }
    else:
        raise ForbiddenError("You need login first!")

    return JsonResponse(res)
