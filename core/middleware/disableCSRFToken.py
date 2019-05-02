#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ==================================================
# @Time : 2019-05-02 11:26 
# @Author : ryuchen
# @Site :  
# @File : disablecsrf.py 
# @Desc : 
# ==================================================
from django.utils.deprecation import MiddlewareMixin


class DisableCSRF(MiddlewareMixin):

    def process_request(self, request):
        setattr(request, '_dont_enforce_csrf_checks', True)
