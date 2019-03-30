#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ==================================================
# @Time : 2019-03-15 22:23
# @Author : ryuchen
# @Site :
# @File : enums.py
# @Desc :
# ==================================================

from .models import *
from django.contrib import admin


class BistuCMSAdmin(admin.ModelAdmin):
    empty_value_display = '--'


class ResearchAdmin(admin.ModelAdmin):
    empty_value_display = '--'
    list_display = ['res_name']
    ordering = ['res_name']


class MajorAdmin(admin.ModelAdmin):
    empty_value_display = '--'
    list_display = ['maj_code', 'maj_name']
    ordering = ['maj_code']


# Register your models here.
admin.site.register(Research, ResearchAdmin)
admin.site.register(Major, MajorAdmin)
admin.site.register(Academy, BistuCMSAdmin)
admin.site.register(Education, BistuCMSAdmin)
admin.site.register(Tutor, BistuCMSAdmin)
admin.site.register(Class, BistuCMSAdmin)
admin.site.register(Thesis, BistuCMSAdmin)
admin.site.register(Student, BistuCMSAdmin)









