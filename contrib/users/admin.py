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


class UsersAdmin(admin.ModelAdmin):
    empty_value_display = '--'


# Register your models here.
admin.site.register(models.Education, UsersAdmin)
admin.site.register(models.Class, UsersAdmin)
admin.site.register(models.Tutor, UsersAdmin)
admin.site.register(models.Student, UsersAdmin)
