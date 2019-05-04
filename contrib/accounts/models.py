#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ==================================================
# @Time : 2019-04-02 10:22
# @Author : ryuchen
# @Site :
# @File : models.py
# @Desc :
# ==================================================
import uuid
from django.db import models
from django.contrib.auth.models import User

from core.definition.enums import *
from contrib.colleges.models import Academy, Major, Research, Class


class Education(models.Model):
    """
    学习经历模型
    """
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True, help_text="唯一标识ID")
    edu_begin_time = models.DateField(help_text="开始时间")
    edu_finish_time = models.DateField(help_text="结束时间")
    edu_school_name = models.CharField(max_length=128, null=True, help_text="学校名称")
    edu_study_major = models.CharField(max_length=128, null=True, help_text="专业方向")
    edu_study_field = models.CharField(max_length=128, null=True, help_text="研究领域")

    def __str__(self):
        return "学校：{0}  专业：{1}".format(self.edu_school_name, self.edu_study_major)

    class Meta:
        db_table = 'education'
        verbose_name = "学习经历"
        verbose_name_plural = verbose_name
        default_permissions = ()
        permissions = [
            ("can_insert_education", "新增学习经历"),
            ("can_delete_education", "删除学习经历"),
            ("can_update_education", "修改学习经历"),
            ("can_search_education", "查询学习经历")
        ]


class Tutor(models.Model):
    """
    导师模型
    """
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True, help_text="唯一标识ID")
    tut_name = models.CharField(null=True, max_length=64, help_text="导师名称")
    tut_avatar = models.ImageField(null=True, upload_to="teachers", default='default.png', help_text="教师图片")
    tut_birth_day = models.DateField(max_length=128, null=True, help_text="出生日期")
    tut_entry_day = models.DateField(max_length=128, null=True, help_text="入职日期")
    tut_telephone = models.IntegerField(null=True, help_text="电话号码")
    tut_number = models.IntegerField(null=True, unique=True, help_text="导师工号")
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name='user')
    tut_cardID = models.CharField(max_length=128, null=True, unique=True, help_text="身份证号")
    education = models.ForeignKey(Education, null=True, on_delete=True, related_name='education', help_text="学历")
    academy = models.ForeignKey(Academy, null=True, on_delete=models.CASCADE, related_name='academy', help_text="所属学院")
    tut_gender = models.CharField(max_length=64, choices=sorted([(tag.name, tag.value) for tag in GenderChoice]),
                                  help_text="性别")
    tut_title = models.CharField(max_length=64, choices=sorted([(tag.name, tag.value) for tag in TitleChoice]),
                                 help_text="职称")
    tut_political = models.CharField(max_length=64, choices=sorted([(tag.name, tag.value) for tag in PoliticalChoice]),
                                     help_text="政治面貌")
    tut_degree = models.CharField(max_length=64, choices=sorted([(tag.name, tag.value) for tag in DegreeChoice]),
                                  help_text="学位")

    def __str__(self):
        return "工号：{0}  姓名：{1}".format(self.tut_number, self.user.first_name + self.user.last_name)

    class Meta:
        db_table = 'teacher'
        verbose_name = "导师"
        verbose_name_plural = verbose_name
        default_permissions = ()
        permissions = [
            ("can_insert_tutor", "新增导师"),
            ("can_delete_tutor", "删除导师"),
            ("can_update_tutor", "修改导师"),
            ("can_search_tutor", "查询导师")
        ]
        ordering = ['tut_number']


