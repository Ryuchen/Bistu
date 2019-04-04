#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ==================================================
# @Time : 2019-04-02 10:23 
# @Author : ryuchen
# @Site :  
# @File : enums.py 
# @Desc : 
# ==================================================
from enum import Enum


class GenderChoice(Enum):
    G1 = "男"
    G2 = "女"


class TitleChoice(Enum):
    T1 = "讲师"
    T2 = "副教授"
    T3 = "教授"
    T4 = "副研究员"
    T5 = "研究员"
    T6 = "助教"


class PoliticalChoice(Enum):
    P1 = "党员"
    P2 = "团员"
    P3 = "群众"
    P4 = "民主党派"


class DegreeChoice(Enum):
    D1 = "博士"
    D2 = "硕士"
    D3 = "本科"


class StatusChoice(Enum):
    S1 = "在校"
    S2 = "离校"
    S3 = "留校"


class StudentType(Enum):
    S1 = "硕士"
    S2 = "博士"
    S3 = "本硕连读"
    S4 = "硕博连读"
    S5 = "直博"


class StudentCategory(Enum):
    S1 = "全日制"
    S2 = "非全日制"


class CultivatingMode(Enum):
    C1 = "专业学位"
    C2 = "专业学位"


class EnrollmentCategory(Enum):
    E1 = "定向"
    E2 = "非定向"


class SpecialProgram(Enum):
    S1 = '无'
    S2 = '少数民族高层次骨干计划'
    S3 = '强军计划'
    S4 = '对口支援西部地区高校定向培养计划'
    S5 = '援藏计划'
    S6 = '农村学校教育硕士师资培养计划'
    S7 = '高校辅导员攻读思想政治教育专业硕士学位计划'
    S8 = '高校思想政治理论课教师攻读博士学位计划'
    S9 = '其他'



