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
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt

from rest_framework import generics, status
from rest_framework.response import Response
from core.decorators.excepts import excepts
from contrib.accounts.models import Student
from contrib.colleges.models import Reform
from contrib.colleges.models import Academy, Major, Research
from .serializers import MajorSerializers, AcademySerializers, ResearchSerializers
from .serializers import ReformSerializers


# 科研方向
class SimpleResearch(object):
    model = Research
    queryset = Research.objects.all()
    serializer_class = ResearchSerializers
    pagination_class = None


class ResearchDetail(SimpleResearch, generics.RetrieveUpdateDestroyAPIView):
    @excepts
    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    @excepts
    def put(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    @excepts
    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_200_OK)


class ResearchList(SimpleResearch, generics.GenericAPIView):
    @excepts
    def get(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
        else:
            serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @excepts
    def put(self, request, *args, **kwargs):
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
    def post(self, request, *args, **kwargs):
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
    @excepts
    @csrf_exempt
    def get(self, request, *args, **kwargs):
        year = request.query_params.get("year", 2019)
        academy = request.query_params.get("academy")
        opening_list = list()
        # 输出每个学院的统计数
        if academy:
            academies = Academy.objects.filter(aca_cname=academy).values('uuid', 'aca_cname')
        else:
            academies = Academy.objects.values('uuid', 'aca_cname')

        for academy in academies:
            opening_dict = dict()
            opening_dict["academy"] = academy["aca_cname"]
            academy_stu = Student.objects.filter(stu_entrance_time__year=year).filter(stu_academy_id=academy["uuid"])
            opening_dict["stu_count"] = academy_stu.count()
            opening_dict["schedule_count"] = academy_stu.filter(stu_thesis__the_is_delay=False).count()
            opening_dict["delay_count"] = academy_stu.filter(stu_thesis__the_is_delay=True).count()
            opening_dict["fail_count"] = academy_stu.filter(stu_thesis__the_final_score=False).count()
            opening_list.append(opening_dict)
        return Response(opening_list)


class OpeningReportUpload(generics.GenericAPIView):
    
    @excepts
    @csrf_exempt
    def get(self, request, *args, **kwargs):
        year = request.query_params.get("year", 2019)
        academy = request.query_params.get("academy")
        workbook = xlwt.Workbook(encoding='utf-8')
        worksheet = workbook.add_sheet('worksheet')
        header_style, table_center_style = TableStyle.header_style, TableStyle.table_center_style
        opening_list = list()
        # 输出每个学院的统计数
        if academy:
            academies = Academy.objects.filter(aca_cname=academy).values('uuid', 'aca_cname')
        else:
            academies = Academy.objects.values('uuid', 'aca_cname')

        for academy in academies:
            opening_dict = dict()
            opening_dict["academy"] = academy["aca_cname"]
            academy_stu = Student.objects.filter(stu_entrance_time__year=year).filter(stu_academy_id=academy["uuid"])
            opening_dict["stu_count"] = academy_stu.count()
            opening_dict["schedule_count"] = academy_stu.filter(stu_thesis__the_is_delay=False).count()
            opening_dict["delay_count"] = academy_stu.filter(stu_thesis__the_is_delay=True).count()
            opening_dict["fail_count"] = academy_stu.filter(stu_thesis__the_final_score=False).count()
            opening_list.append(opening_dict)
    
        # 标题
        worksheet.write_merge(0, 0, 0, 5, label='{0}届研究生开题情况统计-按学院'.format(year), style=header_style)
    
        # 表头
        for index, value in enumerate(['序号', '学院', '学生数', '按期开题人数', '延期开题人数', '开题不通过人数']):
            worksheet.write(1, index, label=value, style=header_style)
    
        # 行高
        tall_style = xlwt.easyxf('font:height 240;')
        first_row = worksheet.row(1)
        first_row.set_style(tall_style)
    
        data_len = len(opening_list)
        for line, data in enumerate(opening_list):
            for index, value in enumerate(["", "academy", "stu_count", "schedule_count", "delay_count", "fail_count"]):
                if index == 0:
                    worksheet.write(line + 2, 0, label=line + 1, style=table_center_style)
                else:
                    worksheet.write(line + 2, index, label=data[value], style=table_center_style)
        # 合计汇总行
        for i, value in enumerate([data_len + 1, '合计',
                                   xlwt.Formula('SUM(C3:C{0})'.format(data_len + 2)),
                                   xlwt.Formula('SUM(D3:D{0})'.format(data_len + 2)),
                                   xlwt.Formula('SUM(E3:E{0})'.format(data_len + 2)),
                                   xlwt.Formula('SUM(F3:F{0})'.format(data_len + 2))]):
            worksheet.write(data_len + 2, i, label=value, style=table_center_style)
    
        # 保存
        workbook.save(os.path.join(settings.BASE_DIR, 'opening_report.xls'))
        if os.path.exists(os.path.join(settings.BASE_DIR, 'opening_report.xls')):
            with open(os.path.join(settings.BASE_DIR, 'opening_report.xls'), 'rb') as excel:
                response = HttpResponse(excel.read(), 'application/vnd.ms-excel')
                response['Content-Disposition'] = "attachment;filename={}".format('opening_report.xls')
            return response
        else:
            raise FileNotFoundError


# 研究生教育改革成果统计
class ReformList(generics.GenericAPIView):
    model = Reform
    queryset = Reform.objects.all()
    serializer_class = ReformSerializers

    @excepts
    @csrf_exempt
    def get(self, request, *args, **kwargs):
        year = request.query_params.get("year", 2019)
        academy = request.query_params.get("academy")
        reform_list = list()
        # 输出每个学院的统计数
        if academy:
            academies = Academy.objects.filter(aca_cname=academy).values('uuid', 'aca_cname')
        else:
            academies = Academy.objects.values('uuid', 'aca_cname')

        for academy in academies:
            reform_dict = dict()
            reform_dict["academy"] = academy["aca_cname"]
            reform = Reform.objects.filter(reform__uuid=academy["uuid"])
            reform_dict["project"] = ",".join(
                [ref['ref_name'] for ref in reform.filter(time=year).filter(ref_type="RT1").values("ref_name")])
            reform_dict["paper"] = ",".join(
                [ref['ref_name'] for ref in reform.filter(time=year).filter(ref_type="RT2").values("ref_name")])
            reform_dict["textbook"] = ",".join(
                [ref['ref_name'] for ref in reform.filter(time=year).filter(ref_type="RT3").values("ref_name")])
            reform_dict["award"] = ",".join(
                [ref['ref_name'] for ref in reform.filter(time=year).filter(ref_type="RT4").values("ref_name")])
            reform_dict["course"] = ",".join(
                [ref['ref_name'] for ref in reform.filter(time=year).filter(ref_type="RT5").values("ref_name")])
            reform_dict["base"] = ",".join(
                [ref['ref_name'] for ref in reform.filter(time=year).filter(ref_type="RT6").values("ref_name")])
            reform_dict["exchange_project"] = ",".join(
                [ref['ref_name'] for ref in reform.filter(time=year).filter(ref_type="RT7").values("ref_name")])
            reform_list.append(reform_dict)
        return Response(reform_list)
    
    # Excel上传
    @excepts
    @csrf_exempt
    def post(self, request, *args, **kwargs):
        res = {}
        file = request.data['file']
        data = xlrd.open_workbook(filename=None, file_contents=file.read())
        table = data.sheets()[0]
        nrows = table.nrows
        time = "2019"
        for i in range(2, nrows-1):
            rowx = table.row_values(i)
            academy = Academy.objects.get(aca_cname=rowx[0])
            reform_list = list()
            for name in rowx[1].splitlines():
                reform = Reform.objects.create(ref_type="RT1", ref_name=name, time=time)
                reform_list.append(reform)

            for name in rowx[2].splitlines():
                reform = Reform.objects.create(ref_type="RT2", ref_name=name, time=time)
                reform_list.append(reform)

            for name in rowx[3].splitlines():
                reform = Reform.objects.create(ref_type="RT3", ref_name=name, time=time)
                reform_list.append(reform)

            for name in rowx[4].splitlines():
                reform = Reform.objects.create(ref_type="RT4", ref_name=name, time=time)
                reform_list.append(reform)

            for name in rowx[5].splitlines():
                reform = Reform.objects.create(ref_type="RT5", ref_name=name, time=time)
                reform_list.append(reform)

            for name in rowx[6].splitlines():
                reform = Reform.objects.create(ref_type="RT6", ref_name=name, time=time)
                reform_list.append(reform)

            for name in rowx[7].splitlines():
                reform = Reform.objects.create(ref_type="RT7", ref_name=name, time=time)
                reform_list.append(reform)

            for x in reform_list:
                academy.reforms.add(x)

        return Response(res, status=status.HTTP_200_OK)


class ReformUpload(generics.GenericAPIView):
    
    @excepts
    @csrf_exempt
    def get(self, request, *args, **kwargs):
        year = request.query_params.get("year", 2019)
        academy = request.query_params.get("academy")
        workbook = xlwt.Workbook(encoding='utf-8')
        worksheet = workbook.add_sheet('worksheet')
        header_style, table_center_style = TableStyle.header_style, TableStyle.table_center_style
        reform_list = list()
        # 输出每个学院的统计数
        if academy:
            academies = Academy.objects.filter(aca_cname=academy).values('uuid', 'aca_cname')
        else:
            academies = Academy.objects.values('uuid', 'aca_cname')

        for academy in academies:
            reform_dict = dict()
            reform_dict["academy"] = academy["aca_cname"]
            reform = Reform.objects.filter(reform__uuid=academy["uuid"])
            reform_dict["project"] = "\n".join(
                [ref['ref_name'] for ref in reform.filter(time=year).filter(ref_type="RT1").values("ref_name")])
            reform_dict["paper"] = "\n".join(
                [ref['ref_name'] for ref in reform.filter(time=year).filter(ref_type="RT2").values("ref_name")])
            reform_dict["textbook"] = "\n".join(
                [ref['ref_name'] for ref in reform.filter(time=year).filter(ref_type="RT3").values("ref_name")])
            reform_dict["award"] = "\n".join(
                [ref['ref_name'] for ref in reform.filter(time=year).filter(ref_type="RT4").values("ref_name")])
            reform_dict["course"] = "\n".join(
                [ref['ref_name'] for ref in reform.filter(time=year).filter(ref_type="RT5").values("ref_name")])
            reform_dict["base"] = "\n".join(
                [ref['ref_name'] for ref in reform.filter(time=year).filter(ref_type="RT6").values("ref_name")])
            reform_dict["exchange_project"] = "\n".join(
                [ref['ref_name'] for ref in reform.filter(time=year).filter(ref_type="RT7").values("ref_name")])
            reform_list.append(reform_dict)
        
        # 标题
        worksheet.write_merge(0, 0, 0, 7, label='{0}年各学院研究生教育改革成果统计'.format(year), style=header_style)
        
        # 表头
        for index, value in enumerate(['学院名称', '研究生教育相关教改项目立项', '发表研究生教育相关教改论文', '出版研究生教材',
                                       '研究生教育相关获奖', '精品/在线课程建设', '实践基地建设', '研究生国际交流']):
            worksheet.write(1, index, label=value, style=header_style)
        
        # 行高
        tall_style = xlwt.easyxf('font:height 240;')
        first_row = worksheet.row(1)
        first_row.set_style(tall_style)

        data_len = len(reform_list)
        for line, data in enumerate(reform_list):
            for index, value in enumerate(["academy", "project", "paper", "textbook", "award", "course", "base",
                                           "exchange_project"]):
                worksheet.write(line + 2, index, label=data[value], style=table_center_style)

        # 合计汇总行
        for i, value in enumerate(['合计',
                                   Reform.objects.filter(time=year).filter(ref_type="RT1").count(),
                                   Reform.objects.filter(time=year).filter(ref_type="RT2").count(),
                                   Reform.objects.filter(time=year).filter(ref_type="RT3").count(),
                                   Reform.objects.filter(time=year).filter(ref_type="RT4").count(),
                                   Reform.objects.filter(time=year).filter(ref_type="RT5").count(),
                                   Reform.objects.filter(time=year).filter(ref_type="RT6").count(),
                                   Reform.objects.filter(time=year).filter(ref_type="RT7").count()]):
            worksheet.write(data_len + 2, i, label=value, style=table_center_style)

        # 保存
        workbook.save(os.path.join(settings.BASE_DIR, 'reform_results.xls'))
        if os.path.exists(os.path.join(settings.BASE_DIR, 'reform_results.xls')):
            with open(os.path.join(settings.BASE_DIR, 'reform_results.xls'), 'rb') as excel:
                response = HttpResponse(excel.read(), 'application/vnd.ms-excel')
                response['Content-Disposition'] = "attachment;filename={}".format('reform_results.xls')
            return response
        else:
            raise FileNotFoundError


def get_paper(year=None, academy=None):
    paper_list = list()
    # 输出每个学院的统计数
    if academy:
        academies = Academy.objects.filter(aca_cname=academy).values('uuid', 'aca_cname')
    else:
        academies = Academy.objects.values('uuid', 'aca_cname')

    for academy in academies:
        paper_dict = dict()
        paper_dict["academy"] = academy["aca_cname"]
        if year:
            student_data = Student.objects.filter(stu_entrance_time__year=year).all()
        else:
            student_data = Student.objects.all()
        academy_stu = student_data.filter(stu_academy_id=academy["uuid"])

        # 每届各个学院的人数
        graduate_stu_count = academy_stu.count()
        paper_dict["full_time_count"] = academy_stu.filter(stu_learn_type="S1").count()

        # 延期
        paper_dict["delay_count"] = academy_stu.filter(stu_thesis__the_is_delay=True).count()
        paper_dict["delay_reason"] = ""

        # 论文查重结果
        paper_deteck_count = academy_stu.filter(stu_thesis__pla_thesis__pla_result__isnull=False).count()
        paper_dict["paper_stu_count"] = paper_deteck_count  # 获取论文检测总数

        # 论文检测一次性通过人数
        paper_one_pass = academy_stu.filter(stu_thesis__the_exam_count=1).count()
        paper_dict["paper_pass_count"] = paper_one_pass
        paper_dict["paper_pass_proportion"] = '{:.0%}'.format(paper_one_pass / paper_deteck_count)

        # 论文检测不合格人数
        paper_fail_count = academy_stu.filter(stu_thesis__pla_thesis__pla_result=False).count()
        paper_dict["paper_fail_count"] = paper_fail_count
        paper_dict["paper_fail_proportion"] = '{:.0%}'.format(paper_fail_count / paper_deteck_count)

        # 论文查重15%以下的人数
        paper_fifteen_count = academy_stu.filter(stu_thesis__pla_thesis__pla_rate__lt=15).count()
        paper_dict["paper_fifteen_count"] = paper_fifteen_count
        paper_dict["paper_fifteen_proportion"] = '{:.0%}'.format(paper_fifteen_count / paper_deteck_count)

        # 论文查重10%以下的人数
        paper_ten_count = academy_stu.filter(stu_thesis__pla_thesis__pla_rate__lt=10).count()
        paper_dict["paper_ten_count"] = paper_ten_count
        paper_dict["paper_ten_proportion"] = '{:.0%}'.format(paper_ten_count / paper_deteck_count)

        # 盲审
        blind_trial_count = academy_stu.filter(stu_thesis__bli_thesis__bli_date__year=year).count()  # TODO 查看盲审的比例
        blind_trial_fail_count = academy_stu.filter(stu_thesis__bli_thesis__bli_score="不合格").count()
        paper_dict["blind_trial_proportion"] = '{:.0%}'.format(blind_trial_count / graduate_stu_count)
        paper_dict["blind_trial_count"] = blind_trial_fail_count

        # 答辩
        paper_dict["reply_count"] = academy_stu.filter(stu_thesis__the_final_score=False).count()

        # 论文评优
        paper_dict["evaluation_count"] = 12  # TODO 论文评优的名额总数
        paper_dict["evaluation_result"] = academy_stu.filter(stu_thesis__the_is_superb=True).count()

        # 毕业情况
        graduate_pass_count = academy_stu.filter(stu_gain_cert=True).count()
        paper_dict["graduate_count"] = graduate_stu_count
        paper_dict["graduate_proportion"] = '{:.0%}'.format(graduate_pass_count / graduate_stu_count)

        # 获学位情况
        degree_count = academy_stu.filter(stu_gain_diploma=True).count()
        paper_dict["degree_count"] = degree_count
        paper_dict["degree_proportion"] = '{:.0%}'.format(degree_count / graduate_stu_count)

        paper_list.append(paper_dict)
    return paper_list


# 学位论文质量统计
class PaperList(generics.GenericAPIView):

    @excepts
    @csrf_exempt
    def get(self, request, *args, **kwargs):
        year = request.query_params.get("year", 2019)
        academy = request.query_params.get("academy")
        paper_list = get_paper(year=year, academy=academy)
        return Response(paper_list)


class PaperUpload(generics.GenericAPIView):
    
    @excepts
    @csrf_exempt
    def get(self, request, *args, **kwargs):
        year = request.query_params.get("year", 2019)
        academy = request.query_params.get("academy")
        workbook = xlwt.Workbook(encoding='utf-8')
        worksheet = workbook.add_sheet('worksheet')
        header_style, table_center_style = TableStyle.header_style, TableStyle.table_center_style

        # get paper data
        paper_list = get_paper(year=year, academy=academy)
        if year:
            student_data = Student.objects.filter(stu_entrance_time__year=year)
        else:
            student_data = Student.objects.all()
        # 表名
        worksheet.write_merge(0, 0, 0, 21, label='{0}年研究生学位论文质量统计'.format(year), style=header_style)
        
        # 表头
        worksheet.write(1, 0, label='序号', style=header_style)
        worksheet.write(1, 1, label='学院', style=header_style)
        worksheet.write(1, 2, label='全日制学生数', style=header_style)
        worksheet.write(1, 3, label='延期人数', style=header_style)
        worksheet.write_merge(1, 1, 4, 12, label='论文检测', style=header_style)
        worksheet.write_merge(1, 1, 13, 14, label='盲审', style=header_style)
        worksheet.write(1, 15, label='答辩', style=header_style)
        worksheet.write_merge(1, 1, 16, 17, label='评优', style=header_style)
        worksheet.write_merge(1, 1, 18, 19, label='毕业情况', style=header_style)
        worksheet.write_merge(1, 1, 20, 21, label='获学位情况', style=header_style)

        for index, value in enumerate(['', '', '', '人数', '人数', '一次通过人数', '一次通过率', '不合格人数',
                                       '不合格占比', '15%以下人数', '15%以下占比', '10%以下人数', '10%以下占比', '比例',
                                       '未通过人数', '未通过人数', '名额', '评选结果', '毕业人数', '毕业率', '获学位人数',
                                       '获学位率']):
            worksheet.write(2, index, label=value, style=header_style)

        # 行高
        tall_style = xlwt.easyxf('font:height 240;')
        first_row = worksheet.row(1)
        first_row.set_style(tall_style)

        data_len = len(paper_list)
        for line, data in enumerate(paper_list):
            for index, value in enumerate(["", "academy", "full_time_count", "delay_count", "paper_stu_count",
                                           "paper_pass_count", "paper_pass_proportion", "paper_fail_count",
                                           "paper_fail_proportion", "paper_fifteen_count", "paper_fifteen_proportion",
                                           "paper_ten_count", "paper_ten_proportion", "blind_trial_proportion",
                                           "blind_trial_count", "reply_count", "evaluation_count", "evaluation_result",
                                           "graduate_count", "graduate_proportion", "degree_count",
                                           "degree_proportion"]):
                if index == 0:
                    worksheet.write(line + 3, 0, label=line + 1, style=table_center_style)
                else:
                    worksheet.write(line + 3, index, label=data[value], style=table_center_style)

        # 合计汇总行
        full_time_all_count = student_data.filter(stu_learn_type="S1").count()
        delay_all_count = student_data.filter(stu_thesis__the_is_delay=True).count()
        student_all_count = student_data.count()
        paper_one_pass_all_count = student_data.filter(stu_thesis__the_exam_count=1).count()
        paper_fail_all_count = student_data.filter(stu_thesis__pla_thesis__pla_result=False).count()
        paper_fifteen_all_count = student_data.filter(stu_thesis__pla_thesis__pla_rate__lt=15).count()
        paper_ten_all_count = student_data.filter(stu_thesis__pla_thesis__pla_rate__lt=10).count()
        
        blind_trial_all_count = student_data.filter(stu_thesis__bli_thesis__bli_date__year=year).count()
        blind_trial_fail_all_count = student_data.filter(stu_thesis__bli_thesis__bli_score="不合格").count()
        final_fail_all_count = student_data.filter(stu_thesis__the_final_score=False).count()
        ia_superb_all_count = student_data.filter(stu_thesis__the_is_superb=True).count()
        graduate_pass_all_count = student_data.filter(stu_gain_cert=True).count()
        degree_all_count = student_data.filter(stu_gain_diploma=True).count()
        
        for i, value in enumerate([data_len + 1, '合计', full_time_all_count, delay_all_count, student_all_count,
                                   paper_one_pass_all_count,
                                   '{:.0%}'.format(paper_one_pass_all_count / student_all_count), paper_fail_all_count,
                                   '{:.0%}'.format(paper_fail_all_count / student_all_count), paper_fifteen_all_count,
                                   '{:.0%}'.format(paper_fifteen_all_count / student_all_count), paper_ten_all_count,
                                   '{:.0%}'.format(paper_ten_all_count / student_all_count),
                                   '{:.0%}'.format(blind_trial_all_count / student_all_count),
                                   blind_trial_fail_all_count, final_fail_all_count, 123, ia_superb_all_count,
                                   graduate_pass_all_count, '{:.0%}'.format(graduate_pass_all_count / student_all_count),
                                   degree_all_count, '{:.0%}'.format(degree_all_count / student_all_count),
                                   ]):
            worksheet.write(data_len + 3, i, label=value, style=table_center_style)

        # 保存
        workbook.save(os.path.join(settings.BASE_DIR, 'paper_quality.xls'))
        if os.path.exists(os.path.join(settings.BASE_DIR, 'paper_quality.xls')):
            with open(os.path.join(settings.BASE_DIR, 'paper_quality.xls'), 'rb') as excel:
                response = HttpResponse(excel.read(), 'application/vnd.ms-excel')
                response['Content-Disposition'] = "attachment;filename={}".format('paper_quality.xls')
            return response
        else:
            raise FileNotFoundError
