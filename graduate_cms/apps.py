#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ==================================================
# @Time : 2019-03-15 22:23
# @Author : ryuchen
# @Site :
# @File : enums.py
# @Desc :
# ==================================================

from django.apps import AppConfig


class GraduateConfig(AppConfig):
    name = 'graduate_cms'
    verbose_name = '研究生管理系统'
    verbose_name_plural = verbose_name
