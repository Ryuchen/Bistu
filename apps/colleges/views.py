#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ==================================================
# @Time : 2019-04-02 20:11 
# @Author : ryuchen
# @Site :  
# @File : views.py
# @Desc : 
# ==================================================
import os
import xlrd
import xlwt
from django.conf import settings
from django.http import HttpResponse
from rest_framework import generics, status
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from core.decorators.excepts import excepts
from django.contrib.auth.models import User
from contrib.academy.models import Academy, Major, Research
from contrib.academy.models import OpeningReport, ReformResults, MidtermExams, PaperQuality
from .serializers import MajorSerializers, AcademySerializers, ResearchSerializers
from .serializers import OpeningReportSerializers, ReformResultsSerializers, MidtermExamsSerializers, PaperQualitySerializers


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


class TableStyle:
    alignment = xlwt.Alignment()
    alignment.horz = xlwt.Alignment.HORZ_CENTER
    alignment.vert = xlwt.Alignment.VERT_CENTER
    
    # 写入excel
    header_style = xlwt.XFStyle()
    header_font = xlwt.Font()
    header_font.bold = True
    header_style.font = header_font
    header_style.alignment = alignment
    # 表格数据居中
    table_center_style = xlwt.XFStyle()
    table_center_style.alignment = alignment


# 研究生开题情况统计
class OpeningReportList(generics.GenericAPIView):
    model = OpeningReport
    queryset = OpeningReport.objects.all()
    serializer_class = OpeningReportSerializers
    pagination_class = None
    
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

    # Excel上传
    @excepts
    @csrf_exempt
    def post(self, request, *args, **kwargs):
        file = request.data['file']
        data = xlrd.open_workbook(filename=None, file_contents=file.read())
        table = data.sheets()[0]
        nrows = table.nrows
        file_list = list()
        for i in range(1, nrows):
            rowx = table.row_values(i)
            file_dict = dict()
            file_dict["academy"] = rowx[1]
            file_dict["stu_count"] = rowx[2]
            file_dict["schedule_count"] = rowx[3]
            file_dict["delay_count"] = rowx[4]
            file_dict["fail_count"] = rowx[5]
            file_dict["time"] = "2019"
            file_list.append(file_dict)
        serializer = self.get_serializer(data=file_list, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    @excepts
    @csrf_exempt
    def patch(self, request, *args, **kwargs):
        year = request.data.get("year", "")
        workbook = xlwt.Workbook(encoding='utf-8')
        worksheet = workbook.add_sheet('worksheet')
        header_style, table_center_style = TableStyle.header_style, TableStyle.table_center_style
        
        worksheet.write_merge(0, 0, 0, 5, label='{0}届研究生开题情况统计-按学院'.format(year), style=header_style)
        
        # 表头
        for index, value in enumerate(['序号', '学院', '学生数', '按期开题人数', '延期开题人数', '开题不通过人数']):
            worksheet.write(1, index, label=value, style=header_style)
        # 行高
        tall_style = xlwt.easyxf('font:height 240;')
        first_row = worksheet.row(1)
        first_row.set_style(tall_style)
        
        datas = OpeningReport.objects.filter(time__year=year).all()
        i = 2
        for data in datas:
            row_start = i
            worksheet.write(row_start, 0, label=(i-1), style=table_center_style)
            worksheet.write(row_start, 1, label=data["academy"], style=table_center_style)
            worksheet.write(row_start, 2, label=data["stu_count"], style=table_center_style)
            worksheet.write(row_start, 3, label=data["schedule_count"], style=table_center_style)
            worksheet.write(row_start, 4, label=data["delay_count"], style=table_center_style)
            worksheet.write(row_start, 5, label=data["fail_count"], style=table_center_style)
            row_start += 1
            i += 1
        worksheet.write(i, 0, label=(i - 1), style=table_center_style)
        worksheet.write(i, 1, label='合计', style=table_center_style)
        worksheet.write(i, 2, label=1, style=table_center_style)
        worksheet.write(i, 3, label=1, style=table_center_style)
        worksheet.write(i, 4, label=1, style=table_center_style)
        worksheet.write(i, 5, label=1, style=table_center_style)
        # 保存
        workbook.save('opening_report.xls')
        if os.path.exists(os.path.join(settings.BASE_DIR, 'opening_report.xls')):
            with open(os.path.join(settings.BASE_DIR, 'opening_report.xls'), 'rb') as excel:
                response = HttpResponse(excel.read(), 'application/vnd.ms-excel')
                response['Content-Disposition'] = "attachment;filename={}".format('opening_report.xls')
            return response
        else:
            raise FileNotFoundError


# 研究生教育改革成果统计
class ReformResultsList(generics.GenericAPIView):
    model = ReformResults
    queryset = ReformResults.objects.all()
    serializer_class = ReformResultsSerializers
    pagination_class = None
    
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
    
    # Excel上传
    @excepts
    @csrf_exempt
    def post(self, request, *args, **kwargs):
        file = request.data['file']
        data = xlrd.open_workbook(filename=None, file_contents=file.read())
        table = data.sheets()[0]
        nrows = table.nrows
        file_list = list()
        for i in range(1, nrows):
            rowx = table.row_values(i)
            file_dict = dict()
            file_dict["academy"] = rowx[0]
            file_dict["project_count"] = rowx[1]
            file_dict["paper_count"] = rowx[2]
            file_dict["textbook_count"] = rowx[3]
            file_dict["award_count"] = rowx[4]
            file_dict["course_count"] = rowx[5]
            file_dict["base_count"] = rowx[6]
            file_dict["exchange_project_count"] = rowx[7]
            file_dict["time"] = "2019"
            file_list.append(file_dict)
        serializer = self.get_serializer(data=file_list, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    @excepts
    @csrf_exempt
    def patch(self, request, *args, **kwargs):
        year = request.data.get("year", "")
        workbook = xlwt.Workbook(encoding='utf-8')
        worksheet = workbook.add_sheet('worksheet')
        header_style, table_center_style = TableStyle.header_style, TableStyle.table_center_style
        
        worksheet.write_merge(0, 0, 0, 7, label='{0}年各学院研究生教育改革成果统计'.format(year), style=header_style)
        # 表头
        worksheet.write(1, 0, label='学院名称 ', style=header_style)
        worksheet.write(1, 1, label='研究生教育相关教改项目立项', style=header_style)
        worksheet.write(1, 2, label='发表研究生教育相关教改论文', style=header_style)
        worksheet.write(1, 3, label='出版研究生教材', style=header_style)
        worksheet.write(1, 4, label='研究生教育相关获奖', style=header_style)
        worksheet.write(1, 5, label='精品/在线课程建设', style=header_style)
        worksheet.write(1, 6, label='实践基地建设', style=header_style)
        worksheet.write(1, 7, label='研究生国际交流', style=header_style)
        # 行高
        tall_style = xlwt.easyxf('font:height 240;')
        first_row = worksheet.row(1)
        first_row.set_style(tall_style)
        
        datas = ReformResults.objects.filter(time__year=year).all()
        i = 2
        for data in datas:
            row_start = i
            worksheet.write(row_start, 0, label=data["academy"], style=table_center_style)
            worksheet.write(row_start, 1, label=data["project_count"], style=table_center_style)
            worksheet.write(row_start, 2, label=data["paper_count"], style=table_center_style)
            worksheet.write(row_start, 3, label=data["textbook_count"], style=table_center_style)
            worksheet.write(row_start, 4, label=data["award_count"], style=table_center_style)
            worksheet.write(row_start, 5, label=data["course_count"], style=table_center_style)
            worksheet.write(row_start, 6, label=data["base_count"], style=table_center_style)
            worksheet.write(row_start, 7, label=data["exchange_project_count"], style=table_center_style)
            row_start += 1
            i += 1
        worksheet.write(i, 0, label='合计', style=table_center_style)
        worksheet.write(i, 1, label=1, style=table_center_style)
        worksheet.write(i, 2, label=1, style=table_center_style)
        worksheet.write(i, 3, label=1, style=table_center_style)
        worksheet.write(i, 4, label=1, style=table_center_style)
        worksheet.write(i, 5, label=1, style=table_center_style)
        worksheet.write(i, 6, label=1, style=table_center_style)
        worksheet.write(i, 7, label=1, style=table_center_style)
        # 保存
        workbook.save('reform_results.xls')
        if os.path.exists(os.path.join(settings.BASE_DIR, 'reform_results.xls')):
            with open(os.path.join(settings.BASE_DIR, 'reform_results.xls'), 'rb') as excel:
                response = HttpResponse(excel.read(), 'application/vnd.ms-excel')
                response['Content-Disposition'] = "attachment;filename={}".format('reform_results.xls')
            return response
        else:
            raise FileNotFoundError


# 研究生中期考核情况统计
class MidtermExamsList(generics.GenericAPIView):
    model = MidtermExams
    queryset = MidtermExams.objects.all()
    serializer_class = MidtermExamsSerializers
    pagination_class = None
    
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
    
    # Excel上传
    @excepts
    @csrf_exempt
    def post(self, request, *args, **kwargs):
        file = request.data['file']
        data = xlrd.open_workbook(filename=None, file_contents=file.read())
        table = data.sheets()[0]
        nrows = table.nrows
        file_list = list()
        for i in range(1, nrows):
            rowx = table.row_values(i)
            file_dict = dict()
            file_dict["academy"] = rowx[1]
            file_dict["stu_count"] = rowx[2]
            file_dict["schedule_count"] = rowx[3]
            file_dict["delay_count"] = rowx[4]
            file_dict["delay_reason"] = rowx[5]
            file_dict["delay_proportion"] = rowx[6]
            file_dict["track_count"] = rowx[7]
            file_dict["track_proportion"] = rowx[8]
            file_dict["fail_count"] = rowx[9]
            file_dict["fail_proportion"] = rowx[10]
            file_dict["time"] = "2019"
            file_list.append(file_dict)
        serializer = self.get_serializer(data=file_list, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    @excepts
    @csrf_exempt
    def patch(self, request, *args, **kwargs):
        year = request.data.get("year", "")
        workbook = xlwt.Workbook(encoding='utf-8')
        worksheet = workbook.add_sheet('worksheet')
        header_style, table_center_style = TableStyle.header_style, TableStyle.table_center_style
        
        worksheet.write_merge(0, 0, 0, 10, label='{0}届研究生中期考核情况统计'.format(year), style=header_style)
        # 表头
        for index, value in enumerate(['序号', '学院', '学生数', '按期考核人数', '延期考核人数', '延期考核原因',
                                       '延期考核比例', '被跟踪人数', '被跟踪比例', '不合格人数', '不合格比例']):
            worksheet.write(1, index, label=value, style=header_style)
            
        # 行高
        tall_style = xlwt.easyxf('font:height 240;')
        first_row = worksheet.row(1)
        first_row.set_style(tall_style)
        
        datas = MidtermExams.objects.filter(time__year=year).all()
        i = 2
        for data in datas:
            row_start = i
            for index, value in enumerate(["academy", "project_count", "paper_count", "textbook_count", "award_count",
                                           "course_count", "base_count", "exchange_project_count"]):
                worksheet.write(row_start, index, label=data[value], style=table_center_style)
            row_start += 1
        # 保存
        workbook.save('midterm_exams.xls')
        if os.path.exists(os.path.join(settings.BASE_DIR, 'midterm_exams.xls')):
            with open(os.path.join(settings.BASE_DIR, 'midterm_exams.xls'), 'rb') as excel:
                response = HttpResponse(excel.read(), 'application/vnd.ms-excel')
                response['Content-Disposition'] = "attachment;filename={}".format('midterm_exams.xls')
            return response
        else:
            raise FileNotFoundError


# 学位论文质量统计
class PaperQualityList(generics.GenericAPIView):
    model = PaperQuality
    queryset = PaperQuality.objects.all()
    serializer_class = PaperQualitySerializers
    pagination_class = None
    
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
    
    # Excel上传
    @excepts
    @csrf_exempt
    def post(self, request, *args, **kwargs):
        file = request.data['file']
        data = xlrd.open_workbook(filename=None, file_contents=file.read())
        table = data.sheets()[0]
        nrows = table.nrows
        file_list = list()
        for i in range(1, nrows):
            rowx = table.row_values(i)
            file_dict = dict()
            file_dict["academy"] = rowx[1]
            file_dict["major"] = rowx[2]
            file_dict["full_time_count"] = rowx[3]
            file_dict["delay_count"] = rowx[4]
            file_dict["delay_reason"] = rowx[5]
            file_dict["paper_stu_count"] = rowx[6]
            file_dict["paper_pass_count"] = rowx[7]
            file_dict["paper_pass_proportion"] = rowx[8]
            file_dict["paper_fail_count"] = rowx[9]
            file_dict["paper_fail_proportion"] = rowx[10]
            file_dict["paper_fifteen_count"] = rowx[11]
            file_dict["paper_fifteen_proportion"] = rowx[12]
            file_dict["paper_ten_count"] = rowx[13]
            file_dict["paper_ten_proportion"] = rowx[14]
            file_dict["blind_trial_proportion"] = rowx[15]
            file_dict["blind_trial_count"] = rowx[16]
            file_dict["reply_count"] = rowx[17]
            file_dict["evaluation_count"] = rowx[18]
            file_dict["evaluation_result"] = rowx[19]
            file_dict["graduate_count"] = rowx[20]
            file_dict["graduate_proportion"] = rowx[21]
            file_dict["degree_count"] = rowx[22]
            file_dict["degree_proportion"] = rowx[23]
            file_dict["time"] = "2019"
            file_list.append(file_dict)
        serializer = self.get_serializer(data=file_list, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    @excepts
    @csrf_exempt
    def patch(self, request, *args, **kwargs):
        year = request.data.get("year", "")
        workbook = xlwt.Workbook(encoding='utf-8')
        worksheet = workbook.add_sheet('worksheet')
        header_style, table_center_style = TableStyle.header_style, TableStyle.table_center_style
        
        worksheet.write_merge(0, 0, 0, 10, label='{0}年研究生学位论文质量统计'.format(year), style=header_style)
        # 表头
        worksheet.write(1, 0, label='序号', style=header_style)
        worksheet.write(1, 1, label='学院', style=header_style)
        worksheet.write(1, 2, label='专业', style=header_style)
        worksheet.write(1, 3, label='全日制学生数', style=header_style)
        worksheet.write_merge(1, 1, 4, 5, label='延期', style=header_style)
        worksheet.write_merge(1, 1, 6, 14, label='论文检测', style=header_style)
        worksheet.write_merge(1, 1, 15, 16, label='盲审', style=header_style)
        worksheet.write(1, 17, label='答辩', style=header_style)
        worksheet.write_merge(1, 1, 18, 19, label='评优', style=header_style)
        worksheet.write_merge(1, 1, 20, 21, label='毕业情况', style=header_style)
        worksheet.write_merge(1, 1, 22, 23, label='获学位情况', style=header_style)
        
        for index, value in enumerate(['', '', '', '', '人数', '原因', '人数', '一次通过人数', '一次通过率', '不合格人数',
                                       '不合格占比', '15%以下人数', '15%以下占比', '10%以下人数', '10%以下占比', '比例',
                                       '未通过人数', '未通过人数', '名额', '评选结果', '毕业人数', '毕业率', '获学位人数',
                                       '获学位率']):
            worksheet.write(2, index, label=value, style=header_style)
        
        # 行高
        tall_style = xlwt.easyxf('font:height 240;')
        first_row = worksheet.row(1)
        first_row.set_style(tall_style)

        datas = PaperQuality.objects.filter(time__year=year).all()
        i = 3
        for data in datas:
            row_start = i
            for index, value in enumerate(["academy", "major", "full_time_count", "delay_count", "delay_reason",
                                           "paper_stu_count", "paper_pass_count", "paper_pass_proportion",
                                           "paper_fail_count", "paper_fail_proportion", "paper_fifteen_count",
                                           "paper_fifteen_proportion", "paper_ten_count", "paper_ten_proportion",
                                           "blind_trial_proportion", "blind_trial_count", "reply_count",
                                           "evaluation_count", "evaluation_result", "graduate_count",
                                           "graduate_proportion", "degree_count", "degree_proportion"]):
                if index == 0:
                    worksheet.write(row_start, 0, label=i-2, style=table_center_style)
                else:
                    worksheet.write(row_start, index, label=data[value], style=table_center_style)
            row_start += 1
        # 保存
        workbook.save('paper_quality.xls')
        if os.path.exists(os.path.join(settings.BASE_DIR, 'paper_quality.xls')):
            with open(os.path.join(settings.BASE_DIR, 'paper_quality.xls'), 'rb') as excel:
                response = HttpResponse(excel.read(), 'application/vnd.ms-excel')
                response['Content-Disposition'] = "attachment;filename={}".format('paper_quality.xls')
            return response
        else:
            raise FileNotFoundError
