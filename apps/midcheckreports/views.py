#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ==================================================
# @Time : 2019-05-06 15:30 
# @Author : libin
# @Site :  
# @File : views.py 
# @Desc : 
# ==================================================
import os
import xlwt

from django.conf import settings
from django.http import HttpResponse
from rest_framework import generics
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt

from core.decorators.excepts import excepts
from contrib.accounts.models import Student
from contrib.colleges.models import Academy
from apps.colleges.views import TableStyle


class MidCheckReportList(generics.GenericAPIView):

    @excepts
    @csrf_exempt
    def get(self, request, *args, **kwargs):
        year = request.query_params.get("year", 2019)
        academy = request.query_params.get("academy")
        mid_check_list = list()
        # 输出每个学院的统计数
        if academy:
            academies = Academy.objects.filter(aca_cname=academy).values('uuid', 'aca_cname')
        else:
            academies = Academy.objects.values('uuid', 'aca_cname')

        for academy in academies:
            aca_dict = dict()
            aca_dict["academy"] = academy["aca_cname"]
            academy_stu = Student.objects.filter(stu_entrance_time__year=year).filter(stu_academy_id=academy["uuid"])
            stu_count = academy_stu.count()
            delay_count = academy_stu.filter(stu_is_delay=False).count()
            track_count = academy_stu.filter(stu_mid_check='S2').count()
            fail_count = academy_stu.filter(stu_mid_check='S3').count()
            aca_dict["stu_count"] = stu_count
            aca_dict["schedule_count"] = academy_stu.filter(stu_is_delay=True).count()
            aca_dict["delay_count"] = delay_count
            aca_dict["delay_proportion"] = '{:.0%}'.format(delay_count / stu_count)
            aca_dict["track_count"] = track_count
            aca_dict["track_proportion"] = '{:.0%}'.format(track_count / stu_count)
            aca_dict["fail_count"] = fail_count
            aca_dict["fail_proportion"] = '{:.0%}'.format(fail_count / stu_count)
            mid_check_list.append(aca_dict)
        return Response(mid_check_list)


class MidCheckReportUpload(generics.GenericAPIView):

    @excepts
    @csrf_exempt
    def get(self, request, *args, **kwargs):
        year = request.query_params.get("year", 2019)
        academy = request.query_params.get("academy")
        workbook = xlwt.Workbook(encoding='utf-8')
        worksheet = workbook.add_sheet('worksheet')
        header_style, table_center_style = TableStyle.header_style, TableStyle.table_center_style
        mid_check_list = list()
        # 输出每个学院的统计数
        if academy:
            academies = Academy.objects.filter(aca_cname=academy).values('uuid', 'aca_cname')
        else:
            academies = Academy.objects.values('uuid', 'aca_cname')

        for academy in academies:
            aca_dict = dict()
            aca_dict["academy"] = academy["aca_cname"]
            academy_stu = Student.objects.filter(stu_entrance_time__year=year).filter(stu_academy_id=academy["uuid"])
            stu_count = academy_stu.count()
            delay_count = academy_stu.filter(stu_is_delay=False).count()
            track_count = academy_stu.filter(stu_mid_check='S2').count()
            fail_count = academy_stu.filter(stu_mid_check='S3').count()
            aca_dict["stu_count"] = stu_count
            aca_dict["schedule_count"] = academy_stu.filter(stu_is_delay=True).count()
            aca_dict["delay_count"] = delay_count
            aca_dict["delay_proportion"] = '{:.0%}'.format(delay_count / stu_count)
            aca_dict["track_count"] = track_count
            aca_dict["track_proportion"] = '{:.0%}'.format(track_count / stu_count)
            aca_dict["fail_count"] = fail_count
            aca_dict["fail_proportion"] = '{:.0%}'.format(fail_count / stu_count)
            mid_check_list.append(aca_dict)

        worksheet.write_merge(0, 0, 0, 9, label='{0}届研究生中期考核情况统计'.format(year), style=header_style)
        # 表头
        for index, value in enumerate(['序号', '学院', '学生数', '按期考核人数', '延期考核人数', '延期考核比例', '被跟踪人数',
                                       '被跟踪比例', '不合格人数', '不合格比例']):
            worksheet.write(1, index, label=value, style=header_style)

        # 行高
        tall_style = xlwt.easyxf('font:height 240;')
        first_row = worksheet.row(1)
        first_row.set_style(tall_style)

        data_len = len(mid_check_list)
        for line, data in enumerate(mid_check_list):
            for index, value in enumerate(["", "academy", "stu_count", "schedule_count", "delay_count",
                                           "delay_proportion", "track_count", "track_proportion", "fail_count",
                                           "fail_proportion"]):
                if index == 0:
                    worksheet.write(line + 2, 0, label=line + 1, style=table_center_style)
                else:
                    worksheet.write(line + 2, index, label=data[value], style=table_center_style)
        # 合计汇总行
        all_academy_stu = Student.objects.filter(stu_entrance_time__year=year)
        stu_all_count = all_academy_stu.count()
        all_delay_count = all_academy_stu.filter(stu_is_delay=False).count()
        all_track_count = all_academy_stu.filter(stu_mid_check='S2').count()
        all_fail_count = all_academy_stu.filter(stu_mid_check='S3').count()
        for i, value in enumerate([data_len + 1, '合计',
                                   xlwt.Formula('SUM(C3:C{0})'.format(data_len + 2)),
                                   xlwt.Formula('SUM(D3:D{0})'.format(data_len + 2)),
                                   xlwt.Formula('SUM(E3:E{0})'.format(data_len + 2)),
                                   '{:.0%}'.format(all_delay_count / stu_all_count),
                                   xlwt.Formula('SUM(G3:G{0})'.format(data_len + 2)),
                                   '{:.0%}'.format(all_track_count / stu_all_count),
                                   xlwt.Formula('SUM(I3:I{0})'.format(data_len + 2)),
                                   '{:.0%}'.format(all_fail_count / stu_all_count)]):
            worksheet.write(data_len + 2, i, label=value, style=table_center_style)

        # 保存
        workbook.save(os.path.join(settings.BASE_DIR, 'midterm_exams.xls'))
        if os.path.exists(os.path.join(settings.BASE_DIR, 'midterm_exams.xls')):
            with open(os.path.join(settings.BASE_DIR, 'midterm_exams.xls'), 'rb') as excel:
                response = HttpResponse(excel.read(), 'application/vnd.ms-excel')
                response['Content-Disposition'] = "attachment;filename={}".format('midterm_exams.xls')
            return response
        else:
            raise FileNotFoundError
