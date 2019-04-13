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
from rest_framework import generics, status
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import make_password
from rest_framework.pagination import LimitOffsetPagination

from contrib.users.models import Tutor
from contrib.academy.models import Major
from .serializers import TutorSerializers
from core.decorators.excepts import excepts


def user_chanle(username, tut_number):
    user = dict()
    if username:
        user['username'] = str(int(tut_number))
        user['first_name'] = username
        user['last_name'] = username
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
    filterset_fields = ("tut_title", "tut_telephone", "tut_degree")
    ordering_fields = ('tut_number', 'tut_birth_day', 'tut_entry_day')


class TutorDetail(SimpleTutor, generics.RetrieveUpdateDestroyAPIView):
    @excepts
    @csrf_exempt
    def get(self, request, *args, **kwargs):
        res = {
            "code": "00000000",
            "data": {
                "status": 200,
            }
        }
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        res['data'] = serializer.data
        return Response(res)

    @excepts
    @csrf_exempt
    def put(self, request, *args, **kwargs):
        res = {
            "code": "00000000",
            "data": {
                "status": 200,
            }
        }
        data = request.data
        username = data.get('user')
        data["user"] = user_chanle(username)
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=data, partial=partial,
                                         context={"academy": "", 'user': "", "education": ""})
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(res)

    @excepts
    @csrf_exempt
    def delete(self, request, *args, **kwargs):
        res = {
            "code": "00000000",
            "data": {
                "status": 200,
            }
        }
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(res)


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
        return queryset

    @excepts
    @csrf_exempt
    def get(self, request, *args, **kwargs):
        res = {
            'code': status.HTTP_200_OK,
            'data': []
        }
        queryset = self.get_queryset()
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
        else:
            serializer = self.get_serializer(queryset, many=True)
        res["data"] = serializer.data

        return Response(res)

    # 添加
    @excepts
    @csrf_exempt
    def post(self, request, *args, **kwargs):
        res = {
            'code': status.HTTP_200_OK,
            'data': {}
        }
        data = request.data
        bulk = isinstance(data, list)
        if not bulk:
            username = data.get('user')
            data["user"] = user_chanle(username)
            data["majors"] = Major.objects.filter(maj_name=data.get('majors')).filter()
            serializer = self.get_serializer(data=data, context={"academy": "", 'user': "", "education": ""})
        else:
            for item in data:
                username = item['user']
                item["user"] = user_chanle(username)
                data["majors"] = Major.objects.filter(maj_name=item.get('majors')).filter()
            serializer = self.get_serializer(data=data, many=True, context={"academy": "", "user": ""})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        res['data'] = serializer.data
        return Response(res)

    @excepts
    @csrf_exempt
    def put(self, request, *args, **kwargs):
        res = {
            'code': status.HTTP_200_OK,
            'data': {}
        }
        file = request.data['file']
        data = xlrd.open_workbook(filename=None, file_contents=file.read())
        table = data.sheets()[0]
        nrows = table.nrows  # 获取该sheet中的有效行数
        t_list = list()
        for i in range(1, nrows):
            row = table.row_values(i)
            t_dict = dict()
            t_dict["tut_number"] = int(row[0]) if row[0] else 0
            t_dict["user"] = user_chanle(row[1], int(row[0]))
            t_dict["tut_gender"] = row[2]
            t_dict["tut_political"] = row[3]
            t_dict["tut_title"] = row[4]
            t_dict["tut_birth_day"] = str(xlrd.xldate_as_datetime(row[5], 'YYYY-MM-DD'))[0:10]
            t_dict["tut_degree"] = row[6]
            t_dict["academy"] = Major.objects.filter(maj_name=row[7]).uuid
            t_dict["tut_cardID"] = row[8]
            t_dict["tut_entry_day"] = str(xlrd.xldate_as_datetime(row[9], 'YYYY-MM-DD'))[0:10]
            t_dict["tut_telephone"] = row[10]

            t_list.append(t_dict)
        serializer = self.get_serializer(data=t_list, many=True, context={"academy": "", 'user': "", "education": ""})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        res['data'] = serializer.data
        return Response(res)
