#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ==================================================
# @Time : 2019-04-02 10:50 
# @Author : ryuchen
# @Site :  
# @File : admins.py 
# @Desc : 
# ==================================================

from contrib.academy.models import *
from contrib.cultivate.models import *
from contrib.users.models import *

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
