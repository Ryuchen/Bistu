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


class ThesisPlaCheckInline(admin.TabularInline):
    verbose_name = '查重结果'
    verbose_name_plural = verbose_name
    model = models.ThesisPlaCheck
    extra = 0


class ThesisBlindReviewInline(admin.TabularInline):
    verbose_name = '盲审结果'
    verbose_name_plural = verbose_name
    model = models.ThesisBlindReview
    extra = 0


class ThesisAdmin(admin.ModelAdmin):
    actions_on_top = True
    search_fields = ('the_title', )
    list_display = (
        'get_thesis_title', 'the_start_time', 'the_start_result', 'the_is_delay', 'the_delay_reason',
        'the_is_superb', 'the_final_score'
    )
    inlines = [
        ThesisPlaCheckInline,
        ThesisBlindReviewInline
    ]
    empty_value_display = '--'


# class ThesisPlaCheckAdmin(admin.ModelAdmin):
#     list_display = (
#         'pla_date', 'pla_result', 'pla_rate', 'thesis'
#     )
#     empty_value_display = '--'
#
#
# class ThesisBlindReviewAdmin(admin.ModelAdmin):
#     list_display = (
#         'bli_date', 'bli_score', 'thesis'
#     )
#     empty_value_display = '--'


# Register your models here.
admin.site.register(models.Thesis, ThesisAdmin)
# admin.site.register(models.ThesisPlaCheck, ThesisPlaCheckAdmin)
# admin.site.register(models.ThesisBlindReview, ThesisBlindReviewAdmin)
