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
from contrib.academy.models import Academy, Major, Research


class Education(models.Model):
    """
    学历模型
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
        verbose_name = "学历"
        verbose_name_plural = verbose_name


class Class(models.Model):
    """
    班级模型
    """
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True, help_text="唯一标识ID")
    cla_name = models.CharField(max_length=128, null=False, help_text="班级名称")
    cla_code = models.IntegerField(null=True, help_text="班级代码")

    def __str__(self):
        return "代码：{0}  名称：{1}".format(self.cla_code, self.cla_name)

    class Meta:
        verbose_name = "班级"
        verbose_name_plural = verbose_name


class Tutor(models.Model):
    """
    导师模型
    """
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True, help_text="唯一标识ID")
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name='user')
    tut_number = models.IntegerField(null=False, unique=True, help_text="导师工号")
    tut_gender = models.CharField(max_length=64, choices=sorted([(tag.name, tag.value) for tag in GenderChoice]),
                                  help_text="性别")
    tut_title = models.CharField(max_length=64, choices=sorted([(tag.name, tag.value) for tag in TitleChoice]),
                                 help_text="职称")
    tut_cardID = models.CharField(max_length=128, null=True, unique=True, help_text="身份证号")
    tut_birth_day = models.DateField(help_text="出生日期", )
    tut_entry_day = models.DateField(help_text="入职日期")
    tut_political = models.CharField(max_length=64, choices=sorted([(tag.name, tag.value) for tag in PoliticalChoice]),
                                     help_text="政治面貌")
    tut_telephone = models.IntegerField(null=True, help_text="电话号码")
    tut_degree = models.CharField(max_length=64, choices=sorted([(tag.name, tag.value) for tag in DegreeChoice]),
                                  help_text="学位")
    education = models.ForeignKey(Education, null=True, on_delete=True, related_name='education', help_text="学历")
    academy = models.ForeignKey(Academy, null=True, on_delete=models.CASCADE, related_name='academy', help_text="所属学院")

    def __str__(self):
        return "工号：{0}  姓名：{1}".format(self.tut_number, self.user.first_name + self.user.last_name)

    class Meta:
        verbose_name = "导师"
        verbose_name_plural = verbose_name
        ordering = ['tut_number']


class Student(models.Model):
    """
    学生模型
    """
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True, help_text="唯一标识ID")
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name='stu_user')
    stu_number = models.IntegerField(null=False, unique=True, default='20190101', help_text="学号")
    stu_avatar = models.ImageField(null=True, help_text="学生照片")
    stu_gender = models.CharField(max_length=64, null=True, choices=[(tag.name, tag.value) for tag in GenderChoice], help_text="性别")
    stu_card_type = models.CharField(max_length=128, null=False, help_text='身份证件类型', default="身份证")
    stu_cardID = models.CharField(max_length=128, null=True, unique=True, help_text="身份证号", default="12345")
    stu_candidate_number = models.CharField(max_length=128, null=True, help_text="考生号")
    stu_birth_day = models.CharField(max_length=64, null=True, help_text="出生日期", default='201909')
    stu_nation = models.CharField(max_length=64, null=False, help_text='民族', default='汉')
    stu_source = models.CharField(max_length=128, null=True, help_text="生源地")
    stu_is_village = models.BooleanField(default=False, help_text='是否农村学生')
    stu_political = models.CharField(max_length=64, null=True, choices=[(tag.name, tag.value) for tag in PoliticalChoice], help_text="政治面貌")
    stu_type = models.CharField(max_length=128, null=False, choices=[(tag.name, tag.value) for tag in StudentType], help_text='学生类型', default='S1')
    stu_learn_type = models.CharField(max_length=64, null=False, choices=[(tag.name, tag.value) for tag in StudentCategory], help_text='学习形式', default='S1')
    stu_learn_status = models.CharField(max_length=64, null=False, help_text='学习阶段', default='D2', choices=[(tag.name, tag.value) for tag in DegreeChoice])
    stu_grade = models.CharField(max_length=64, null=False, help_text='年级', default='1')
    stu_system = models.IntegerField(null=False, help_text='学制', default=3)
    stu_entrance_time = models.CharField(max_length=32, null=False, help_text='入学日期', default='2019-09')
    stu_graduation_time = models.CharField(max_length=32, null=False, help_text='毕业日期', default='2021-07')
    stu_cultivating_mode = models.CharField(max_length=128, null=False, help_text='培养方式', default='C1', choices=[(tag.name, tag.value) for tag in CultivatingMode])
    stu_enrollment_category = models.CharField(max_length=64, null=False, choices=[(tag.name, tag.value) for tag in EnrollmentCategory], help_text='录取类别', default='E1')
    stu_nationality = models.CharField(max_length=128, null=False, help_text='国籍', default='中国')
    stu_special_program = models.CharField(max_length=128, null=False, choices=[(tag.name, tag.value) for tag in SpecialProgram], help_text='专项计划', default='S1')
    stu_is_regular_income = models.BooleanField(default=False, help_text='是否有固定收入')
    stu_is_tuition_fees = models.BooleanField(default=False, help_text='是否欠缴学费')
    stu_is_archives = models.BooleanField(default=False, help_text='档案是否转到学校')
    stu_is_superb = models.BooleanField(default=False, help_text="是否优秀毕业生")
    stu_telephone = models.IntegerField(null=True, help_text="电话号码")
    stu_status = models.CharField(max_length=64, null=False, choices=[(tag.name, tag.value) for tag in StatusChoice], help_text="在学状态", default='S1')
    stu_class = models.CharField(max_length=128, null=True, help_text="所属班级")
    tutor = models.ForeignKey(Tutor, null=True, related_name='stu_tutor', on_delete=models.SET_NULL, help_text="指导老师")
    academy = models.ForeignKey(Academy, null=True, related_name='stu_academy', on_delete=models.SET_NULL, help_text='所属学院')
    major_category = models.CharField(max_length=128, null=True, choices=[(tag.name, tag.value) for tag in MajorDegree], help_text='专业大类', default='D1')
    major = models.ForeignKey(Major, null=True, related_name='stu_major', on_delete=models.SET_NULL, help_text="学科专业")
    research = models.ForeignKey(Research, null=True, related_name='stu_research', on_delete=models.SET_NULL, help_text="科研方向")

    def __str__(self):
        return "学生编号：{0}     学生姓名：{1}".format(self.stu_number, self.user.first_name + self.user.last_name)

    class Meta:
        verbose_name = "学生"
        verbose_name_plural = verbose_name
        ordering = ['stu_number']
