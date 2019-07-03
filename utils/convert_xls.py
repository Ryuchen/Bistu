#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ==================================================
# @Time : 2019-06-24 14:58
# @Author : ryuchen
# @File : convert_xls.py
# @Desc :
# ==================================================
import re
import xlrd
import json

objects = []

regex = r"^(?P<code>\d*)(?P<name>.*)\((?P<type>.*)\)"


# 读取学校excel的内容
def read_college_information():
    data = xlrd.open_workbook('data2.xlsx')

    # 获取每个sheet的名称 => 对应的是学院名称
    tables = data.sheets()
    # 第一步：将excel的数据格式化
    entity_list = list()
    for table in tables:
        entity_dict = dict()
        entity_dict["academy"] = table.name.strip()
        keys = table.row_values(1)
        entity_dict["majors"] = []
        # entity_dict["tutors"] = []
        rows_num = table.nrows  # 行
        # cols_num = table.ncols  # 列
        for r in range(2, rows_num - 1):
            major_cell_value = table.row_values(r)[0]
            if major_cell_value != "":
                matches = re.findall(regex, major_cell_value, re.MULTILINE)
                if matches:
                    major = {"code": matches[0][0], "name": matches[0][1], "type": matches[0][2]}
                    entity_dict["majors"].append(major)
        #
        #     tutor_cell_value = table.row_values(r)[1]
        #     if tutor_cell_value != "":
        #         entity_dict["tutors"].append(tutor_cell_value)
        #
        #     student_cell_value = table.row_values(r)[2]
        #     print(student_cell_value)

        objects.append(entity_dict)

    return objects


# 读取学生信息的内容

def read_student_information():
    data = xlrd.open_workbook('data1.xlsx')

    # 读取学生信息表
    table = data.sheet_by_index(0)

    # 第一步：将excel的数据格式化
    students = []
    majors = set()

    rows_num = table.nrows  # 行

    keys = table.row_values(0)
    for r in range(2, rows_num - 1):
        values = table.row_values(r)
        majors.add((values[11], values[12]))
        student = dict(zip(keys, values))
        # print(student)
        students.append(student)

    return majors


if __name__ == "__main__":
    all_majors = read_student_information()
    all_colleges = read_college_information()

    for item in all_colleges:
        for _ in item["majors"]:
            major = (_["code"], _["name"])
            if major in all_majors:
                print("in", major)
            else:
                print("out", major)
