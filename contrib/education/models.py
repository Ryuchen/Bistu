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

from django.db import models

# from contrib.accounts.models import Student
from contrib.colleges.models import Academy, Major


class Thesis(models.Model):
    """
    毕业论文模型
    """
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True, verbose_name="唯一标识ID")
    the_title = models.CharField(max_length=128, null=False, verbose_name="课题名称")
    the_start_time = models.DateField(verbose_name="开题时间")
    the_start_result = models.BooleanField(null=False, default=True, verbose_name="开题结果")
    the_exam_count = models.IntegerField(null=False, default=0, verbose_name="论文查重次数")  # 这个数据应该从查重那张表统计出来
    the_is_delay = models.BooleanField(default=False, verbose_name="是否延期")
    the_delay_reason = models.TextField(null=True, verbose_name="延期原因")
    the_is_superb = models.BooleanField(default=False, verbose_name="是否优秀论文")
    the_final_score = models.BooleanField(default=False, verbose_name="答辩成绩")  # 只存通过和不通过两种情况

    def get_thesis_title(self):
        return '《{0}》'.format(self.the_title)
    get_thesis_title.short_description = '标题'

    def __str__(self):
        return "论文课题：《{0}》".format(self.the_title)

    class Meta:
        db_table = 'thesis'
        verbose_name = "毕业论文"
        verbose_name_plural = verbose_name
        default_permissions = ()
        permissions = [
            ("can_insert_thesis", "新增毕业论文"),
            ("can_delete_thesis", "删除毕业论文"),
            ("can_update_thesis", "修改毕业论文"),
            ("can_search_thesis", "查询毕业论文")
        ]


class ThesisPlaCheck(models.Model):
    """
    论文查重模型 Pla = Plagiarism
    """
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True, verbose_name="唯一标识ID")
    pla_date = models.DateField(null=False, verbose_name="查重时间")
    pla_result = models.CharField(max_length=128, null=False, verbose_name="查重结果")
    pla_rate = models.CharField(max_length=128, null=False, verbose_name="重复率")
    thesis = models.ForeignKey(Thesis, null=True, related_name='pla_thesis', on_delete=models.SET_NULL, verbose_name="论文课题")

    def __str__(self):
        return "查重:《{0}》".format(self.thesis.the_title)

    class Meta:
        db_table = 'thesis_pla_check'
        verbose_name = "论文查重"
        verbose_name_plural = verbose_name
        default_permissions = ()
        permissions = [
            ("can_insert_thesis_pla_check", "新增查重结果"),
            ("can_delete_thesis_pla_check", "删除查重结果"),
            ("can_update_thesis_pla_check", "修改查重结果"),
            ("can_search_thesis_pla_check", "查询查重结果")
        ]


class ThesisBlindReview(models.Model):
    """
    论文盲审模型
    """
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True, verbose_name="唯一标识ID")
    bli_date = models.DateField(null=False, verbose_name="盲审时间")
    bli_score = models.CharField(max_length=64, verbose_name="盲审结果")
    thesis = models.ForeignKey(Thesis, null=True, related_name='bli_thesis', on_delete=models.SET_NULL, verbose_name="论文课题")

    def __str__(self):
        return "盲审:《{0}》".format(self.thesis.the_title)

    class Meta:
        db_table = 'thesis_blind_review'
        verbose_name = "论文盲审"
        verbose_name_plural = verbose_name
        default_permissions = ()
        permissions = [
            ("can_insert_thesis_blind_review", "新增盲审结果"),
            ("can_delete_thesis_blind_review", "删除盲审结果"),
            ("can_update_thesis_blind_review", "修改盲审结果"),
            ("can_search_thesis_blind_review", "查询盲审结果")
        ]


