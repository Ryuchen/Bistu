#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ==================================================
# @Time : 2019-04-03 11:44 
# @Author : ryuchen
# @Site :  
# @File : admin.py
# @Desc : 
# ==================================================
from . import models

from django.contrib import admin


class CultivateAdmin(admin.ModelAdmin):
    empty_value_display = '--'


# Register your models here.
admin.site.register(models.Thesis, CultivateAdmin)
