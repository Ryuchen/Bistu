#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ==================================================
# @Time : 2019-04-02 20:21 
# @Author : ryuchen
# @Site :  
# @File : views.py 
# @Desc : 
# ==================================================
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from core.decorators.excepts import excepts
from core.exceptions.errors import ForbiddenError


@csrf_exempt
@excepts
def student_view(request):
    res = {
        "code": "00000000",
        "data": {
            "status": 200,
        }
    }
    return JsonResponse(res)


@csrf_exempt
@excepts
def students_view(request):
    res = {
        "code": "00000000",
        "data": {
            "status": 200,
        }
    }
    return JsonResponse(res)
