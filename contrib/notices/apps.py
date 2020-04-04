#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ==================================================
# @Time : 2020/4/4-16:56
# @Author : Ryuchen
# @Site : https://ryuchen.github.io
# @File : apps.py
# @Desc : 
# ==================================================
from django.apps import AppConfig


class NoticesConfig(AppConfig):
    name = 'contrib.notices'
    verbose_name = '消息通知'
    verbose_name_plural = verbose_name
