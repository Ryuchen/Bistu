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


class GenderType(Enum):
    G1 = "男"
    G2 = "女"


GenderChoice = [(tag.name, tag.value) for tag in GenderType]


class TitleType(Enum):
    T1 = "讲师"
    T2 = "副教授"
    T3 = "教授"
    T4 = "副研究员"
    T5 = "研究员"
    T6 = "助教"


TitleChoice = [(tag.name, tag.value) for tag in TitleType]


class PoliticalType(Enum):
    P1 = "党员"
    P2 = "团员"
    P3 = "群众"
    P4 = "民主党派"


PoliticalChoice = [(tag.name, tag.value) for tag in PoliticalType]


class DegreeType(Enum):
    S1 = "博士"
    S2 = "硕士"
    S3 = "本科"


DegreeChoice = [(tag.name, tag.value) for tag in DegreeType]


class StudentStatusType(Enum):
    S1 = "在校"
    S2 = "离校"
    S3 = "留校"


StudentStatusChoice = [(tag.name, tag.value) for tag in StudentStatusType]


class MidCheckType(Enum):
    S1 = "合格"
    S2 = "跟踪"
    S3 = "不合格"


MidCheckChoice = [(tag.name, tag.value) for tag in MidCheckType]


class StudentLearnType(Enum):
    S1 = "硕士"
    S2 = "博士"
    S3 = "本硕连读"
    S4 = "硕博连读"
    S5 = "直博"


StudentLearnChoice = [(tag.name, tag.value) for tag in StudentLearnType]


class StudentCategoryType(Enum):
    S1 = "全日制"
    S2 = "非全日制"


StudentCategoryChoice = [(tag.name, tag.value) for tag in StudentCategoryType]


class CultivatingModeType(Enum):
    C1 = "专硕"
    C2 = "学硕"


CultivatingModeChoice = [(tag.name, tag.value) for tag in CultivatingModeType]


class EnrollmentCategoryType(Enum):
    E1 = "定向"
    E2 = "非定向"


EnrollmentCategoryChoice = [(tag.name, tag.value) for tag in EnrollmentCategoryType]


class SpecialProgramType(Enum):
    S1 = '无'
    S2 = '少数民族高层次骨干计划'
    S3 = '强军计划'
    S4 = '对口支援西部地区高校定向培养计划'
    S5 = '援藏计划'
    S6 = '农村学校教育硕士师资培养计划'
    S7 = '高校辅导员攻读思想政治教育专业硕士学位计划'
    S8 = '高校思想政治理论课教师攻读博士学位计划'
    S9 = '其他'


SpecialProgramChoice = [(tag.name, tag.value) for tag in SpecialProgramType]


class MajorType(Enum):
    C1 = "专业硕士学位"
    C2 = "学科硕士学位"


MajorTypeChoice = [(tag.name, tag.value) for tag in MajorType]


class MajorDegree(Enum):
    D1 = "哲学"
    D2 = "经济学"
    D3 = "法学"
    D4 = "教育学"
    D5 = "文学"
    D6 = "历史学"
    D7 = "理学"
    D8 = "工学"
    D9 = "农学"
    D10 = "医学"
    D11 = "军事学"
    D12 = "管理学"
    D13 = "艺术学"


MajorDegreeChoice = [(tag.name, tag.value) for tag in MajorDegree]


class ReformType(Enum):
    RT1 = "研究生教改项目立项"
    RT2 = "研究生教改论文发表"
    RT3 = "研究生课程教材出版"
    RT4 = "研究生教育相关获奖"
    RT5 = "精品/在线课程建设"
    RT6 = "研究生实践基地建设"
    RT7 = "研究生国际交流项目"


ReformTypeChoice = [(tag.name, tag.value) for tag in ReformType]
