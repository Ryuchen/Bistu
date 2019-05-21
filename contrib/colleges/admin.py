#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ==================================================
# @Time : 2019-04-03 11:44 
# @Author : ryuchen
# @Site :  
# @File : admin.py
# @Desc : 
# ==================================================
from django.conf.urls import url
from django.shortcuts import redirect
from inline_actions.admin import InlineActionsModelAdminMixin
from import_export import resources
from import_export.fields import Field
from import_export.admin import ExportMixin

from . import forms
from . import models

from contrib.accounts.models import Student

from django.urls import reverse
from django.contrib import admin
from django_admin_listfilter_dropdown.filters import DropdownFilter, ChoiceDropdownFilter


class ResearchInline(admin.TabularInline):
    verbose_name = '研究方向'
    verbose_name_plural = verbose_name
    model = models.Major.maj_research.through
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
    model = models.Academy.aca_majors.through
    fields = (
        'major',
    )
    readonly_fields = (
        'major',
    )
    can_delete = False
    show_change_link = False
    extra = 0


class ReformInline(admin.TabularInline):
    verbose_name = '教改项目'
    verbose_name_plural = verbose_name
    model = models.Academy.aca_reforms.through
    fields = (
        'reform',
    )
    readonly_fields = (
        'reform',
    )
    can_delete = False
    show_change_link = False
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
        ('maj_first', DropdownFilter),
    ]
    list_display = (
        'maj_code', 'maj_name', 'get_major_type', 'maj_first', 'maj_second',
        'maj_setup_time', 'get_major_degree'
    )
    exclude = ('maj_research',)
    empty_value_display = '--'


class ClassAdmin(admin.ModelAdmin):
    list_display = ('cla_code', 'cla_name')
    empty_value_display = '--'


class AcademyAdmin(InlineActionsModelAdminMixin, admin.ModelAdmin):

    def get_enroll_statistic(self, request, obj, parent_obj=None):
        filter_year = request.GET.get('aca_reforms__ref_time', '')
        response = redirect(reverse("create_xls"), year=filter_year)
        return response
    get_enroll_statistic.short_description = '招生情况'

    def get_urls(self):
        urls = super(AcademyAdmin, self).get_urls()
        urls += [
            url(r'^enroll-statistic/$', self.admin_site.admin_view(self.enroll_statistic))
        ]
        return urls

    def enroll_statistic(self, request):
        filter_year = request.GET.get('aca_reforms__ref_time', '')
        response = redirect(reverse("create_xls"), year=filter_year)
        return response
    
    inlines = [MajorInline, ReformInline]
    inline_actions = ['get_enroll_statistic']
    list_filter = [
        'aca_reforms__ref_time'
    ]
    list_display = (
        'aca_cname', 'aca_code', 'aca_ename', 'aca_phone', 'aca_fax', 'aca_href'
    )
    exclude = ('aca_majors', 'aca_reforms')
    empty_value_display = '--'
    change_list_template = "admin/web/Academy/change_list.html"


class ReformAdmin(admin.ModelAdmin):
    list_display = (
        'ref_name', 'ref_type', 'ref_time'
    )
    empty_value_display = '--'


class ReformResultsResource(resources.ModelResource):
    get_academy_cname = Field(attribute='get_academy_cname', column_name='学院')
    project_count = Field(attribute='project_count', column_name='研究生教育相关教改项目立项数量')
    paper_count = Field(attribute='paper_count', column_name='发表研究生教育相关教改论文数量')
    textbook_count = Field(attribute='textbook_count', column_name='出版研究生教材数量')
    award_count = Field(attribute='award_count', column_name='研究生教育相关获奖数量')
    course_count = Field(attribute='course_count', column_name='精品/在线课程建设数量')
    base_count = Field(attribute='base_count', column_name='实践基地建设数量')
    exchange_project_count = Field(attribute='exchange_project_count', column_name='研究生国际交流数量')

    class Meta:
        model = models.ReformResults
        fields = (
            'get_academy_cname', 'project_count', 'paper_count', 'textbook_count', 'award_count',
            'course_count', 'base_count', 'exchange_project_count'
        )


@admin.register(models.ReformResults)
class ReformResultsAdmin(ExportMixin, admin.ModelAdmin):
    resource_class = ReformResultsResource
    list_display = (
        'get_academy_cname', 'project_count', 'paper_count', 'textbook_count', 'award_count', 'course_count',
        'base_count', 'exchange_project_count', 'get_reform_year'
    )
    date_hierarchy = 'time'
    empty_value_display = '--'


# Register your models here.
admin.site.register(models.Major, MajorsAdmin)
admin.site.register(models.Class, ClassAdmin)
admin.site.register(models.Academy, AcademyAdmin)
admin.site.register(models.Reform, ReformAdmin)
