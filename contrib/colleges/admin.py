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

from contrib.accounts.models import Student

from django.contrib import admin
from django_admin_listfilter_dropdown.filters import DropdownFilter, ChoiceDropdownFilter


class ResearchInline(admin.TabularInline):
    verbose_name = '研究方向'
    verbose_name_plural = verbose_name
    model = models.Major.research.through
    fields = (
        'research',
    )
    readonly_fields = (
        'research',
    )
    can_delete = False
    show_change_link = False
    extra = 0


class ClassInline(admin.TabularInline):
    verbose_name = '专业班级'
    verbose_name_plural = verbose_name
    model = models.Class
    fields = (
        'cla_code', 'cla_name',
    )
    readonly_fields = (
        'cla_code', 'cla_name',
    )
    can_delete = False
    show_change_link = False
    extra = 0


class StudentInline(admin.TabularInline):
    verbose_name = '学生列表'
    verbose_name_plural = verbose_name
    model = Student
    fields = (
        'stu_number', 'stu_name', 'stu_telephone', 'stu_birth_day', 'stu_nation', 'stu_source', 'stu_entrance_time',
        'stu_academy', 'stu_major', 'stu_research'
    )
    readonly_fields = (
        'stu_number', 'stu_name', 'stu_telephone', 'stu_birth_day', 'stu_nation', 'stu_source', 'stu_entrance_time',
        'stu_academy', 'stu_major', 'stu_research'
    )
    can_delete = False
    show_change_link = False
    extra = 0


class MajorInline(admin.TabularInline):
    verbose_name = '学科专业'
    verbose_name_plural = verbose_name
    model = models.Academy.majors.through
    extra = 0


class ReformInline(admin.TabularInline):
    verbose_name = '教改项目'
    verbose_name_plural = verbose_name
    model = models.Academy.reforms.through
    extra = 0


class MajorsAdmin(admin.ModelAdmin):
    form = forms.MajorForm
    inlines = [
        ResearchInline,
        StudentInline,
        ClassInline
    ]
    list_filter = [
        ('maj_type', ChoiceDropdownFilter),
        ('maj_degree', ChoiceDropdownFilter),
        # for choice fields
        ('maj_first', DropdownFilter),
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
        ReformInline,
    ]
    list_display = (
        'aca_code', 'aca_cname', 'aca_ename', 'aca_phone', 'aca_fax', 'aca_href'
    )
    exclude = ('majors', 'reforms')
    empty_value_display = '--'


class ReformAdmin(admin.ModelAdmin):
    list_display = (
        'ref_name', 'ref_type', 'time'
    )
    empty_value_display = '--'


# Register your models here.
admin.site.register(models.Major, MajorsAdmin)
admin.site.register(models.Class, ClassAdmin)
admin.site.register(models.Academy, AcademyAdmin)
admin.site.register(models.Reform, ReformAdmin)
