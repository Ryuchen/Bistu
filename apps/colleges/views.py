#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ==================================================
# @Time : 2019-04-02 20:11 
# @Author : ryuchen
# @Site :  
# @File : views.py
# @Desc : 
# ==================================================
import xlrd
from rest_framework import generics, status
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from core.decorators.excepts import excepts
from django.contrib.auth.models import User
from contrib.academy.models import Academy, Major, Research
from .serializers import MajorSerializers, AcademySerializers, ResearchSerializers


# 科研方向
class SimpleResearch(object):
    model = Research
    queryset = Research.objects.all()
    serializer_class = ResearchSerializers
    pagination_class = None


class ResearchDetail(SimpleResearch, generics.RetrieveUpdateDestroyAPIView):
    @excepts
    @csrf_exempt
    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    @excepts
    @csrf_exempt
    def put(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    @excepts
    @csrf_exempt
    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_200_OK)


class ResearchList(SimpleResearch, generics.GenericAPIView):
    @excepts
    @csrf_exempt
    def get(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
        else:
            serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    # 添加
    @excepts
    @csrf_exempt
    def post(self, request, *args, **kwargs):
        data = request.data
        bulk = isinstance(data, list)
        if not bulk:
            serializer = self.get_serializer(data=data)
        else:
            serializer = self.get_serializer(data=data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    @excepts
    @csrf_exempt
    def put(self, request, *args, **kwargs):
        file = request.data['file']
        data = xlrd.open_workbook(filename=None, file_contents=file.read())
        table = data.sheets()[0]
        nrows = table.nrows  # 获取该sheet中的有效行数
        m_list = list()
        for i in range(1, nrows):
            row = table.row_values(i)
            m_dict = dict()
            m_dict["maj_code"] = row[0]
            m_dict["maj_name"] = row[1]
            m_dict["maj_type"] = row[2]
            m_list.append(m_dict)
        serializer = self.get_serializer(data=m_list, many=True, context={"research": ""})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


# 专业
class SimpleMajor(object):
    model = Major
    queryset = Major.objects.all()
    serializer_class = MajorSerializers
    pagination_class = None


class MajorDetail(SimpleMajor, generics.RetrieveUpdateDestroyAPIView):
    @excepts
    @csrf_exempt
    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    @excepts
    @csrf_exempt
    def put(self, request, *args, **kwargs):
        data = request.data
        data["research"] = [i.uuid for i in Research.objects.filter(res_name__in=data.get('research').split(","))]
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=data, partial=partial, context={"research": ""})
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    @excepts
    @csrf_exempt
    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status.HTTP_200_OK)


class MajorList(SimpleMajor, generics.GenericAPIView):
    @excepts
    @csrf_exempt
    def get(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
        else:
            serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    # 添加
    @excepts
    @csrf_exempt
    def post(self, request, *args, **kwargs):
        data = request.data
        bulk = isinstance(data, list)

        if not bulk:
            data["research"] = [i.uuid for i in Research.objects.filter(res_name__in=data.get('research').split(","))]
            serializer = self.get_serializer(data=data, context={"research": ""})
        else:
            for item in data.get('research'):
                data["research"] = [i.uuid for i in
                                    Research.objects.filter(res_name__in=item.get('research').split(","))]
            serializer = self.get_serializer(data=data, many=True, context={"research": ""})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    @excepts
    @csrf_exempt
    def put(self, request, *args, **kwargs):
        file = request.data['file']
        data = xlrd.open_workbook(filename=None, file_contents=file.read())
        table = data.sheets()[0]
        nrows = table.nrows  # 获取该sheet中的有效行数
        m_list = list()
        for i in range(1, nrows):
            row = table.row_values(i)
            m_dict = dict()
            m_dict["maj_code"] = row[0]
            m_dict["maj_name"] = row[1]
            m_dict["maj_type"] = row[2]
            m_list.append(m_dict)
        serializer = self.get_serializer(data=m_list, many=True, context={"research": ""})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


# 学院
class SimpleAcademy(object):
    model = Academy
    queryset = Academy.objects.all()
    serializer_class = AcademySerializers
    pagination_class = None


class AcademyDetail(SimpleAcademy, generics.RetrieveUpdateDestroyAPIView):
    @excepts
    @csrf_exempt
    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    @excepts
    @csrf_exempt
    def put(self, request, *args, **kwargs):
        data = request.data
        data["aca_user"] = User.objects.get(username=data.get('aca_user')).id
        data["majors"] = [i.uuid for i in Major.objects.filter(maj_name__in=data.get('majors').split(","))]
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    @excepts
    @csrf_exempt
    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status.HTTP_200_OK)


class AcademyList(SimpleAcademy, generics.GenericAPIView):
    @excepts
    @csrf_exempt
    def get(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
        else:
            serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    # 添加
    @excepts
    @csrf_exempt
    def post(self, request, *args, **kwargs):
        data = request.data
        bulk = isinstance(data, list)
        if not bulk:
            data["aca_user"] = User.objects.get(username=data.get('aca_user')).id
            data["majors"] = [i.uuid for i in Major.objects.filter(maj_name__in=data.get('majors').split(","))]
            serializer = self.get_serializer(data=data, context={"majors": "", "aca_user": ""})
        else:
            for item in data:
                data["aca_user"] = User.objects.get(username=item.get('aca_user')).id
                data["majors"] = [i.uuid for i in Major.objects.filter(maj_name__in=item.get('majors').split(","))]
            serializer = self.get_serializer(data=data, many=True, context={"majors": "", "aca_user": ""})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    @excepts
    @csrf_exempt
    def put(self, request, *args, **kwargs):
        file = request.data['file']
        data = xlrd.open_workbook(filename=None, file_contents=file.read())
        table = data.sheets()[0]
        nrows = table.nrows  # 获取该sheet中的有效行数
        m_list = list()
        for i in range(1, nrows):
            row = table.row_values(i)
            m_dict = dict()
            m_dict["aca_code"] = int(row[0]) if row[0] else 0
            m_dict["aca_name"] = row[1]
            m_dict["majors"] = row[2].split('、')
            m_list.append(m_dict)
        serializer = self.get_serializer(data=m_list, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
