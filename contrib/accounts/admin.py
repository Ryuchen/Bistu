#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ==================================================
# @Time : 2019-04-03 11:44 
# @Author : ryuchen
# @Site :  
# @File : admin.py
# @Desc : 
# ==================================================
from import_export import resources
from import_export.fields import Field
from import_export.admin import ExportActionMixin

from . import forms
from . import models

from django.contrib import admin
from django.contrib.auth.models import User, Group


class StudentInline(admin.TabularInline):
    verbose_name = '指导学生'
    verbose_name_plural = verbose_name
    model = models.Student
    fields = (
        'stu_number', 'stu_name', 'stu_telephone', 'stu_nation', 'stu_source', 'stu_entrance_time',
        'stu_academy', 'stu_major'
    )
    readonly_fields = (
        'stu_number', 'stu_name', 'stu_telephone', 'stu_nation', 'stu_source', 'stu_entrance_time',
        'stu_academy', 'stu_major'
    )
    can_delete = False
    extra = 0


class TutorResource(resources.ModelResource):
    tut_number = Field(attribute='tut_number', column_name='教师编号')
    tut_name = Field(attribute='tut_name', column_name='教师姓名')
    get_gender = Field(attribute='get_gender', column_name='性别')
    get_title = Field(attribute='get_title', column_name='职称')
    get_political = Field(attribute='get_political', column_name='政治面貌')
    tut_aca_cname = Field(attribute='tut_academy__aca_cname', column_name='所属学院')
    tut_email = Field(attribute='tut_user__email', column_name='教师邮箱')
    tut_telephone = Field(attribute='tut_telephone', column_name='教师电话')
    get_degree = Field(attribute='get_degree', column_name='最高学历')
    tut_edu_school_name = Field(attribute='tut_education__edu_school_name', column_name='毕业院校')
    tut_birth_day = Field(attribute='tut_birth_day', column_name='出生日期')
    tut_entry_day = Field(attribute='tut_entry_day', column_name='入职日期')

    class Meta:
        model = models.Tutor
        fields = (
            'tut_number', 'tut_name', 'get_gender', 'get_title', 'get_political',
            'tut_aca_cname', 'tut_email', 'tut_telephone', 'get_degree',
            'tut_edu_school_name', 'tut_birth_day', 'tut_entry_day'
        )


@admin.register(models.Tutor)
class TutorAdmin(ExportActionMixin, admin.ModelAdmin):
    resource_class = TutorResource
    form = forms.TutorForm
    inlines = [StudentInline]
    fieldsets = (
        ('关联账户', {
            'fields': ('tut_user',)
        }),
        ('基本信息', {
            'fields': (
                'tut_number', 'tut_name', 'tut_avatar', 'tut_gender', 'tut_cardID',
                'tut_birth_day', 'tut_telephone', 'tut_title', 'tut_political',
                'tut_degree', 'tut_entry_day', 'tut_education'
            )
        }),
        ('学院资料', {
            'fields': ('tut_academy',),
        })
    )
    list_filter = [
        'tut_academy',
        'tut_political',
        'tut_title',
        'tut_degree'
    ]
    list_display = (
        'tut_number', 'tut_name', 'get_gender', 'tut_telephone', 'tut_cardID',
        'get_degree', 'get_political', 'tut_birth_day', 'tut_entry_day'
    )
    list_per_page = 20
    search_fields = ('tut_number', 'tut_name', 'tut_telephone')
    empty_value_display = '--'
    change_list_template = 'admin/web/Tutor/change_list.html'