class Student(models.Model):
    """
    学生模型
    """
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True, help_text="唯一标识ID")
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name='stu_user')
    stu_name = models.CharField(null=True, max_length=64, help_text="学生名称")
    stu_number = models.IntegerField(null=True, unique=True, default='20190101', help_text="学号")
    stu_avatar = models.ImageField(null=True, upload_to="students", default='default.png', help_text="学生照片")
    stu_gender = models.CharField(max_length=64, null=True, choices=[(tag.name, tag.value) for tag in GenderChoice], help_text="性别")
    stu_telephone = models.IntegerField(null=True, help_text="电话号码")
    stu_card_type = models.CharField(max_length=128, null=True, help_text='身份证件类型', default="身份证")
    stu_cardID = models.CharField(max_length=128, null=True, unique=True, help_text="身份证号", default="")
    stu_candidate_number = models.CharField(max_length=128, null=True, help_text="考生号")
    stu_birth_day = models.DateField(max_length=64, null=True, help_text="出生日期", default='201909')
    stu_nation = models.CharField(max_length=64, null=True, help_text='民族', default='汉')
    stu_source = models.CharField(max_length=128, null=True, help_text="生源地")
    stu_is_village = models.BooleanField(null=True, help_text='是否农村学生')
    stu_political = models.CharField(max_length=64, null=True, choices=[(tag.name, tag.value) for tag in PoliticalChoice], help_text="政治面貌")
    stu_type = models.CharField(max_length=128, null=True, choices=[(tag.name, tag.value) for tag in StudentType], help_text='学生类型', default='S1')
    stu_learn_type = models.CharField(max_length=64, null=True, choices=[(tag.name, tag.value) for tag in StudentCategory], help_text='学习形式', default='S1')
    stu_learn_status = models.CharField(max_length=64, null=True, help_text='学习阶段', default='D2', choices=[(tag.name, tag.value) for tag in DegreeChoice])
    stu_grade = models.CharField(max_length=64, null=True, help_text='年级', default='1')
    stu_system = models.IntegerField(null=True, help_text='学制', default=3)
    stu_entrance_time = models.DateField(max_length=32, null=True, help_text='入学日期', default='2019-09')
    stu_graduation_time = models.DateField(max_length=32, null=True, help_text='毕业日期', default='2021-07')
    stu_cultivating_mode = models.CharField(max_length=128, null=True, help_text='培养方式', default='C1', choices=[(tag.name, tag.value) for tag in CultivatingMode])
    stu_enrollment_category = models.CharField(max_length=64, null=True, choices=[(tag.name, tag.value) for tag in EnrollmentCategory], help_text='录取类别', default='E1')
    stu_nationality = models.CharField(max_length=128, null=True, help_text='国籍', default='中国')
    stu_special_program = models.CharField(max_length=128, null=True, choices=[(tag.name, tag.value) for tag in SpecialProgram], help_text='专项计划', default='S1')
    stu_is_regular_income = models.BooleanField(default=False, help_text='是否有固定收入')
    stu_is_tuition_fees = models.BooleanField(default=False, help_text='是否欠缴学费')
    stu_is_archives = models.BooleanField(default=False, help_text='档案是否转到学校')
    stu_is_superb = models.BooleanField(default=False, help_text="是否优秀毕业生")
    stu_is_exemption = models.BooleanField(default=False, help_text="是否推免生")
    stu_is_adjust = models.BooleanField(default=False, help_text="是否调剂")
    stu_is_volunteer = models.BooleanField(default=True, help_text="是否第一志愿")
    stu_is_delay = models.BooleanField(default=True, help_text="是否延期（中期考核）")
    stu_delay_reason = models.CharField(max_length=255, null=True, help_text="中期考核延期原因")
    stu_mid_check = models.CharField(max_length=64, null=True, choices=[(tag.name, tag.value) for tag in MidCheckChoice], help_text="中期考核结果")
    stu_status = models.CharField(max_length=64, null=True, choices=[(tag.name, tag.value) for tag in StatusChoice], help_text="在学状态", default='S1')
    stu_gain_diploma = models.BooleanField(null=True, default=False, help_text="学位证")
    stu_gain_cert = models.BooleanField(null=True, default=False, help_text="毕业证")
    stu_tutor = models.ForeignKey(Tutor, null=True, related_name='stu_tutor', on_delete=models.SET_NULL, help_text="指导老师")
    stu_class = models.ForeignKey(Class, null=True, related_name='stu_class', on_delete=models.SET_NULL, help_text="所属班级")
    stu_major = models.ForeignKey(Major, null=True, related_name='stu_major', on_delete=models.SET_NULL, help_text="所属专业")
    stu_academy = models.ForeignKey(Academy, null=True, related_name='stu_academy', on_delete=models.SET_NULL, help_text='所属学院')
    stu_research = models.ForeignKey(Research, null=True, related_name='stu_research', on_delete=models.SET_NULL, help_text="科研方向")

    def __str__(self):
        return "学生编号：{0}  学生姓名：{1}".format(self.stu_number, self.user.first_name + self.user.last_name)

    class Meta:
        db_table = 'student'
        verbose_name = "学生"
        verbose_name_plural = verbose_name
        default_permissions = ()
        permissions = [
            ("can_insert_student", "新增学生"),
            ("can_delete_student", "删除学生"),
            ("can_update_student", "修改学生"),
            ("can_search_student", "查询学生")
        ]
        ordering = ['stu_number']


class MidCheckReport(models.Model):
    """
    中期考核统计模型
    """
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True, help_text="唯一标识ID")
    time = models.DateField(null=False, default='2019', help_text="年份")
    # stu_count = models.IntegerField(null=False, default=0, help_text="学生数量")  # 根据学生查处来
    schedule_count = models.IntegerField(null=False, default=0, help_text="按期考核人数")
    pass_count = models.IntegerField(null=False, default=0, help_text="延期考核人数")
    pass_proportion = models.IntegerField(null=False, default=0, help_text="延期考核比例")
    delay_count = models.IntegerField(null=False, default=0, help_text="延期考核人数")
    # delay_reason = models.TextField(null=False, default="", help_text="延期考核原因")  # 每个延期考核的学生都有自己的延期原因
    delay_proportion = models.IntegerField(null=False, default=0, help_text="延期考核比例")
    track_count = models.IntegerField(null=False, default=0, help_text="被跟踪人数")
    track_proportion = models.IntegerField(null=False, default=0, help_text="被跟踪比例")
    fail_count = models.IntegerField(null=False, default=0, help_text="不合格人数")
    fail_proportion = models.IntegerField(null=False, default=0, help_text="不合格比例")

    class Meta:
        db_table = 'mid_check_report'
        verbose_name = "中期考核统计"
        verbose_name_plural = verbose_name
        default_permissions = ()
        permissions = [
            ("can_insert_mid_check_report", "新增中期考核统计"),
            ("can_delete_mid_check_report", "删除中期考核统计"),
            ("can_update_mid_check_report", "修改中期考核统计"),
            ("can_search_mid_check_report", "查询中期考核统计")
        ]