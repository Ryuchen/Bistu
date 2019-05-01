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
    layout = 'horizontal'
