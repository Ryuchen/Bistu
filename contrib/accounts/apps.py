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


class AccountConfig(AppConfig):
    name = 'contrib.accounts'
    label = '用户管理'
    verbose_name = '用户管理'
    verbose_name_plural = 1

