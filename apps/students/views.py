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
from rest_framework.response import Response
from rest_framework import mixins, generics, status
from django.views.decorators.csrf import csrf_exempt
from rest_framework.pagination import LimitOffsetPagination

from contrib.users.models import Student
from core.decorators.excepts import excepts
from apps.teachers.views import user_chanle
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
						'stu_class', 'major_category', 'stu_name')
	ordering_fields = ('stu_number', 'stu_entrance_time', 'stu_graduation_time', 'stu_birth_day')


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
		serializer = self.get_serializer(instance, data=data, partial=partial, context={"stu_academy": "", 'stu_user': "", "stu_major": "", "stu_tutor": ""})
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
		return queryset

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
			return self.get_paginated_response(serializer.data)

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
			data["stu_major"] = Major.objects.filter(maj_name=data.get('stu_major')).uuid
			data["stu_academy"] = Academy.objects.filter(aca_cname=data.get('stu_academy')).uuid
			serializer = self.get_serializer(data=data, context={"stu_academy": "", 'stu_user': "", "stu_major": "", "stu_tutor": ""})
		else:
			for item in data:
				username = item['user']
				item["user"] = user_chanle(username)
				data["stu_major"] = Major.objects.filter(maj_name=item['stu_major']).uuid
				data["stu_academy"] = Academy.objects.filter(aca_cname=item['stu_academy']).uuid
			serializer = self.get_serializer(data=data, many=True, context={"stu_academy": "", 'stu_user': "", "stu_major": "", "stu_tutor": ""})
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
		s_list = list()
		for i in range(1, nrows):
			rowx = table.row_values(i)
			student_dict = dict()
			student_dict["user"] = user_chanle(rowx[0])
			student_dict["stu_number"] = rowx[1]
			student_dict["stu_candidate_number"] = rowx[2]
			student_dict["stu_card_type"] = rowx[3]
			student_dict["stu_cardID"] = rowx[4]
			student_dict["stu_gender"] = rowx[5]
			student_dict["stu_birth_day"] = rowx[6]
			student_dict["stu_nation"] = rowx[7]
			student_dict["stu_source"] = rowx[8]
			student_dict["stu_is_village"] = True if rowx[9] == "是" else False
			student_dict["stu_political"] = rowx[10]
			student_dict["academy"] = Academy.objects.filter(aca_cname=rowx[11]).uuid
			student_dict["major"] = Major.objects.filter(maj_name=rowx[12]).uuid
			student_dict["major_category"] = rowx[13]
			student_dict["stu_class"] = rowx[14]
			student_dict["stu_status"] = rowx[15]
			student_dict["tutor"] = rowx[16]
			student_dict["stu_type"] = rowx[17]
			student_dict["stu_learn_type"] = rowx[18]
			student_dict["stu_learn_status"] = rowx[19]
			student_dict["stu_grade"] = rowx[20]
			student_dict["stu_system"] = rowx[21]
			student_dict["stu_entrance_time"] = rowx[22]
			student_dict["stu_cultivating_mode"] = rowx[23]
			student_dict["stu_enrollment_category"] = rowx[24]
			student_dict["stu_natioanlity"] = rowx[25]
			student_dict["stu_special_program"] = rowx[26]
			student_dict["stu_is_regular_income"] = True if rowx[27] == "是" else False
			student_dict["stu_is_tuition_fees"] = True if rowx[28] == "是" else False
			student_dict["stu_is_achives"] = True if rowx[29] == "是" else False
			student_dict["stu_graduation_time"] = rowx[30]
			s_list.append(student_dict)
		serializer = self.get_serializer(data=s_list, many=True, context={"stu_academy": "", 'stu_user': "", "stu_major": "", "stu_tutor": ""})
		serializer.is_valid(raise_exception=True)
		serializer.save()
		res['data'] = serializer.data
		return Response(res)

