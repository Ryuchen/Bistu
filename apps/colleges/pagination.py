#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ==================================================
# @Time : 2020/4/6-15:08
# @Author : Ryuchen
# @Site : https://ryuchen.github.io
# @File : pagination.py
# @Desc : 
# ==================================================
from rest_framework.pagination import PageNumberPagination


class StandardPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 100
