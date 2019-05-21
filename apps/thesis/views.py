#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ==================================================
# @Time : 2019-04-02 20:22
# @Author : ryuchen
# @Site :
# @File : views.py
# @Desc :
# ==================================================
from rest_framework import generics
from rest_framework.response import Response

from django.views.decorators.csrf import csrf_exempt

from contrib.accounts.models import Student
from contrib.education.models import Thesis
from core.decorators.excepts import excepts
from .serializers import ThesisSerializers


class SimpleThesis(object):
    model = Thesis
    queryset = Thesis.objects.all()
    serializer_class = ThesisSerializers
    pagination_class = None


class ThesisDetail(SimpleThesis, generics.RetrieveUpdateDestroyAPIView):
    @excepts
    @csrf_exempt
    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class ThesisList(SimpleThesis, generics.GenericAPIView):

    @excepts
    @csrf_exempt
    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        else:
            serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    # 添加
    # @excepts
    # @csrf_exempt
    def post(self, request, *args, **kwargs):
        data = request.data
        bulk = isinstance(data, list)
        if not bulk:
            stu_number = data.get('stu_number')
            data["student"] = Student.objects.filter(stu_number=stu_number).first()
            serializer = self.get_serializer(data=data, context={"thesis": ""})
        else:
            for item in data:
                stu_number = item['student']
                item["student"] = Student.objects.filter(stu_number=stu_number).first()
            serializer = self.get_serializer(data=data, many=True, context={"thesis": ""})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

