#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ==================================================
# @Time : 2019-04-02 11:25 
# @Author : ryuchen
# @Site :  
# @File : errors.py 
# @Desc : 
# ==================================================
from rest_framework import status


class AuthenticateError(Exception):
    code = status.HTTP_400_BAD_REQUEST
    details = ""

    def __init__(self, details=None):
        self.details = details


class ForbiddenError(Exception):
    code = status.HTTP_403_FORBIDDEN
    details = ""

    def __init__(self, details=None):
        self.details = details

