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
    D4 = "本硕连读"
    D5 = "硕博连读"
    D6 = "直博"


class StatusChoice(Enum):
    S1 = "在校"
    S2 = "离校"
    S3 = "留校"


class LearnTypeChoice(Enum):
    L1 = "全日制"
    L2 = '非全日制'


class EducationChoice(Enum):
    L1 = '硕士'
    L2 = '博士'








