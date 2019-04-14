#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ==================================================
# @Time : 2019-04-02 20:11 
# @Author : libin
# @Site :  
# @File : views.py
# @Desc : 
# ==================================================
import xlrd
from datetime import datetime
from rest_framework.response import Response
from rest_framework import mixins, generics, status
from django.views.decorators.csrf import csrf_exempt
from rest_framework.pagination import LimitOffsetPagination

from core.decorators.excepts import excepts
from apps.teachers.views import user_chanle
from contrib.users.models import Student, Tutor
from contrib.academy.models import Academy, Major
from apps.students.serializers import StudentSerializers


class SimpleStudent(object):
    model = Student
    queryset = Student.objects.all()
    serializer_class = StudentSerializers
    pagination_class = LimitOffsetPagination
    filterset_fields = ('stu_number', 'stu_gender', 'stu_cardID', 'stu_candidate_number', 'stu_nation', 'stu_source',
                        'stu_is_village', 'stu_political', 'stu_type', 'stu_learn_type', 'stu_learn_status',
                        'stu_grade', 'stu_system', 'stu_entrance_time', 'stu_graduation_time', 'stu_cultivating_mode',
                        'stu_enrollment_category', 'stu_nationality', 'stu_special_program', 'stu_is_regular_income',
                        'stu_is_tuition_fees', 'stu_is_archives', 'stu_is_superb', 'stu_telephone', 'stu_status',
                        'stu_class', 'major_category', 'stu_name',)
    ordering = ('stu_number',)
    ordering_fields = ('stu_number', 'stu_entrance_time', 'stu_graduation_time', 'stu_birth_day',)


class StudentDetail(SimpleStudent, generics.RetrieveUpdateDestroyAPIView):

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
        username = data.get('user')
        data["user"] = user_chanle(username)
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=data, partial=partial,
                                         context={"stu_academy": "", 'stu_user': "", "stu_major": "", "stu_tutor": ""})
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    @excepts
    @csrf_exempt
    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status.HTTP_200_OK)


