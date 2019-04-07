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
        verbose_name = "研究方向"
        verbose_name_plural = verbose_name


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
        verbose_name = "学科专业"
        verbose_name_plural = verbose_name


class Academy(models.Model):
    """
    学院模型
    """
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True, help_text="唯一标识ID")
    # aca_avatar = models.ImageField(help_text="学院图标", null=False)
    aca_avatar = models.CharField(max_length=128, help_text="学院图标", null=True)
    aca_nickname = models.CharField(max_length=128, null=True, help_text="学院简称")
    aca_cname = models.CharField(max_length=128, null=True, help_text="学院名称(中)")
    aca_ename = models.CharField(max_length=128, null=True, help_text="学院名称(英)")
    aca_code = models.IntegerField(null=True, help_text="学院代码")
    aca_phone = models.CharField(max_length=128, null=True, help_text="学院电话")
    aca_fax = models.CharField(max_length=128, null=True, help_text="学院传真")
    aca_href = models.URLField(max_length=256, null=True, help_text="学院网址")
    aca_brief = models.TextField(help_text="学院简介")
    # aca_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, help_text="学院负责人")
    aca_user = models.CharField(max_length=64, null=True, help_text="学院负责人")
    majors = models.ManyToManyField(Major, related_name='majors')

    def __str__(self):
        return str(self.aca_code) + self.aca_cname

    class Meta:
        verbose_name = "学院"
        verbose_name_plural = verbose_name
