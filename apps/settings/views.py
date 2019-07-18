#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ==================================================
# @Time : 2019-04-16 17:05 
# @Author : libin
# @Site :  
# @File : views.py 
# @Desc : 
# ==================================================
import os
import json

from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes

from django.conf import settings

from core.decorators.excepts import excepts
from core.definition.enums import *


@api_view(["GET"])
@authentication_classes(())
@permission_classes(())
@excepts
def application(request):
    res = {
        "code": "00000000",
        "data": {
            "status": 200,
        }
    }
    res['data']['app'] = {"name": "Bistu Postgraduate Manager System", "description": "Using for Bistu College CMS"}
    res['data']['menu'] = [
        {
            'text': '快捷中心',
            'group': True,
            'children': [
                {
                    'text': '工作总览',
                    'link': '/dashboard',
                    'icon': {'type': 'icon', 'value': 'appstore'},
                },
                {
                    'text': '快捷入口',
                    'link': '/dashboard',
                    'icon': {'type': 'icon', 'value': 'rocket'},
                    'shortcutRoot': True,
                },
            ],
        },
    ]
    return Response(res)


@api_view(["GET"])
@authentication_classes(())
@permission_classes(())
@excepts
def translation(request):
    request.encoding = 'utf-8'
    trans = request.GET.get("i18n", "zh-CN")
    res = {
        "code": "00000000",
        "data": {
            "status": 200,
            "default": trans
        }
    }
    with open(os.path.join(settings.TRANSLATE_DIRS, '{}.json'.format(trans)), "r") as translate:
        res['data']['translation'] = json.loads(translate.read())
    return Response(res)


@api_view(["GET"])
@authentication_classes(())
@permission_classes(())
@excepts
def definitions(request):
    res = dict()
    res['degree_choice'] = {tag.name: tag.value for tag in DegreeType}
    res['gender_choice'] = {tag.name: tag.value for tag in GenderType}
    res['title_choice'] = {tag.name: tag.value for tag in TitleType}
    res['political_choice'] = {tag.name: tag.value for tag in PoliticalType}
    res['status_choice'] = {tag.name: tag.value for tag in StudentStatusType}
    res['student_type'] = {tag.name: tag.value for tag in StudentLearnType}
    res['student_category'] = {tag.name: tag.value for tag in StudentCategoryType}
    res['cultivating_mode'] = {tag.name: tag.value for tag in CultivatingModeType}
    res['enrollment_category'] = {tag.name: tag.value for tag in EnrollmentCategoryType}
    res['special_program'] = {tag.name: tag.value for tag in SpecialProgramType}
    res['major_type'] = {tag.name: tag.value for tag in MajorType}
    res['major_degree'] = {tag.name: tag.value for tag in MajorDegree}
    return Response(res)


def trans_choice():
    res = dict()
    for item in [DegreeType, GenderType, TitleType, PoliticalType,
                 StudentStatusType, StudentStatusType, StudentCategoryType,
                 CultivatingModeType, EnrollmentCategoryType, SpecialProgramType, MajorType, MajorDegree]:
        for tag in item:
            res[tag.value] = tag.name
    return res
