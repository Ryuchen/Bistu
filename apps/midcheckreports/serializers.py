#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ==================================================
# @Time : 2019-05-06 15:30 
# @Author : libin
# @Site :  
# @File : serializers.py 
# @Desc : 
# ==================================================
from rest_framework import serializers
from contrib.accounts.models import MidCheckReport


class MidCheckReportSerializers(serializers.ModelSerializer):
    """ 研究生中期考核情况统计 """

    class Meta:
        model = MidCheckReport
        fields = '__all__'

