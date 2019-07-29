#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ==================================================
# @Time : 2019-07-24 15:22
# @Author : ryuchen
# @File : views.py
# @Desc :
# ==================================================
import logging

from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes

from core.decorators.excepts import excepts

from contrib.accounts.models import Student, Tutor
from contrib.colleges.models import Academy

log = logging.getLogger('default')


@api_view(["GET"])
@permission_classes([IsAuthenticated])
@excepts
def total_view(request):
    """
    用于查询当前账户详情接口
    :param request:
    :return:
    """
    res = {
        "code": "00000000",
        "data": {}
    }

    res['data']['student'] = Student.objects.count()
    res['data']['teacher'] = Tutor.objects.count()
    res['data']['academy'] = Academy.objects.count()

    return JsonResponse(res)
