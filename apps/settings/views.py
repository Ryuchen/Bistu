#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ==================================================
# @Time : 2019-04-16 17:05 
# @Author : libin
# @Site :  
# @File : views.py 
# @Desc : 
# ==================================================
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt

from core.definition.enums import *


@api_view(["GET"])
@csrf_exempt
def common_settings(request):
    res = dict()
    res['degree_choice'] = {tag.name: tag.value for tag in DegreeChoice}
    res['gender_choice'] = {tag.name: tag.value for tag in GenderChoice}
    res['title_choice'] = {tag.name: tag.value for tag in TitleChoice}
    res['political_choice'] = {tag.name: tag.value for tag in PoliticalChoice}
    res['status_choice'] = {tag.name: tag.value for tag in StatusChoice}
    res['student_type'] = {tag.name: tag.value for tag in StudentType}
    res['student_category'] = {tag.name: tag.value for tag in StudentCategory}
    res['cultivating_mode'] = {tag.name: tag.value for tag in CultivatingMode}
    res['enrollment_category'] = {tag.name: tag.value for tag in EnrollmentCategory}
    res['special_program'] = {tag.name: tag.value for tag in SpecialProgramChoice}
    res['major_type'] = {tag.name: tag.value for tag in MajorType}
    res['major_degree'] = {tag.name: tag.value for tag in MajorDegree}
    return Response(res)


def trans_choice():
    res = dict()
    for item in [DegreeChoice, GenderChoice, TitleChoice, PoliticalChoice, StatusChoice, StudentCategory,
                 CultivatingMode, EnrollmentCategory, SpecialProgramChoice, MajorType, MajorDegree, StudentType]:
        for tag in item:
            res[tag.value] = tag.name
    return res
