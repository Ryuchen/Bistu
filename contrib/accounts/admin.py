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


class TutorAdmin(admin.ModelAdmin):
    list_display = (
        'tut_number', 'tut_name', 'get_gender', 'tut_telephone', 'get_degree',
        'get_political', 'tut_birth_day', 'tut_entry_day', 'tut_cardID'
    )
    empty_value_display = '--'


class StudentAdmin(admin.ModelAdmin):
    form = forms.StudentForm

    # stu_telephone = models.IntegerField(null=True, verbose_name="电话号码")
    # stu_card_type = models.CharField(max_length=128, null=True, verbose_name='身份证件类型', default="身份证")
    # stu_cardID = models.CharField(max_length=128, null=True, unique=True, verbose_name="身份证号", default="")
    # stu_candidate_number = models.CharField(max_length=128, null=True, verbose_name="考生号")
    # stu_birth_day = models.DateField(max_length=64, null=True, verbose_name="出生日期", default='201909')
    # stu_nation = models.CharField(max_length=64, null=True, verbose_name='民族', default='汉')
    # stu_source = models.CharField(max_length=128, null=True, verbose_name="生源地")
    # stu_is_village = models.BooleanField(null=True, verbose_name='是否农村学生')
    # stu_political = models.CharField(max_length=64, null=True, choices=[(tag.name, tag.value) for tag in PoliticalChoice], verbose_name="政治面貌")
    # stu_type = models.CharField(max_length=128, null=True, choices=[(tag.name, tag.value) for tag in StudentType], verbose_name='学生类型', default='S1')
    # stu_learn_type = models.CharField(max_length=64, null=True, choices=[(tag.name, tag.value) for tag in StudentCategory], verbose_name='学习形式', default='S1')
    # stu_learn_status = models.CharField(max_length=64, null=True, verbose_name='学习阶段', default='D2', choices=[(tag.name, tag.value) for tag in DegreeChoice])
    # stu_grade = models.CharField(max_length=64, null=True, verbose_name='年级', default='1')
    # stu_system = models.IntegerField(null=True, verbose_name='学制', default=3)
    # stu_entrance_time = models.DateField(max_length=32, null=True, verbose_name='入学日期', default='2019-09')
    # stu_graduation_time = models.DateField(max_length=32, null=True, verbose_name='毕业日期', default='2021-07')
    # stu_cultivating_mode = models.CharField(max_length=128, null=True, verbose_name='培养方式', default='C1', choices=[(tag.name, tag.value) for tag in CultivatingMode])
    # stu_enrollment_category = models.CharField(max_length=64, null=True, choices=[(tag.name, tag.value) for tag in EnrollmentCategory], verbose_name='录取类别', default='E1')
    # stu_nationality = models.CharField(max_length=128, null=True, verbose_name='国籍', default='中国')
    # stu_special_program = models.CharField(max_length=128, null=True, choices=[(tag.name, tag.value) for tag in SpecialProgram], verbose_name='专项计划', default='S1')
    # stu_is_regular_income = models.BooleanField(default=False, verbose_name='是否有固定收入')
    # stu_is_tuition_fees = models.BooleanField(default=False, verbose_name='是否欠缴学费')
    # stu_is_archives = models.BooleanField(default=False, verbose_name='档案是否转到学校')
    # stu_is_exemption = models.BooleanField(default=False, verbose_name="是否推免生")
    # stu_is_adjust = models.BooleanField(default=False, verbose_name="是否调剂")
    # stu_is_volunteer = models.BooleanField(default=True, verbose_name="是否第一志愿")
    # stu_is_superb = models.BooleanField(default=False, verbose_name="是否优秀毕业生")
    # stu_is_delay = models.BooleanField(default=True, verbose_name="是否延期（中期考核）")
    # stu_delay_reason = models.CharField(max_length=255, null=True, verbose_name="中期考核延期原因")
    # stu_mid_check = models.CharField(max_length=64, null=True, choices=[(tag.name, tag.value) for tag in MidCheckChoice], verbose_name="中期考核结果")
    # stu_status = models.CharField(max_length=64, null=True, choices=[(tag.name, tag.value) for tag in StatusChoice], verbose_name="在学状态", default='S1')
    # stu_gain_diploma = models.BooleanField(null=True, default=False, verbose_name="学位证")
    # stu_gain_cert = models.BooleanField(null=True, default=False, verbose_name="毕业证")
    # stu_tutor = models.ForeignKey(Tutor, null=True, related_name='stu_tutor', on_delete=models.SET_NULL, verbose_name="指导老师")
    # stu_class = models.ForeignKey(Class, null=True, related_name='stu_class', on_delete=models.SET_NULL, verbose_name="所属班级")
    # stu_major = models.ForeignKey(Major, null=True, related_name='stu_major', on_delete=models.SET_NULL, verbose_name="所属专业")
    # stu_academy = models.ForeignKey(Academy, null=True, related_name='stu_academy', on_delete=models.SET_NULL, verbose_name='所属学院')
    # stu_research = models.ForeignKey(Research, null=True, related_name='stu_research', on_delete=models.SET_NULL, verbose_name="科研方向")
    #
    fieldsets = (
        ('关联账户', {
            'fields': ('user',)
        }),
        ('基本信息', {
            'fields': (
                'stu_number', 'stu_name', 'stu_avatar', 'stu_gender',
                'stu_telephone', 'stu_candidate_number', 'stu_birth_day')
        }),
        ('学院资料', {
            'fields': ('stu_academy', 'stu_major', 'stu_class', 'stu_research', 'stu_tutor'),
        }),
        ('档案信息', {
            'fields': ('stu_is_village', 'stu_is_regular_income'),
        }),
    )
    list_display = (
        'stu_number', 'stu_name', 'get_gender', 'stu_telephone', 'stu_card_type', 'stu_cardID',
        'stu_birth_day', 'stu_nation', 'stu_source', 'stu_is_village', 'get_political',
        'stu_type', 'stu_entrance_time',
        # 'stu_graduation_time', 'stu_cultivating_mode', 'stu_enrollment_category', 'stu_nationality',
        # 'stu_candidate_number', 'stu_special_program', 'stu_learn_type', 'stu_learn_status', 'stu_grade', 'stu_system',
        'stu_is_regular_income', 'stu_is_tuition_fees', 'stu_is_archives', 'stu_is_exemption',
        'stu_is_adjust', 'stu_is_volunteer',
    )
    empty_value_display = '--'


# Register your models here.
admin.site.register(models.Tutor, TutorAdmin)
admin.site.register(models.Student, StudentAdmin)
