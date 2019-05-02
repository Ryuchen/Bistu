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

from contrib.users.models import Student
from contrib.academy.models import Academy


class Thesis(models.Model):
    """
    毕业论文模型
    """
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True, help_text="唯一标识ID")
    the_title = models.CharField(max_length=128, null=False, help_text="课题名称")
    the_start_time = models.DateField(help_text="开题时间")
    the_mid_score = models.CharField(max_length=64, help_text="中期考核结果")
    the_start_result = models.BooleanField(null=False, default=True, help_text="开题结果")
    the_exam_count = models.IntegerField(null=False, default=0, help_text="论文查重次数")
    the_final_score = models.CharField(max_length=64, help_text="答辩成绩")
    the_is_superb = models.BooleanField(default=False, help_text="是否优秀论文")
    the_is_delay = models.BooleanField(default=False, help_text="是否延期")
    the_delay_reason = models.TextField(null=True, help_text="延期原因")
    student = models.OneToOneField(Student, null=True, related_name='student', on_delete=models.SET_NULL, help_text="课题学生")

    def __str__(self):
        return "论文课题：{0}".format(self.the_title)

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


class PlaCheck(models.Model):
    """
    论文查重模型 Pla = Plagiarism
    """
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True, help_text="唯一标识ID")
    pla_result = models.CharField(max_length=128, null=False, help_text="查重结果")
    pla_rate = models.CharField(max_length=128, null=False, help_text="重复率")
    thesis = models.OneToOneField(Thesis, null=True, related_name='thesis', on_delete=models.SET_NULL, help_text="论文课题")

    def __str__(self):
        return "论文查重：{0}".format(self.thesis.the_title)

    class Meta:
        db_table = 'plaCheck'
        verbose_name = "论文查重"
        verbose_name_plural = verbose_name
        default_permissions = ()
        permissions = [
            ("can_insert_plaCheck", "新增查重结果"),
            ("can_delete_plaCheck", "删除查重结果"),
            ("can_update_plaCheck", "修改查重结果"),
            ("can_search_plaCheck", "查询查重结果")
        ]


class BlindReview(models.Model):
    """
    论文盲审模型
    """
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True, help_text="唯一标识ID")
    bli_score = models.CharField(max_length=64, help_text="盲审结果")
    thesis = models.OneToOneField(Thesis, null=True, related_name='thesis', on_delete=models.SET_NULL, help_text="论文课题")

    def __str__(self):
        return "论文盲审：{0}".format(self.thesis.the_title)

    class Meta:
        db_table = 'blindReview'
        verbose_name = "论文盲审"
        verbose_name_plural = verbose_name
        default_permissions = ()
        permissions = [
            ("can_insert_blindReview", "新增盲审结果"),
            ("can_delete_blindReview", "删除盲审结果"),
            ("can_update_blindReview", "修改盲审结果"),
            ("can_search_blindReview", "查询盲审结果")
        ]


class OpenThesisReport(models.Model):
    """
    开题统计模型
    """
    academy = models.CharField(max_length=128, null=False, default="", help_text="学院名称")
    stu_count = models.IntegerField(null=False, default=0, help_text="学生数量")
    schedule_count = models.IntegerField(null=False, default=0, help_text="按期开题人数")
    delay_count = models.IntegerField(null=False, default=0, help_text="延期开题人数")
    fail_count = models.IntegerField(null=False, default=0, help_text="开题不通过人数")
    time = models.DateField(null=False, default='2019', help_text="开题年份")

    class Meta:
        db_table = 'openThesisReport'
        verbose_name = "开题报告统计"
        verbose_name_plural = verbose_name
        default_permissions = ()
        permissions = [
            ("can_insert_openThesisReport", "新增开题统计"),
            ("can_delete_openThesisReport", "删除开题统计"),
            ("can_update_openThesisReport", "修改开题统计"),
            ("can_search_openThesisReport", "查询开题统计")
        ]


class MidThesisReport(models.Model):
    """
    中期考核统计模型
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
        db_table = 'midThesisReport'
        verbose_name = "中期考核统计"
        verbose_name_plural = verbose_name
        default_permissions = ()
        permissions = [
            ("can_insert_midThesisReport", "新增中期考核统计"),
            ("can_delete_midThesisReport", "删除中期考核统计"),
            ("can_update_midThesisReport", "修改中期考核统计"),
            ("can_search_midThesisReport", "查询中期考核统计")
        ]


class ThesisQuality(models.Model):
    """
    论文质量统计模型
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
        db_table = 'thesisQuality'
        verbose_name = "论文质量统计"
        verbose_name_plural = verbose_name
        default_permissions = ()
        permissions = [
            ("can_insert_thesisQuality", "新增论文质量统计"),
            ("can_delete_thesisQuality", "删除论文质量统计"),
            ("can_update_thesisQuality", "修改论文质量统计"),
            ("can_search_thesisQuality", "查询论文质量统计")
        ]
