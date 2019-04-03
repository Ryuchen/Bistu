#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ==================================================
# @Time : 2019-04-02 11:25 
# @Author : ryuchen
# @Site :  
# @File : errors.py 
# @Desc : 
# ==================================================
import json

from rest_framework import status


class ForbiddenError(Exception):
    code = status.HTTP_403_FORBIDDEN
    details = ""

    def __init__(self, details=None):
        if type(details) is str:
            self.details = json.loads(details)
        else:
            self.details = details

