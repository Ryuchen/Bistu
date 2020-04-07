#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ==================================================
# @Time : 2019-04-02 20:22 
# @Author : ryuchen
# @Site :  
# @File : views.py 
# @Desc : 
# ==================================================
import xlrd
from datetime import datetime
from rest_framework import generics, status
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import make_password
from rest_framework.pagination import LimitOffsetPagination

from contrib.accounts.models import Tutor
from contrib.colleges.models import Major, Academy
from .serializers import TutorSerializers
from .serializers import AcademySerializer
from core.decorators.excepts import excepts
from apps.settings.views import trans_choice


def user_create(username, tut_number):
    user = dict()
    if username:
        user['username'] = str(int(tut_number))
        user['first_name'] = username[0:1]
        user['last_name'] = username[1:]
        user['password'] = make_password('123456')
        user['is_superuser'] = False
        user['is_staff'] = True
        user['is_active'] = False
    return user


class SimpleTutor(object):
    model = Tutor
    queryset = Tutor.objects.all()
    serializer_class = TutorSerializers
    pagination_class = LimitOffsetPagination
    filter_fields = ("tut_title", "tut_telephone", "tut_degree")


class TutorDetail(SimpleTutor, generics.RetrieveUpdateDestroyAPIView):
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
        serializer = self.get_serializer(instance, data=request.data, partial=partial,
                                         context={"academy": "", 'user': "", "education": ""})
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    @excepts
    @csrf_exempt
    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status.HTTP_200_OK)


class TutorList(SimpleTutor, generics.GenericAPIView):

    def get_queryset(self):
        queryset = self.queryset
        academy = self.request.query_params.get('academy')
        if academy:
            queryset = queryset.filter(academy__uuid=academy)
        # 姓名
        username = self.request.query_params.get('username')
        if username:
            queryset = queryset.filter(user__username=username)

        ordering = self.request.query_params.get('ordering')
        if ordering:
            queryset = queryset.order_by(ordering)
        return queryset

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

    @excepts
    @csrf_exempt
    def put(self, request, *args, **kwargs):
        """ TODO """
        data = request.data
        data["tut_user"] = user_create(data.get('tut_name'), data.get('tut_number'))
        data["tut_academy"] = Academy.objects.get(uuid=data.get("academy"))
        serializer = self.get_serializer(data=data, context={"tut_academy": "", 'tut_user': "", "tut_education": ""})
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @excepts
    @csrf_exempt
    def post(self, request, *args, **kwargs):
        trans = trans_choice()
        file = request.data['file']
        data = xlrd.open_workbook(filename=None, file_contents=file.read())
        table = data.sheets()[0]
        nrows = table.nrows  # 获取该sheet中的有效行数
        t_list = list()
        for i in range(1, nrows):
            row = table.row_values(i)
            t_dict = dict()
            t_dict["tut_number"] = int(row[0]) if row[0] else 0
            t_dict["tut_user"] = user_create(row[1], int(row[0]))
            t_dict["tut_gender"] = trans[row[2]]
            t_dict["tut_political"] = trans[row[3]]
            t_dict["tut_title"] = trans[row[4]]
            t_dict["tut_birth_day"] = datetime.strptime(str(int(row[5])), '%Y%m%d').strftime('%Y-%m-%d')
            t_dict["tut_degree"] = trans[row[6]]
            t_dict["tut_academy"] = Academy.objects.filter(aca_cname=row[7]).first()
            t_dict["tut_cardID"] = row[8]
            t_dict["tut_entry_day"] = datetime.strptime(str(int(row[9])), '%Y%m').strftime('%Y-%m-01')
            t_dict["tut_telephone"] = row[10]
            t_list.append(t_dict)
        serializer = self.get_serializer(data=t_list, many=True, context={"tut_academy": "", 'tut_user': "", "tut_education": ""})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