class ThesisOpenReport(models.Model):
    """
    开题统计模型
    """
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True, verbose_name="唯一标识ID")
    time = models.DateField(null=False, default='2019', verbose_name="年份")
    stu_count = models.IntegerField(null=False, default=0, verbose_name="学生数量")
    schedule_count = models.IntegerField(null=False, default=0, verbose_name="按期开题人数")
    delay_count = models.IntegerField(null=False, default=0, verbose_name="延期开题人数")
    fail_count = models.IntegerField(null=False, default=0, verbose_name="开题不通过人数")
    academy = models.ForeignKey(Academy, null=True, related_name='otr_academy', on_delete=models.SET_NULL, verbose_name="学院名称")

    class Meta:
        db_table = 'thesis_open_report'
        verbose_name = "开题报告统计"
        verbose_name_plural = verbose_name
        default_permissions = ()
        permissions = [
            ("can_insert_thesis_open_report", "新增开题统计"),
            ("can_delete_thesis_open_report", "删除开题统计"),
            ("can_update_thesis_open_report", "修改开题统计"),
            ("can_search_thesis_open_report", "查询开题统计")
        ]


class ThesisQualityReport(models.Model):
    """
    论文质量统计模型
    """
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True, verbose_name="唯一标识ID")
    time = models.DateField(null=False, default='2019', verbose_name="年份")
    full_time_count = models.IntegerField(null=False, default=0, verbose_name="全日制学生数量")
    delay_count = models.IntegerField(null=False, default=0, verbose_name="延期人数")
    delay_reason = models.TextField(null=False, default="", verbose_name="延期原因")
    paper_stu_count = models.IntegerField(null=False, default=0, verbose_name="论文检测人数")
    paper_pass_count = models.IntegerField(null=False, default=0, verbose_name="论文检测结果一次通过人数")
    paper_pass_proportion = models.IntegerField(null=False, default=0, verbose_name="论文检测结果一次通过率")
    paper_fail_count = models.IntegerField(null=False, default=0, verbose_name="论文检测结果不合格人数")
    paper_fail_proportion = models.IntegerField(null=False, default=0, verbose_name="论文检测结果不合格占比")
    paper_fifteen_count = models.IntegerField(null=False, default=0, verbose_name="论文检测结果15%以下人数")
    paper_fifteen_proportion = models.IntegerField(null=False, default=0, verbose_name="论文检测结果15%以下占比")
    paper_ten_count = models.IntegerField(null=False, default=0, verbose_name="论文检测结果10%以下人数")
    paper_ten_proportion = models.IntegerField(null=False, default=0, verbose_name="论文检测结果10%以下占比")
    blind_trial_proportion = models.IntegerField(null=False, default=0, verbose_name="盲审比例")
    blind_trial_count = models.IntegerField(null=False, default=0, verbose_name="盲审未通过人数")
    reply_count = models.IntegerField(null=False, default=0, verbose_name="答辩未通过人数")
    evaluation_count = models.IntegerField(null=False, default=0, verbose_name="评优名额")
    evaluation_result = models.IntegerField(null=False, default=0, verbose_name="评优评选结果")
    graduate_count = models.IntegerField(null=False, default=0, verbose_name="毕业人数")
    graduate_proportion = models.IntegerField(null=False, default=0, verbose_name="毕业率")
    degree_count = models.IntegerField(null=False, default=0, verbose_name="获学位人数")
    degree_proportion = models.IntegerField(null=False, default=0, verbose_name="获学位率")
    major = models.ForeignKey(Major, null=True, related_name='tq_major', on_delete=models.SET_NULL, verbose_name="学科专业")
    academy = models.ForeignKey(Academy, null=True, related_name='tq_academy', on_delete=models.SET_NULL, verbose_name="学院名称")

    class Meta:
        db_table = 'thesis_quality_report'
        verbose_name = "论文质量统计"
        verbose_name_plural = verbose_name
        default_permissions = ()
        permissions = [
            ("can_insert_thesis_quality_report", "新增论文质量统计"),
            ("can_delete_thesis_quality_report", "删除论文质量统计"),
            ("can_update_thesis_quality_report", "修改论文质量统计"),
            ("can_search_thesis_quality_report", "查询论文质量统计")
        ]
