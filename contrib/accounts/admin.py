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


class TutorAdmin(admin.ModelAdmin):
    list_display = (
        'tut_number', 'tut_name', 'get_gender', 'tut_telephone', 'get_degree',
        'get_political', 'tut_birth_day', 'tut_entry_day', 'tut_cardID'
    )
    empty_value_display = '--'


class StudentAdmin(admin.ModelAdmin):
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
