#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ==================================================
# @Time : 2019-04-03 11:44 
# @Author : ryuchen
# @Site :  
# @File : admin.py
# @Desc : 
# ==================================================
import csv

from . import forms
from . import models

from django.contrib import admin
from django.http import HttpResponse

from django_admin_listfilter_dropdown.filters import DropdownFilter, RelatedDropdownFilter, ChoiceDropdownFilter


class StudentInline(admin.TabularInline):
    verbose_name = '指导学生'
    verbose_name_plural = verbose_name
    model = models.Student
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


class TutorAdmin(admin.ModelAdmin):

    def export_as_csv(self, request, queryset):
        field_names = [
            "教师编号", "教师姓名", "性别", "职称", "政治面貌",
            "所属学院", "教师邮箱", "教师电话", "最高学历", "毕业院校",
            "出生日期", "入职日期"
        ]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=教师表格.csv'
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            writer.writerow(obj.export_row())

        return response
    export_as_csv.short_description = "导出所选的 教师"

    form = forms.TutorForm
    inlines = [StudentInline]
    actions = ["export_as_csv"]
    fieldsets = (
        ('关联账户', {
            'fields': ('tut_user', )
        }),
        ('基本信息', {
            'fields': (
                'tut_number', 'tut_name', 'tut_avatar', 'tut_gender', 'tut_cardID',
                'tut_birth_day', 'tut_telephone', 'tut_title', 'tut_political',
                'tut_degree', 'tut_entry_day', 'tut_education'
            )
        }),
        ('学院资料', {
            'fields': ('tut_academy', ),
        })
    )
    list_filter = [
        ('tut_academy', RelatedDropdownFilter),
        ('tut_political', ChoiceDropdownFilter),
    ]
    list_display = (
        'tut_number', 'tut_name', 'get_gender', 'tut_telephone', 'tut_cardID',
        'get_degree', 'get_political', 'tut_birth_day', 'tut_entry_day'
    )

    empty_value_display = '--'
    change_list_template = 'admin/web/Tutor/change_list.html'


class StudentAdmin(admin.ModelAdmin):

    def export_as_csv(self, request, queryset):
        field_names = [
            "姓名", "学号", "考生号", "身份证件类型", "身份证号",
            "性别", "出生日期", "民族", "生源地", "是否农村学生",
            "政治面貌", "学院", "专业", "专业大类", "班级", "在学状态",
            "导师工号", "导师", "学生类型", "	学习形式", "学习阶段",
            "年级", "学制	", "入学日期", "培养方式", "录取类别",
            "国籍", "专项计划", "是否有固定收入", "是否欠缴学费",
            "档案是否转到学校", "毕业日期"
        ]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=学生表格.csv'
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            writer.writerow(obj.export_row())

        return response
    export_as_csv.short_description = "导出所选的 学生"

    form = forms.StudentForm
    actions = ["export_as_csv"]
    fieldsets = (
        ('关联账户', {
            'fields': ('stu_user',)
        }),
        ('基本信息', {
            'fields': (
                'stu_number', 'stu_name', 'stu_avatar', 'stu_gender', 'stu_is_regular_income',
                'stu_card_type', 'stu_cardID', 'stu_entrance_time', 'stu_graduation_time',
                'stu_telephone', 'stu_candidate_number', 'stu_birth_day', 'stu_is_village',
                'stu_nationality'
            )
        }),
        ('学院资料', {
            'fields': ('stu_academy', 'stu_major', 'stu_class', 'stu_tutor', 'stu_research'),
        }),
        ('档案信息', {
            'fields': (
                'stu_status', 'stu_gain_diploma', 'stu_gain_cert', 'stu_is_superb',
                'stu_is_volunteer', 'stu_is_adjust', 'stu_is_exemption', 'stu_is_archives',
                'stu_is_tuition_fees', 'stu_special_program', 'stu_political', 'stu_type',
                'stu_learn_type', 'stu_learn_status', 'stu_grade', 'stu_system', 'stu_cultivating_mode',
                'stu_enrollment_category', 'stu_thesis'
            ),
        }),
        ('中期考核', {
            'fields': ('stu_is_delay', 'stu_delay_reason', 'stu_mid_check'),
        }),
    )
    list_filter = [
        ('stu_special_program', ChoiceDropdownFilter),
        ('stu_cultivating_mode', ChoiceDropdownFilter),
        ('stu_enrollment_category', ChoiceDropdownFilter),
        ('stu_entrance_time', DropdownFilter),
        ('stu_academy', RelatedDropdownFilter),
        ('stu_major', RelatedDropdownFilter),
        ('stu_political', ChoiceDropdownFilter),
    ]
    list_display = (
        'stu_number', 'stu_name', 'get_gender', 'stu_telephone', 'stu_card_type', 'stu_cardID',
        'stu_birth_day', 'stu_nation', 'stu_source', 'stu_is_village', 'get_political',
        'get_stu_type', 'stu_entrance_time',
    )
    search_fields = ('stu_name',)
    empty_value_display = '--'
    change_list_template = 'admin/web/Student/change_list.html'


# Register your models here.
admin.site.register(models.Student, StudentAdmin)
admin.site.register(models.Tutor, TutorAdmin)
