#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ==================================================
# @Time : 2019-05-01 11:30 
# @Author : ryuchen
# @Site :  
# @File : displays.py 
# @Desc : 
# ==================================================
from django.utils import six


def permissions_display(self):
    permission_category = six.text_type(self.content_type.app_label)
    permission_class = six.text_type(self.content_type)
    permission_describe = six.text_type(self.name)
    return '%s: %s -> %s' % (permission_category, permission_class.title(), permission_describe)
