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
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True, help_text="唯一标识ID")
    res_name = models.CharField(max_length=128, null=True, help_text="研究方向")

    def __str__(self):
        return self.res_name

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
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True, help_text="唯一标识ID")
    maj_name = models.CharField(max_length=128, null=True, help_text="学科名称")
    maj_code = models.IntegerField(null=True, help_text="学科编号")
    maj_type = models.CharField(max_length=128, choices=[(tag.name, tag.value) for tag in MajorType], help_text="学科类型")
    maj_first = models.BooleanField(help_text="是否一级学科")
    maj_second = models.BooleanField(help_text="是否二级学科")
    maj_first_uuid = models.UUIDField(null=True, help_text="所属一级学科")
    maj_setup_time = models.DateField(help_text="获批时间")
    maj_degree = models.CharField(max_length=128, choices=[(tag.name, tag.value) for tag in MajorDegree], help_text="学位类型")
    research = models.ManyToManyField(Research, related_name='research', help_text="科研方向")

    def __str__(self):
        return str(self.maj_code) + self.maj_name

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


class Academy(models.Model):
    """
    学院模型
    """
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True, help_text="唯一标识ID")
    aca_avatar = models.ImageField(null=True, upload_to="academies", default='default.png', help_text="学院图标")
    # aca_avatar = models.ImageField(max_length=128, help_text="学院图标", null=True)
    aca_nickname = models.CharField(max_length=128, null=True, help_text="学院简称")
    aca_cname = models.CharField(max_length=128, null=True, help_text="学院名称(中)")
    aca_ename = models.CharField(max_length=128, null=True, help_text="学院名称(英)")
    aca_code = models.IntegerField(null=True, help_text="学院代码")
    aca_phone = models.CharField(max_length=128, null=True, help_text="学院电话")
    aca_fax = models.CharField(max_length=128, null=True, help_text="学院传真")
    aca_href = models.URLField(max_length=256, null=True, help_text="学院网址")
    aca_brief = models.TextField(help_text="学院简介")
    aca_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, help_text="学院负责人", related_name="aca_user")
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


# TODO: add this pages
class OpeningReport(models.Model):
    """
    开题报告统计模型
    """
    academy = models.CharField(max_length=128, null=False, default="", help_text="学院名称")
    stu_count = models.IntegerField(null=False, default=0, help_text="学生数量")
    schedule_count = models.IntegerField(null=False, default=0, help_text="按期开题人数")
    delay_count = models.IntegerField(null=False, default=0, help_text="延期开题人数")
    fail_count = models.IntegerField(null=False, default=0, help_text="开题不通过人数")
    time = models.DateField(null=False, default='2019', help_text="入学年份")

    class Meta:
        verbose_name = "开题报告统计"
        verbose_name_plural = verbose_name
        
        
class ReformResults(models.Model):
    """
    教育改革成果统计模型
    """
    academy = models.CharField(max_length=128, null=False, default="", help_text="学院名称")
    project_count = models.IntegerField(null=False, default=0, help_text="研究生教育相关教改项目立项数量")
    paper_count = models.IntegerField(null=False, default=0, help_text="发表研究生教育相关教改论文数量")
    textbook_count = models.IntegerField(null=False, default=0, help_text="出版研究生教材数量")
    award_count = models.IntegerField(null=False, default=0, help_text="研究生教育相关获奖数量")
    course_count = models.IntegerField(null=False, default=0, help_text="精品/在线课程建设数量")
    base_count = models.IntegerField(null=False, default=0, help_text="实践基地建设数量")
    exchange_project_count = models.IntegerField(null=False, default=0, help_text="研究生国际交流数量")
    time = models.DateField(null=False, default='2019', help_text="入学年份")

    class Meta:
        verbose_name = "教育改革成果统计"
        verbose_name_plural = verbose_name


class MidtermExams(models.Model):
    """
    中期考核情况统计模型
    """
    academy = models.CharField(max_length=128, null=False, default="", help_text="学院名称")
    stu_count = models.IntegerField(null=False, default=0, help_text="学生数量")
    schedule_count = models.IntegerField(null=False, default=0, help_text="按期考核人数")
    delay_count = models.IntegerField(null=False, default=0, help_text="延期考核人数")
    delay_reason = models.TextField(null=False, default="", help_text="延期考核原因")
    delay_proportion = models.IntegerField(null=False, default=0, help_text="延期考核比例")
    track_count = models.IntegerField(null=False, default=0, help_text="被跟踪人数")
    track_proportion = models.IntegerField(null=False, default=0, help_text="被跟踪比例")
    fail_count = models.IntegerField(null=False, default=0, help_text="不合格人数")
    fail_proportion = models.IntegerField(null=False, default=0, help_text="不合格比例")
    time = models.DateField(null=False, default='2019', help_text="入学年份")

    class Meta:
        verbose_name = "中期考核情况统计"
        verbose_name_plural = verbose_name


class PaperQuality(models.Model):
    """
    学位论文质量统计模型
    """
    academy = models.CharField(max_length=128, null=False, default="", help_text="学院名称")
    major = models.CharField(max_length=128, null=False, default="", help_text="专业名称")
    full_time_count = models.IntegerField(null=False, default=0, help_text="全日制学生数量")
    delay_count = models.IntegerField(null=False, default=0, help_text="延期人数")
    delay_reason = models.TextField(null=False, default="", help_text="延期原因")
    paper_stu_count = models.IntegerField(null=False, default=0, help_text="论文检测人数")
    paper_pass_count = models.IntegerField(null=False, default=0, help_text="论文检测结果一次通过人数")
    paper_pass_proportion = models.IntegerField(null=False, default=0, help_text="论文检测结果一次通过率")
    paper_fail_count = models.IntegerField(null=False, default=0, help_text="论文检测结果不合格人数")
    paper_fail_proportion = models.IntegerField(null=False, default=0, help_text="论文检测结果不合格占比")
    paper_fifteen_count = models.IntegerField(null=False, default=0, help_text="论文检测结果15%以下人数")
    paper_fifteen_proportion = models.IntegerField(null=False, default=0, help_text="论文检测结果15%以下占比")
    paper_ten_count = models.IntegerField(null=False, default=0, help_text="论文检测结果10%以下人数")
    paper_ten_proportion = models.IntegerField(null=False, default=0, help_text="论文检测结果10%以下占比")
    blind_trial_proportion = models.IntegerField(null=False, default=0, help_text="盲审比例")
    blind_trial_count = models.IntegerField(null=False, default=0, help_text="盲审未通过人数")
    reply_count = models.IntegerField(null=False, default=0, help_text="答辩未通过人数")
    evaluation_count = models.IntegerField(null=False, default=0, help_text="评优名额")
    evaluation_result = models.IntegerField(null=False, default=0, help_text="评优评选结果")
    graduate_count = models.IntegerField(null=False, default=0, help_text="毕业人数")
    graduate_proportion = models.IntegerField(null=False, default=0, help_text="毕业率")
    degree_count = models.IntegerField(null=False, default=0, help_text="获学位人数")
    degree_proportion = models.IntegerField(null=False, default=0, help_text="获学位率")
    time = models.DateField(null=False, default='2019', help_text="入学年份")

    class Meta:
        verbose_name = "学位论文质量统计"
        verbose_name_plural = verbose_name
