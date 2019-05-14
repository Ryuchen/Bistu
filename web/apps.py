#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ==================================================
# @Time : 2019-05-01 11:13 
# @Author : ryuchen
# @Site :  
# @File : apps.py 
# @Desc : 
# ==================================================

from suit.apps import DjangoSuitConfig


class SuitConfig(DjangoSuitConfig):
    verbose_name = '研究生信息管理系统'
    layout = 'horizontal'
    form_inlines_hide_original = True
