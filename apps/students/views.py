#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ==================================================
# @Time : 2019-04-02 20:11 
# @Author : libin
# @Site :  
# @File : views.py
# @Desc : 
# ==================================================
import os

import xlrd
import xlwt
from datetime import datetime

from django.conf import settings
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import mixins, generics, status
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from rest_framework.pagination import LimitOffsetPagination

from core.decorators.excepts import excepts
from apps.teachers.views import user_create
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
        data["user"] = user_create(username)
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
                queryset = queryset.filter(tutor__uuid=tutor)
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
    def put(self, request, *args, **kwargs):
        data = request.data
        bulk = isinstance(data, list)
        if not bulk:
            username = data.get('user')
            data["user"] = user_create(username)
            data["stu_major"] = Major.objects.filter(maj_name=data.get('stu_major')).first()
            data["stu_academy"] = Academy.objects.filter(aca_cname=data.get('stu_academy')).first()
            data["tutor"] = Tutor.objects.filter(user__first_name=data.get('tutor')).first()
            serializer = self.get_serializer(data=data, context={"stu_academy": "", 'stu_user': "", "stu_major": "",
                                                                 "stu_tutor": ""})
        else:
            for item in data:
                username = item['user']
                item["user"] = user_create(username)
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
    def post(self, request, *args, **kwargs):
        file = request.data['file']
        data = xlrd.open_workbook(filename=None, file_contents=file.read())
        table = data.sheets()[0]
        nrows = table.nrows  # 获取该sheet中的有效行数
        s_list = list()
        for i in range(1, nrows):
            rowx = table.row_values(i)
            student_dict = dict()
            student_dict["user"] = user_create(rowx[0], rowx[1])
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
        year = request.GET.get("year", "")
        if year:
            student = Student.objects.filter(stu_entrance_time__year=year).all()
        else:
            student = Student.objects.all()
        majors = Academy.objects.all().values('aca_cname', 'majors__maj_name', 'majors__maj_type', 'majors__maj_code')
        s_list = list()
        for item in majors:
            s_dict = dict(name="", major={}, count=0)
            s_dict['count'] = student.filter(academy__aca_cname=item['aca_cname']).count()
            aca_student = student.filter(academy__aca_cname=item['aca_cname']).filter(major__maj_name=item['majors__maj_name'])
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


