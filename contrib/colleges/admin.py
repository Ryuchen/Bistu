#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ==================================================
# @Time : 2019-04-03 11:44 
# @Author : ryuchen
# @Site :  
# @File : admin.py
# @Desc : 
# ==================================================
from . import forms
from . import models

from django.contrib import admin


class ResearchInline(admin.TabularInline):
    verbose_name = '研究方向'
    verbose_name_plural = verbose_name
    model = models.Major.research.through
    extra = 0


class MajorInline(admin.TabularInline):
    verbose_name = '学科专业'
    verbose_name_plural = verbose_name
    model = models.Academy.majors.through
    extra = 0


class ResearchesAdmin(admin.ModelAdmin):
    inlines = [
        ResearchInline,
    ]
    empty_value_display = '--'


class MajorsAdmin(admin.ModelAdmin):
    form = forms.MajorForm
    inlines = [
        ResearchInline
    ]
    list_display = (
        'maj_code', 'maj_name', 'get_major_type', 'maj_first', 'maj_second',
        'maj_setup_time', 'get_major_degree'
    )
    exclude = ('research', )
    empty_value_display = '--'


class ClassAdmin(admin.ModelAdmin):
    list_display = ('cla_code', 'cla_name')
    empty_value_display = '--'


class AcademyAdmin(admin.ModelAdmin):
    inlines = [
        MajorInline,
    ]
    list_display = (
        'aca_code', 'aca_cname', 'aca_ename', 'aca_phone', 'aca_fax', 'aca_href'
    )
    exclude = ('majors', )
    empty_value_display = '--'


class CommonAdmin(admin.ModelAdmin):
    empty_value_display = '--'


# Register your models here.
admin.site.register(models.Research, ResearchesAdmin)
admin.site.register(models.Major, MajorsAdmin)
admin.site.register(models.Class, ClassAdmin)
admin.site.register(models.Academy, AcademyAdmin)
admin.site.register(models.Reform, CommonAdmin)
