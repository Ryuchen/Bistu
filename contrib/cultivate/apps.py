#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ==================================================
# @Time : 2019-04-03 11:44 
# @Author : ryuchen
# @Site :  
# @File : apps.py 
# @Desc : 
# ==================================================
from django.apps import AppConfig


class CultivateConfig(AppConfig):
    name = 'contrib.cultivate'
    label = '培养管理'
    verbose_name = '培养管理'
    verbose_name_plural = verbose_name