# @excepts
# @csrf_exempt
@api_view(['GET'])
def create_xls(request):
    year = request.GET.get("year", "")

    # 创建一个workbook 设置编码
    workbook = xlwt.Workbook(encoding='utf-8')
    # 创建一个worksheet
    worksheet = workbook.add_sheet('worksheet')
    alignment = xlwt.Alignment()
    alignment.horz = xlwt.Alignment.HORZ_CENTER
    alignment.vert = xlwt.Alignment.VERT_CENTER

    # 写入excel
    # 第一行
    header_style = xlwt.XFStyle()
    header_font = xlwt.Font()
    header_font.bold = True
    header_style.font = header_font
    header_style.alignment = alignment
    # 表格数据居中
    table_center_style = xlwt.XFStyle()
    table_center_style.alignment = alignment
    # 表格数据居左
    table_left_style = xlwt.XFStyle()
    table_left_alignment = xlwt.Alignment()
    table_left_alignment.horz = xlwt.Alignment.HORZ_LEFT
    table_left_alignment.vert = xlwt.Alignment.VERT_CENTER
    table_left_style.alignment = table_left_alignment
    # 表格数据居右
    table_right_style = xlwt.XFStyle()
    table_right_alignment = xlwt.Alignment()
    table_right_alignment.horz = xlwt.Alignment.HORZ_RIGHT
    table_right_alignment.vert = xlwt.Alignment.VERT_CENTER
    table_right_style.alignment = table_right_alignment

    worksheet.write_merge(0, 0, 0, 11, label='{0}年硕士生分专业招生人数汇总表'.format(year), style=header_style)

    # 参数对应第二行
    worksheet.write(1, 0, label='招生专业代码', style=header_style)
    worksheet.write(1, 1, label='招生专业名称', style=header_style)
    worksheet.write_merge(1, 2, 2, 2, '学院名称', style=header_style)
    worksheet.write(1, 3, label='学院总数', style=header_style)
    worksheet.write_merge(1, 2, 4, 4, '各专业招生数', style=header_style)
    worksheet.write(1, 5, label='全日制学术型', style=header_style)
    worksheet.write(1, 6, label='全日制专业学位', style=header_style)
    worksheet.write(1, 7, label='非全日制专业学位', style=header_style)
    worksheet.write(1, 8, label='录取一志愿', style=header_style)
    worksheet.write(1, 9, label='推免生', style=header_style)
    worksheet.write(1, 10, label='调剂人数', style=header_style)
    worksheet.write(1, 11, label='退役大学生', style=header_style)
    # 参数对应第三行
    worksheet.write(2, 0, label='')
    worksheet.write(2, 1, label='合计', style=header_style)
    worksheet.write(2, 3, label='')
    worksheet.write(2, 5, label='')
    worksheet.write(2, 6, label='')
    worksheet.write(2, 7, label='')
    worksheet.write(2, 8, label='')
    worksheet.write(2, 9, label='')
    worksheet.write(2, 10, label='')
    worksheet.write(2, 11, label='')
    # 列宽
    worksheet.col(0).width = 256 * 12
    worksheet.col(1).width = 256 * 30
    worksheet.col(2).width = 256 * 20
    worksheet.col(3).width = 256 * 15
    worksheet.col(4).width = 256 * 15
    worksheet.col(5).width = 256 * 15
    worksheet.col(6).width = 256 * 15
    worksheet.col(7).width = 256 * 15
    worksheet.col(8).width = 256 * 15
    # 行高
    tall_style = xlwt.easyxf('font:height 240;')
    first_row = worksheet.row(1)
    first_row.set_style(tall_style)
    # 获取所有的学院
    acas = Academy.objects.values("aca_cname", "uuid")
    i = 2
    for aca in acas:
        majors = Academy.objects.filter(uuid=aca['uuid']).values('majors__uuid', 'majors__maj_name', 'majors__maj_code')
        row_start = i + 1
        row_end = row_start + len(majors)
        worksheet.write_merge(row_start, row_end, 2, 2, aca['aca_cname'], style=table_center_style)
        if year:
            aca_student = Student.objects.filter(academy__uuid=aca["uuid"])\
                .filter(stu_entrance_time__year=year).all()
        else:
            aca_student = Student.objects.filter(academy__uuid=aca["uuid"]).all()

        worksheet.write_merge(row_start, row_end, 3, 3, aca_student.count(), style=table_center_style)
        for major in majors:
            maj_student = aca_student.filter(major_id=major["majors__uuid"])
            worksheet.write(row_start, 0, label=major['majors__maj_code'], style=table_center_style)
            worksheet.write(row_start, 1, label=major['majors__maj_name'])
            worksheet.write(row_start, 4, label=maj_student.count(), style=table_center_style)
            worksheet.write(row_start, 5, label=maj_student.filter(stu_learn_type='S1')
                            .filter(stu_cultivating_mode='C2').count(), style=table_center_style)
            worksheet.write(row_start, 6, label=maj_student.filter(stu_learn_type='S1')
                            .filter(stu_cultivating_mode='C1').count(), style=table_center_style)
            worksheet.write(row_start, 7, label=maj_student.filter(stu_learn_type='S2')
                            .filter(stu_cultivating_mode='C1').count(), style=table_center_style)
            worksheet.write(row_start, 8, label=maj_student.filter(stu_is_volunteer=True).count(), style=table_center_style)
            worksheet.write(row_start, 9, label=maj_student.filter(stu_is_exemption=True).count(), style=table_center_style)
            worksheet.write(row_start, 10, label=maj_student.filter(stu_is_adjust=True).count(), style=table_center_style)
            worksheet.write(row_start, 11, label=maj_student.filter(stu_special_program='S3').count(), style=table_center_style)
            row_start += 1
        # 学院汇总
        worksheet.write(row_start, 0, label='')
        worksheet.write(row_start, 1, label='学院汇总', style=table_right_style)
        worksheet.write(row_start, 4, label=aca_student.count(), style=table_center_style)
        worksheet.write(row_start, 5, label=aca_student.filter(stu_learn_type='S1')
                        .filter(stu_cultivating_mode='C2').count(), style=table_center_style)
        worksheet.write(row_start, 6, label=aca_student.filter(stu_learn_type='S1')
                        .filter(stu_cultivating_mode='C1').count(), style=table_center_style)
        worksheet.write(row_start, 7, label=aca_student.filter(stu_learn_type='S2')
                        .filter(stu_cultivating_mode='C1').count(), style=table_center_style)
        worksheet.write(row_start, 8, label=aca_student.filter(stu_is_volunteer=True).count(), style=table_center_style)
        worksheet.write(row_start, 9, label=aca_student.filter(stu_is_exemption=True).count(), style=table_center_style)
        worksheet.write(row_start, 10, label=aca_student.filter(stu_is_adjust=True).count(), style=table_center_style)
        worksheet.write(row_start, 11, label=aca_student.filter(stu_special_program='S3').count(), style=table_center_style)
        i = row_start

    # 总表统计
    all_student = Student.objects.all()
    i = i+1
    worksheet.write(i, 0, label='')
    worksheet.write(i, 1, label='')
    worksheet.write_merge(i, i, 2, 3, label='拟录取人数汇总', style=table_left_style)
    worksheet.write(i, 4, label=all_student.count(), style=table_center_style)
    worksheet.write(i, 5, label=all_student.filter(stu_learn_type='S1')
                    .filter(stu_cultivating_mode='C2').count(), style=table_center_style)
    worksheet.write(i, 6, label=all_student.filter(stu_learn_type='S1')
                    .filter(stu_cultivating_mode='C1').count(), style=table_center_style)
    worksheet.write(i, 7, label=all_student.filter(stu_learn_type='S2')
                    .filter(stu_cultivating_mode='C1').count(), style=table_center_style)
    worksheet.write(i, 8, label=all_student.filter(stu_is_volunteer=True).count(), style=table_center_style)
    worksheet.write(i, 9, label=all_student.filter(stu_is_exemption=True).count(), style=table_center_style)
    worksheet.write(i, 10, label=all_student.filter(stu_is_adjust=True).count(), style=table_center_style)
    worksheet.write(i, 11, label=all_student.filter(stu_special_program='S3').count(),
                    style=table_center_style)

    # 保存
    workbook.save('document.xls')
    if os.path.exists(os.path.join(settings.BASE_DIR, 'document.xls')):
        with open(os.path.join(settings.BASE_DIR, 'document.xls'), 'rb') as excel:
            response = HttpResponse(excel.read(), 'application/vnd.ms-excel')
            response['Content-Disposition'] = "attachment;filename={}".format('document.xls')
        return response
    else:
        raise FileNotFoundError
