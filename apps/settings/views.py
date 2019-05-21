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
