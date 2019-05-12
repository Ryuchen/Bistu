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


class ThesisAdmin(admin.ModelAdmin):
    list_display = (
        'the_title', 'the_start_time', 'the_start_result', 'the_is_delay', 'the_delay_reason',
        'the_is_superb', 'the_final_score'
    )
    empty_value_display = '--'


class ThesisPlaCheckAdmin(admin.ModelAdmin):
    empty_value_display = '--'


class ThesisBlindReviewAdmin(admin.ModelAdmin):
    empty_value_display = '--'


class ThesisOpenReportAdmin(admin.ModelAdmin):
    empty_value_display = '--'


# Register your models here.
admin.site.register(models.Thesis, ThesisAdmin)
admin.site.register(models.ThesisPlaCheck, ThesisPlaCheckAdmin)
admin.site.register(models.ThesisBlindReview, ThesisBlindReviewAdmin)
admin.site.register(models.ThesisOpenReport, ThesisOpenReportAdmin)
