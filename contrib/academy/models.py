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


class Research(models.Model):
    """
    研究方向模型
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
    学科专业模型
    """
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True, help_text="唯一标识ID")
    maj_name = models.CharField(max_length=128, null=True, help_text="学科专业名称")
    maj_code = models.IntegerField(null=True, help_text="学科专业编号")
    research = models.ManyToManyField(Research, help_text="科研方向")

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
    aca_name = models.CharField(max_length=128, null=True, help_text="学院名称")
    aca_code = models.IntegerField(null=True, help_text="学院代码")
    major = models.ManyToManyField(Major)

    def __str__(self):
        return str(self.aca_code) + self.aca_name

    class Meta:
        verbose_name = "学院"
        verbose_name_plural = verbose_name