class StudentResource(resources.ModelResource):
    stu_name = Field(attribute='stu_name', column_name='姓名')
    stu_number = Field(attribute='stu_number', column_name='学号')
    stu_candidate_number = Field(attribute='stu_candidate_number', column_name='考生号')
    stu_card_type = Field(attribute='stu_card_type', column_name='身份证件类型')
    stu_cardID = Field(attribute='stu_cardID', column_name='身份证号')
    get_gender = Field(attribute='get_gender', column_name='性别')
    stu_birth_day = Field(attribute='stu_birth_day', column_name='出生日期')
    stu_nation = Field(attribute='stu_nation', column_name='民族')
    stu_source = Field(attribute='stu_source', column_name='生源地')
    stu_is_village = Field(attribute='stu_is_village', column_name='是否农村学生')
    get_political = Field(attribute='get_political', column_name='政治面貌')
    stu_aca_cname = Field(attribute='stu_academy__aca_cname', column_name='学院')
    stu_maj_name = Field(attribute='stu_major__maj_name', column_name='专业')
    stu_get_major_type = Field(attribute='stu_major__maj_type', column_name='专业大类')
    stu_class = Field(attribute='stu_class', column_name='班级')
    get_stu_status = Field(attribute='get_stu_status', column_name='在学状态')
    stu_tut_number = Field(attribute='stu_tutor__tut_number', column_name='导师工号')
    stu_tut_name = Field(attribute='stu_tutor__tut_name', column_name='导师')
    get_stu_type = Field(attribute='get_stu_type', column_name='学生类型')
    get_stu_learn_type = Field(attribute='get_stu_learn_type', column_name='学习形式')
    get_stu_learn_status = Field(attribute='get_stu_learn_status', column_name='学习阶段')
    stu_grade = Field(attribute='stu_grade', column_name='年级')
    stu_system = Field(attribute='stu_system', column_name='学制')
    stu_entrance_time = Field(attribute='stu_entrance_time', column_name='入学日期')
    get_stu_cultivating_mode = Field(attribute='get_stu_cultivating_mode', column_name='培养方式')
    get_stu_enrollment_category = Field(attribute='get_stu_enrollment_category', column_name='录取类别')
    stu_nationality = Field(attribute='stu_nationality', column_name='国籍')
    get_stu_special_program = Field(attribute='get_stu_special_program', column_name='专项计划')
    stu_is_regular_income = Field(attribute='stu_is_regular_income', column_name='是否有固定收入')
    stu_is_tuition_fees = Field(attribute='stu_is_tuition_fees', column_name='是否欠缴学费')
    stu_is_archives = Field(attribute='stu_is_archives', column_name='档案是否转到学校')
    stu_graduation_time = Field(attribute='stu_graduation_time', column_name='毕业日期')

    class Meta:
        model = models.Student
        fields = (
            'stu_name', 'stu_number', 'stu_candidate_number', 'stu_card_type', 'stu_cardID',
            'get_gender', 'stu_birth_day', 'stu_nation', 'stu_source', 'stu_is_village',
            'get_political', 'stu_aca_cname', 'stu_maj_name', 'stu_get_major_type', 'stu_class',
            'get_stu_status', 'stu_tut_number', 'stu_tut_name', 'get_stu_type', 'get_stu_learn_type',
            'get_stu_learn_status', 'stu_grade', 'stu_system', 'stu_entrance_time', 'get_stu_cultivating_mode',
            'get_stu_enrollment_category', 'stu_nationality', 'get_stu_special_program', 'stu_is_regular_income',
            'stu_is_tuition_fees', 'stu_is_archives', 'stu_graduation_time'
        )


@admin.register(models.Student)
class StudentAdmin(ExportActionMixin, admin.ModelAdmin):
    resource_class = StudentResource
    form = forms.StudentForm
    fieldsets = [
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
        })
    ]
    list_filter = (
        'stu_special_program',
        'stu_cultivating_mode',
        'stu_enrollment_category',
        'stu_academy',
        'stu_major',
        'stu_political'
    )
    list_display = (
        'stu_number', 'stu_name', 'get_gender', 'stu_telephone', 'stu_card_type', 'stu_cardID',
        'stu_birth_day', 'stu_nation', 'stu_source', 'stu_is_village', 'get_political',
        'get_stu_type', 'stu_entrance_time',
    )
    list_per_page = 20
    search_fields = ('stu_name', 'stu_telephone')
    empty_value_display = '--'
    change_list_template = 'admin/web/Student/change_list.html'


# admin.site.unregister(User)
# admin.site.unregister(Group)
#
#
# @admin.register(User)
# class AccountAdmin(admin.ModelAdmin):
#     list_per_page = 20
#     empty_value_display = '--'
