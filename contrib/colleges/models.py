#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ==================================================
# @Time : 2019-04-02 10:26 
# @Author : ryuchen
# @Site :  
# @File : models.py 
# @Desc : 
# ==================================================
import uuid

from core.definition.enums import *

from django.db import models
from django.contrib.auth.models import User


class Research(models.Model):
    """
    科研方向模型
    """
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True, verbose_name="唯一标识ID")
    res_name = models.CharField(max_length=128, null=True, verbose_name="研究方向")

    def __str__(self):
        return '研究方向: {0}'.format(self.res_name)

    class Meta:
        db_table = 'research'
        verbose_name = "研究方向"
        verbose_name_plural = verbose_name
        default_permissions = ()
        permissions = [
            ("can_insert_research", "新增研究方向"),
            ("can_delete_research", "删除研究方向"),
            ("can_update_research", "修改研究方向"),
            ("can_search_research", "查询研究方向")
        ]


class Major(models.Model):
    """
    学科模型
    """
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True, verbose_name="唯一标识ID")
    maj_name = models.CharField(max_length=128, null=True, verbose_name="学科名称")
    maj_code = models.IntegerField(null=True, verbose_name="学科编号")
    maj_type = models.CharField(max_length=128, choices=[(tag.name, tag.value) for tag in MajorType], verbose_name="学科类型")
    maj_first = models.BooleanField(verbose_name="是否一级学科")
    maj_second = models.BooleanField(verbose_name="是否二级学科")
    maj_setup_time = models.DateField(verbose_name="获批时间")
    maj_degree = models.CharField(max_length=128, choices=[(tag.name, tag.value) for tag in MajorDegree], verbose_name="学位类型")
    research = models.ManyToManyField(Research, related_name='research', verbose_name="科研方向")

    def get_major_type(self):
        return self.maj_type
    get_major_type.short_description = '学科类型'

    def get_major_degree(self):
        return self.maj_degree
    get_major_degree.short_description = '学位类型'

    def __str__(self):
        return '专业编码: {0} 专业名称: {1}'.format(self.maj_code, self.maj_name)

    class Meta:
        db_table = 'major'
        verbose_name = "学科专业"
        verbose_name_plural = verbose_name
        default_permissions = ()
        permissions = [
            ("can_insert_major", "新增学科专业"),
            ("can_delete_major", "删除学科专业"),
            ("can_update_major", "修改学科专业"),
            ("can_search_major", "查询学科专业")
        ]


class Class(models.Model):
    """
    班级模型
    """
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True, verbose_name="唯一标识ID")
    cla_name = models.CharField(max_length=128, null=True, verbose_name="班级名称")
    cla_code = models.IntegerField(null=True, verbose_name="班级代码")
    major = models.ForeignKey(Major, null=True, related_name='cla_major', on_delete=models.SET_NULL, verbose_name="专业名称")

    def __str__(self):
        return "专业名称: {0} => {1}{2}  ".format(self.major.maj_name, self.cla_name, self.cla_code)

    class Meta:
        db_table = 'classes'
        verbose_name = "班级"
        verbose_name_plural = verbose_name
        default_permissions = ()
        permissions = [
            ("can_insert_class", "新增班级"),
            ("can_delete_class", "删除班级"),
            ("can_update_class", "修改班级"),
            ("can_search_class", "查询班级")
        ]


class Academy(models.Model):
    """
    学院模型
    """
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True, verbose_name="唯一标识ID")
    aca_avatar = models.ImageField(null=True, upload_to="academies", default='default.png', verbose_name="学院图标")
    aca_nickname = models.CharField(max_length=128, null=True, verbose_name="学院简称")
    aca_cname = models.CharField(max_length=128, null=True, verbose_name="学院名称(中)")
    aca_ename = models.CharField(max_length=128, null=True, verbose_name="学院名称(英)")
    aca_code = models.IntegerField(null=True, verbose_name="学院代码")
    aca_phone = models.CharField(max_length=128, null=True, verbose_name="学院电话")
    aca_fax = models.CharField(max_length=128, null=True, verbose_name="学院传真")
    aca_href = models.URLField(max_length=256, null=True, verbose_name="学院网址")
    aca_brief = models.TextField(verbose_name="学院简介")
    aca_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name="学院负责人", related_name="aca_user")
    majors = models.ManyToManyField(Major, related_name='majors')

    def __str__(self):
        return str(self.aca_code) + self.aca_cname

    class Meta:
        db_table = 'academy'
        verbose_name = "学院"
        verbose_name_plural = verbose_name
        default_permissions = ()
        permissions = [
            ("can_insert_academy", "新增学院"),
            ("can_delete_academy", "删除学院"),
            ("can_update_academy", "修改学院"),
            ("can_search_academy", "查询学院")
        ]


class Reform(models.Model):
    """
    教育改革项目统计模型
    """
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True, verbose_name="唯一标识ID")
    time = models.IntegerField(null=False, verbose_name="年份")
    ref_type = models.CharField(max_length=128, choices=[(tag.name, tag.value) for tag in ReformType], verbose_name="教改成果类型")
    ref_name = models.TextField(verbose_name="教改项目名称")
    academy = models.ForeignKey(Academy, null=True, related_name='r_academy', on_delete=models.SET_NULL, verbose_name="学院名称")

    class Meta:
        db_table = 'reform'
        verbose_name = "教育改革成果"
        verbose_name_plural = verbose_name
        default_permissions = ()
        permissions = [
            ("can_insert_reform", "新增教改成果"),
            ("can_delete_reform", "删除教改成果"),
            ("can_update_reform", "修改教改成果"),
            ("can_search_reform", "查询教改成果")
        ]


class ReformResults(models.Model):
    """
    教育改革成果统计模型
    """
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True, verbose_name="唯一标识ID")
    time = models.IntegerField(null=False, verbose_name="年份")
    project_count = models.IntegerField(null=False, default=0, verbose_name="研究生教育相关教改项目立项数量")
    paper_count = models.IntegerField(null=False, default=0, verbose_name="发表研究生教育相关教改论文数量")
    textbook_count = models.IntegerField(null=False, default=0, verbose_name="出版研究生教材数量")
    award_count = models.IntegerField(null=False, default=0, verbose_name="研究生教育相关获奖数量")
    course_count = models.IntegerField(null=False, default=0, verbose_name="精品/在线课程建设数量")
    base_count = models.IntegerField(null=False, default=0, verbose_name="实践基地建设数量")
    exchange_project_count = models.IntegerField(null=False, default=0, verbose_name="研究生国际交流数量")
    academy = models.ForeignKey(Academy, null=True, related_name='rr_academy', on_delete=models.SET_NULL, verbose_name="学院名称")

    class Meta:
        db_table = 'reform_result'
        verbose_name = "教育改革成果统计"
        verbose_name_plural = verbose_name
        default_permissions = ()
        permissions = [
            ("can_insert_reform_result", "新增教改统计"),
            ("can_delete_reform_result", "删除教改统计"),
            ("can_update_reform_result", "修改教改统计"),
            ("can_search_reform_result", "查询教改统计")
        ]
