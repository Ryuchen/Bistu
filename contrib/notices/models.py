#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ==================================================
# @Time : 2020/4/4-15:37
# @Author : Ryuchen
# @Site : https://ryuchen.github.io
# @File : models.py
# @Desc : 
# ==================================================
import uuid

from django.db import models
from django.contrib.auth.models import User


class Notices(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, verbose_name="唯一标识ID")
    notice_create_user = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name='notice_create_user', verbose_name="创建者")
    notice_relate_user = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name='notice_relate_user', verbose_name="指定者")
    notice_content = models.TextField(null=True, verbose_name="消息内容")
    notice_create_time = models.DateTimeField(null=True, verbose_name='创建时间')
    notice_expire_time = models.DateTimeField(null=True, verbose_name='过期时间')
    notice_is_read = models.BooleanField(default=False, null=True, verbose_name="是否已读")
    notice_is_deleted = models.BooleanField(default=False, null=True, verbose_name="是否删除")
    notice_is_finished = models.BooleanField(default=False, null=True, verbose_name="是否完成")
    notice_is_broadcast = models.BooleanField(default=False, null=True, verbose_name="是否广播")

    def __str__(self):
        return "消息:《{0}》创建者: {1}".format(self.notice_content, self.notice_create_user)

    class Meta:
        db_table = 'notices'
        verbose_name = "消息通知"
        verbose_name_plural = verbose_name
        default_permissions = ()
        permissions = [
            ("can_insert_notice", "新增消息通知"),
            ("can_delete_notice", "删除消息通知"),
            ("can_update_notice", "修改消息通知"),
            ("can_search_notice", "查询消息通知")
        ]
