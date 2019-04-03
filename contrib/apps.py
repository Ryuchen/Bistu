#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ==================================================
# @Time : 2019-04-02 10:51 
# @Author : ryuchen
# @Site :  
# @File : apps.py 
# @Desc : 
# ==================================================

from django.apps import AppConfig


class GraduateConfig(AppConfig):
    name = 'contrib'
    verbose_name = '研究生管理系统'
    verbose_name_plural = verbose_name
