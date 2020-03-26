#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ==================================================
# @Author : Copyright@Ryuchen
# ==================================================

import re

import xlrd
import json


def read_student_information():
    data = xlrd.open_workbook('greenbirds.xlsx')

    # 读取学生信息表
    table = data.sheet_by_index(0)
    # 第一步：将excel的数据格式化
    students = []
    classes = set()
    majors = set()
    academies = set()

    rows_num = table.nrows  # 行

    keys = table.row_values(1)
    for r in range(2, rows_num - 1):
        values = table.row_values(r)
        classes.add(values[11])
        majors.add((values[5], values[6]))

        academies.add(values[15])
        student = dict(zip(keys, values))
        students.append(student)
    return {
        'academies': academies,
        'majors': majors,
        'classes': classes,
        'students': students
    }


if __name__ == "__main__":
    print(read_student_information())
