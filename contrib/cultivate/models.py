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


class Thesis(models.Model):
    """
    毕业论文模型
    """
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True, help_text="唯一标识ID")
    the_title = models.CharField(max_length=128, null=False, help_text="课题名称")
    the_start_time = models.DateField(help_text="开题时间")
    the_mid_score = models.CharField(max_length=64, help_text="中期考核结果")
    the_start_score = models.CharField(max_length=64, help_text="开题结果")
    the_check_score = models.CharField(max_length=64, help_text="查重结果")
    the_blind_score1 = models.CharField(max_length=64, help_text="盲审结果1")
    the_blind_score2 = models.CharField(max_length=64, help_text="盲审结果2")
    the_final_score = models.CharField(max_length=64, help_text="答辩成绩")
    the_is_superb = models.BooleanField(default=False, help_text="是否优秀论文")

    def __str__(self):
        return "论文课题：{0}".format(self.the_title)

    class Meta:
        verbose_name = "论文"
        verbose_name_plural = verbose_name