class StudentList(SimpleStudent, mixins.ListModelMixin, generics.GenericAPIView):

    def get_queryset(self):
        queryset = self.queryset
        params = self.request.query_params
        if params:
            academy = params.get('academy')
            if academy:
                queryset = queryset.filter(academy__uuid=academy)

            major = params.get('major')
            if major:
                queryset = queryset.filter(major__uuid=major)

            tutor = params.get('tutor')
            if tutor:
                queryset = queryset.filter(tutor__user__username=tutor)
            ordering = self.request.query_params.get('ordering')
            if ordering:
                queryset = queryset.order_by(ordering)
        return queryset

    @excepts
    @csrf_exempt
    def get(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    # 添加
    @excepts
    @csrf_exempt
    def post(self, request, *args, **kwargs):
        data = request.data
        bulk = isinstance(data, list)
        if not bulk:
            username = data.get('user')
            data["user"] = user_chanle(username)
            data["stu_major"] = Major.objects.filter(maj_name=data.get('stu_major')).first()
            data["stu_academy"] = Academy.objects.filter(aca_cname=data.get('stu_academy')).first()
            data["tutor"] = Tutor.objects.filter(user__first_name=data.get('tutor')).first()
            serializer = self.get_serializer(data=data, context={"stu_academy": "", 'stu_user': "", "stu_major": "",
                                                                 "stu_tutor": ""})
        else:
            for item in data:
                username = item['user']
                item["user"] = user_chanle(username)
                data["stu_major"] = Major.objects.filter(maj_name=item['stu_major']).first()
                data["stu_academy"] = Academy.objects.filter(aca_cname=item['stu_academy']).first()
                data["tutor"] = Tutor.objects.filter(user__first_name=data.get('tutor')).first()
            serializer = self.get_serializer(data=data, many=True,
                                             context={"stu_academy": "", 'stu_user': "", "stu_major": "",
                                                      "stu_tutor": ""})
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
        s_list = list()
        for i in range(1, nrows):
            rowx = table.row_values(i)
            student_dict = dict()
            student_dict["user"] = user_chanle(rowx[0], rowx[1])
            student_dict["stu_name"] = rowx[0]
            student_dict["stu_number"] = rowx[1]
            student_dict["stu_candidate_number"] = rowx[2]
            student_dict["stu_card_type"] = rowx[3]
            student_dict["stu_cardID"] = rowx[4]
            student_dict["stu_gender"] = rowx[5]
            student_dict["stu_birth_day"] = datetime.strptime(str(int(rowx[6])), '%Y%m%d').strftime('%Y-%m-%d')
            student_dict["stu_nation"] = rowx[7]
            student_dict["stu_source"] = rowx[8]
            student_dict["stu_is_village"] = True if rowx[9] == "是" else False
            student_dict["stu_political"] = rowx[10]
            student_dict["academy"] = Academy.objects.filter(aca_cname=rowx[11]).first()
            student_dict["major"] = Major.objects.filter(maj_name=rowx[12]).first()
            student_dict["major_category"] = rowx[13]
            student_dict["stu_class"] = rowx[14]
            student_dict["stu_status"] = rowx[15]
            student_dict["tutor"] = Tutor.objects.filter(user__first_name=rowx[16][:1]).filter(user__last_name=rowx[16][1:]).first()
            student_dict["stu_type"] = rowx[17]
            student_dict["stu_learn_type"] = rowx[18]
            student_dict["stu_learn_status"] = rowx[19]
            student_dict["stu_grade"] = rowx[20]
            student_dict["stu_system"] = rowx[21]
            student_dict["stu_entrance_time"] = datetime.strptime(str(int(rowx[22])), '%Y%m').strftime('%Y-%m-01')
            student_dict["stu_cultivating_mode"] = rowx[23]
            student_dict["stu_enrollment_category"] = rowx[24]
            student_dict["stu_nationality"] = rowx[25]
            student_dict["stu_special_program"] = rowx[26]
            student_dict["stu_is_regular_income"] = True if rowx[27] == "是" else False
            student_dict["stu_is_tuition_fees"] = True if rowx[28] == "是" else False
            student_dict["stu_is_archives"] = True if rowx[29] == "是" else False
            student_dict["stu_graduation_time"] = datetime.strptime(str(int(rowx[30])), '%Y%m').strftime('%Y-%m-01')
            s_list.append(student_dict)
        serializer = self.get_serializer(data=s_list, many=True, context={"stu_academy": "", 'stu_user': "",
                                                                          "stu_major": "", "stu_tutor": ""})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class StudentStatistics(generics.GenericAPIView):
    @excepts
    @csrf_exempt
    def get(self, request, *args, **kwargs):
        student = Student.objects.all()
        majors = Academy.objects.all().values('aca_cname', 'majors__maj_name', 'majors__maj_type', 'majors__maj_code')
        s_list = list()
        for item in majors:
            s_dict = dict(name="", major={}, count=0)
            s_dict['count'] = student.filter(academy__aca_cname=item['aca_cname']).count()
            aca_student = student.filter(academy__aca_cname=item['aca_cname']).filter(
                major__maj_name=item['majors__maj_name'])
            s_dict['name'] = item['aca_cname']
            s_dict['code'] = item['majors__maj_code']
            s_dict['major']['name'] = item['majors__maj_name']
            s_dict['major']['type'] = item['majors__maj_type']
            s_dict['major']['maj_code'] = item['majors__maj_code']
            s_dict['major']['count'] = aca_student.count()
            s_dict['major']['col_1'] = aca_student.filter(stu_learn_type='S1').filter(stu_learn_status='C2').count()
            s_dict['major']['col_2'] = aca_student.filter(stu_learn_type='S1').filter(stu_learn_status='C1').count()
            s_dict['major']['col_3'] = aca_student.filter(stu_learn_type='S2').filter(stu_learn_status='C1').count()
            s_dict['major']['col_4'] = aca_student.filter(volunteer=True).count()
            s_dict['major']['col_5'] = aca_student.filter(exemption=True).count()
            s_dict['major']['col_6'] = aca_student.filter(adjust=True).count()
            s_dict['major']['col_7'] = aca_student.filter(stu_special_program='S3').count()
            s_list.append(s_dict)
        return Response(s_list)
