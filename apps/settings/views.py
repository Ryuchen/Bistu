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

from django.urls import reverse
from django.conf import settings

from core.decorators.excepts import excepts
from core.definition.enums import *


@api_view(["GET"])
@authentication_classes(())
@permission_classes(())
@excepts
def accesslimit(request):
    res = {
        "code": "00000000",
        "data": {
            'menus': [
                {
                    "key": reverse('student-list'),
                    "title": "学生管理",
                    "name": "students",
                    "role": ["admin", "staff", "teacher"],
                    "icon": "appstore"
                },
                {
                    "key": reverse('teacher-list'),
                    "title": "教师管理",
                    "name": "teachers",
                    "role": ["admin", "staff", "teacher"],
                    "icon": "appstore"
                },
                {
                    "key": '2',
                    "title": "学院管理",
                    "name": "colleges",
                    "role": ["admin", "staff", "teacher"],
                    "icon": "appstore",
                    "subs": [
                        {
                            "key": reverse('colleges:academy-table'),
                            "title": "学院列表",
                            "name": "aca-list",
                            "role": ["admin", "staff", "teacher"],
                            "icon": "appstore",
                        },
                        {
                            "key": reverse('colleges:major-table'),
                            "title": "专业领域",
                            "name": "maj-list",
                            "role": ["admin", "staff", "teacher"],
                            "icon": "appstore",
                        },
                        {
                            "key": reverse('colleges:research-table'),
                            "title": "研究方向",
                            "name": "res-list",
                            "role": ["admin", "staff", "teacher"],
                            "icon": "appstore",
                        },
                        {
                            "key": reverse('colleges:class-table'),
                            "title": "班级管理",
                            "name": "cls-list",
                            "role": ["admin", "staff", "teacher"],
                            "icon": "appstore",
                        }
                    ]
                },
            ]
        }
    }
    return Response(res)


@api_view(["GET"])
@authentication_classes(())
@permission_classes(())
@excepts
def application(request):
    res = {
        "code": "00000000",
        "data": {
            'app': {
                "name": "Postgraduate Manager System",
                "description": "Using for College CMS"
            },
            'auth': {
                "name": "Ryuchen",
                "year": "2018",
                "href": "https://github.com/Ryuchen"
            },
            'toolbox': {
                "lock": {
                    "enable": True,
                    "verify": "email"
                },
                "github": {
                    "enable": True,
                    "link": "https://github.com/ryuchen"
                },
                "search": {
                    "enable": True,
                },
                "notice": {
                    "enable": True,
                },
                "utility": {
                    "enable": True,
                }
            }
        }
    }
    return Response(res)


@api_view(["GET"])
@authentication_classes(())
@permission_classes(())
@excepts
def translation(request):
    res = {
        "code": "00000000",
        "data": {}
    }
    request.encoding = 'utf-8'
    trans = request.GET.get("i18n", "zh-CN")
    res['data']['default'] = trans
    with open(os.path.join(settings.TRANSLATE_DIRS, '{}.json'.format(trans)), "r") as translate:
        res['data']['translation'] = json.loads(translate.read())
    return Response(res)


@api_view(["GET"])
@authentication_classes(())
@permission_classes(())
@excepts
def definitions(request):
    res = {
        "code": "00000000",
        "data": {}
    }
    res['data']['degree_choice'] = {tag.name: tag.value for tag in DegreeType}
    res['data']['gender_choice'] = {tag.name: tag.value for tag in GenderType}
    res['data']['title_choice'] = {tag.name: tag.value for tag in TitleType}
    res['data']['political_choice'] = {tag.name: tag.value for tag in PoliticalType}
    res['data']['status_choice'] = {tag.name: tag.value for tag in StudentStatusType}
    res['data']['student_type'] = {tag.name: tag.value for tag in StudentLearnType}
    res['data']['student_category'] = {tag.name: tag.value for tag in StudentCategoryType}
    res['data']['cultivating_mode'] = {tag.name: tag.value for tag in CultivatingModeType}
    res['data']['enrollment_category'] = {tag.name: tag.value for tag in EnrollmentCategoryType}
    res['data']['special_program'] = {tag.name: tag.value for tag in SpecialProgramType}
    res['data']['major_type'] = {tag.name: tag.value for tag in MajorType}
    res['data']['major_degree'] = {tag.name: tag.value for tag in MajorDegree}
    return Response(res)


def trans_choice():
    res = dict()
    for item in [DegreeType, GenderType, TitleType, PoliticalType,
                 StudentStatusType, StudentStatusType, StudentCategoryType,
                 CultivatingModeType, EnrollmentCategoryType, SpecialProgramType, MajorType, MajorDegree]:
        for tag in item:
            res[tag.value] = tag.name
    return res
