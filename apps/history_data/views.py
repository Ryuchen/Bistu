#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ==================================================
# @Time : 2019-05-20 17:38 
# @Author : libin
# @Site :  
# @File : views.py 
# @Desc : 
# ==================================================
import re
import xlrd

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import make_password

from django.contrib.auth.models import User
from contrib.accounts.models import Student, Tutor
from contrib.colleges.models import Academy, Major, Class

default_password = make_password('123456')


def get_merged_cells(sheet):
    return sheet.merged_cells


def get_merged_cells_value(sheet, row_index, col_index):
    merged = get_merged_cells(sheet)
    for (rlow, rhigh, clow, chigh) in merged:
        if (row_index >= rlow and row_index < rhigh):
            if (col_index >= clow and col_index < chigh):
                cell_value = sheet.cell_value(rlow, clow)
                return cell_value
                break
    return None


@api_view(["POST"])
@csrf_exempt
def upload_history_data(request):
    res = {}
    cols_field = ["major", "tutor", "class", "student", "sub_major"]
    file = request.data['file']
    data = xlrd.open_workbook(filename=None, file_contents=file.read())
    tables = data.sheets()
    # 第一步：将excel的数据格式化
    entity_list = list()
    for table in tables:
        nrows_num = table.nrows  # 行
        cols_num = table.ncols  # 列
        aca_name = table.row_values(0)[0]  # 学院名称
        for r in range(2, nrows_num - 1):
            entity_dict = dict()
            entity_dict["academy"] = aca_name
            for c in range(0, 5):
                cell_value = table.row_values(r)[c]
                if cell_value is None or cell_value == "":
                    cell_value = get_merged_cells_value(table, r, c)
                entity_dict[cols_field[c]] = cell_value
            entity_list.append(entity_dict)

    # 第二部：将数据录入到系统中
    for item in entity_list:
        # 判断学院是否已经录入数据库
        if not Academy.objects.filter(aca_cname=item["academy"]).count():
            academy = Academy.objects.create(aca_cname=item["academy"])
        else:
            academy = Academy.objects.get(aca_cname=item["academy"])

        # 判断学科专业是否录入数据库
        maj_code = re.findall(r"^\d+", item["major"])[0]
        maj_type = "C1" if "专业学位" in item["major"] else "C2"
        if "(" in item["major"]:
            maj_name = item["major"].split("(")[0][len(maj_code):]
        else:
            maj_name = item["major"].split("（")[0][len(maj_code):]
        if not Major.objects.filter(maj_code=maj_code).count():
            major = Major.objects.create(maj_code=maj_code, maj_name=maj_name, maj_type=maj_type,
                                         maj_first=True, maj_second=False)
        else:
            major = Major.objects.get(maj_code=maj_code)
        academy.aca_majors.add(major)

        # 判断导师是否录入数据库，并加入但用户列表
        tutor_name = item["tutor"].replace(" ", "")
        if not Tutor.objects.filter(tut_name=tutor_name).count():
            if not User.objects.filter(username=tutor_name).count():
                tutor_user = User.objects.create(username=tutor_name, first_name=tutor_name[0:1], last_name=tutor_name[1:])
                tutor_user.set_password("123456")
            else:
                tutor_user = User.objects.get(username=tutor_name)
            tutor = Tutor.objects.create(tut_name=tutor_name, tut_academy=academy, tut_user=tutor_user)
        else:
            tutor = Tutor.objects.get(tut_name=tutor_name)

        # 判断班级是否落入数据库
        if not Class.objects.filter(cla_name=item["class"]).count():
            stu_class = Class.objects.create(cla_name=item["class"], cla_major=major)
        else:
            stu_class = Class.objects.get(cla_name=item["class"])

        # 判断二级学科是否落入数据库
        sub_major = item["sub_major"]
        if not Major.objects.filter(maj_name=sub_major).count():
            Major.objects.create(maj_name=sub_major, maj_first=False, maj_second=True)

        # 判断学生是否落入数据库
        student_name = item["student"].replace(" ", "")
        if not Student.objects.filter(stu_name=student_name).count():
            if not User.objects.filter(username=student_name).count():
                student_user = User.objects.create(username=student_name, first_name=student_name[0:1],
                                                   last_name=student_name[1:])
                student_user.set_password("123456")
            else:
                student_user = User.objects.get(username=student_name)

            Student.objects.create(stu_name=student_name, stu_academy=academy, stu_major=major,
                                   stu_tutor=tutor, stu_class=stu_class, stu_user=student_user)

    return Response(res, status=status.HTTP_200_OK)
