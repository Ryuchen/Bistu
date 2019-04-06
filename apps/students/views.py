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
from rest_framework import generics, status
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt

from core.decorators.excepts import excepts
from contrib.users.models import Student
from apps.students.serializers import StudentSerializers
from apps.teachers.views import user_chanle


class SimpleStudent(object):
	model = Student
	queryset = Student.objects.all()
	serializer_class = StudentSerializers


class StudentDetail(SimpleStudent, generics.RetrieveUpdateDestroyAPIView):
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
										 context={"stu_academy": "", 'stu_user': "", "stu_major": "", "stu_tutor": ""})
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


class StudentList(SimpleStudent, generics.ListCreateAPIView):
	@excepts
	@csrf_exempt
	def get(self, request, *args, **kwargs):
		res = {
			'code': status.HTTP_200_OK,
			'data': []
		}
		queryset = self.filter_queryset(self.get_queryset())
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
			serializer = self.get_serializer(data=data, context={"stu_academy": "", 'stu_user': "", "stu_major": "", "stu_tutor": ""})
		else:
			for item in data:
				username = item['user']
				item["user"] = user_chanle(username)
			serializer = self.get_serializer(data=data, many=True, context={"stu_academy": "", 'stu_user': "", "stu_major": "", "stu_tutor": ""})
		serializer.is_valid(raise_exception=True)
		self.perform_create(serializer)
		res['data'] = serializer.data
		return Response(res)


@excepts
@csrf_exempt
def upload_student(request):
	res = {
		'code': status.HTTP_200_OK,
		'data': {}
	}
	file = request.FILES.get('students')
	data = xlrd.open_workbook(file)
	table = data.sheets()[0]
	# table_name = table.name
	nrows = table.nrows  # 获取该sheet中的有效行数
	ncols = table.ncols  # 获取该sheet中的有效行数
	student_list = list()
	for rowx in nrows:
		table.row(rowx)  # 返回由该行中所有的单元格对象组成的列
		student_dict = dict()
		student_dict["user"] = rowx[0]
		student_dict["stu_number"] = rowx[1]
		student_dict["stu_candidate_number"] = rowx[1]
		student_dict["stu_card_type"] = rowx[1]
		student_dict["stu_cardID"] = rowx[1]
		student_dict["stu_gender"] = rowx[1]
		student_dict["stu_birth_day"] = rowx[1]
		student_dict["stu_nation"] = rowx[1]
		student_dict["stu_source"] = rowx[1]
		student_dict["stu_is_village"] = rowx[1]
		student_dict["stu_political"] = rowx[1]
		student_dict["academy"] = rowx[1]
		student_dict["major"] = rowx[1]

		student_dict[""] = rowx[1]
		student_dict["stu_class"] = rowx[1]
		student_dict["stu_status"] = rowx[1]
		student_dict["tutor"] = rowx[1]
		student_dict["stu_type"] = rowx[1]
		student_dict["stu_learn_type"] = rowx[1]
		student_dict["stu_learn_status"] = rowx[1]
		student_dict["stu_grade"] = rowx[1]
		student_dict["stu_system"] = rowx[1]
		student_dict["stu_entrance_time"] = rowx[1]
		student_dict["stu_cultivating_mode"] = rowx[1]
		student_dict["stu_enrollment_category"] = rowx[1]
		student_dict["stu_natioanlity"] = rowx[1]
		student_dict["stu_special_program"] = rowx[1]
		student_dict["stu_is_regular_income"] = rowx[1]
		student_dict["stu_is_tuition_fees"] = rowx[1]
		student_dict["stu_is_achives"] = rowx[1]
		student_dict["stu_graduation_time"] = rowx[1]
	return Response(res)
