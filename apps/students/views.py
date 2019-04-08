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

from core.decorators.excepts import excepts
from contrib.users.models import Student
from contrib.academy.models import Academy, Major
from apps.students.serializers import StudentSerializers
from apps.teachers.views import user_chanle


class SimpleStudent(object):
	model = Student
	queryset = Student.objects.all()
	serializer_class = StudentSerializers
	filterset_fields = ('stu_number', 'stu_gender', 'stu_cardID', 'stu_candidate_number', 'stu_nation', 'stu_source',
						'stu_is_village', 'stu_political', 'stu_type', 'stu_learn_type', 'stu_learn_status',
						'stu_grade', 'stu_system', 'stu_entrance_time', 'stu_graduation_time', 'stu_cultivating_mode',
						'stu_enrollment_category', 'stu_nationality', 'stu_special_program', 'stu_is_regular_income',
						'stu_is_tuition_fees', 'stu_is_archives', 'stu_is_superb', 'stu_telephone', 'stu_status',
						'stu_class', 'major_category')


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


class StudentList(SimpleStudent, mixins.ListModelMixin, generics.GenericAPIView):

	def get_queryset(self):
		queryset = self.queryset
		params = self.request.query_params
		if params:
			username = params.get('username')
			if username:
				queryset = queryset.filter(user__username=username)

			academy = params.get('academy')
			if academy:
				queryset = queryset.filter(academy__uuid=academy)

			major = params.get('major')
			if major:
				queryset = queryset.filter(major__uuid=major)

			tutor = params.get('tutor')
			if tutor:
				queryset = queryset.filter(tutor__user__username=tutor)

			# stu_number = params.get('stu_number')
			# if stu_number:
			# 	queryset = queryset.filter(stu_number=stu_number)
			#
			# stu_gender = params.get('stu_gender')
			# if stu_gender:
			# 	queryset = queryset.filter(stu_gender=stu_gender)
			#
			# stu_card_id = params.get('stu_cardID')
			# if stu_card_id:
			# 	queryset = queryset.filter(stu_cardID=stu_card_id)
			#
			# stu_candidate_number = params.get('stu_candidate_number')
			# if stu_candidate_number:
			# 	queryset = queryset.filter(stu_candidate_number=stu_candidate_number)
			#
			# stu_nation = params.get('stu_nation')
			# if stu_nation:
			# 	queryset = queryset.filter(stu_nation=stu_nation)
			#
			# stu_source = params.get('stu_source')
			# if stu_source:
			# 	queryset = queryset.filter(stu_source=stu_source)
			#
			# stu_is_village = params.get('stu_is_village')
			# if stu_is_village:
			# 	queryset = queryset.filter(stu_source=stu_source)
			#
			# stu_political = params.get('stu_political')
			# if stu_political:
			# 	queryset = queryset.filter(stu_political=stu_political)
			#
			# stu_type = params.get('stu_type')
			# if stu_type:
			# 	queryset = queryset.filter(stu_type=stu_type)
			#
			# stu_learn_type = params.get('stu_learn_type')
			# if stu_learn_type:
			# 	queryset = queryset.filter(stu_learn_type=stu_learn_type)
			#
			# stu_learn_status = params.get('stu_learn_status')
			# if stu_learn_status:
			# 	queryset = queryset.filter(stu_learn_status=stu_learn_status)
			#
			# stu_grade = params.get('stu_grade')
			# if stu_grade:
			# 	queryset = queryset.filter(stu_grade=stu_grade)
			#
			# stu_system = params.get('stu_system')
			# if stu_system:
			# 	queryset = queryset.filter(stu_system=stu_system)
			#
			# stu_entrance_time = params.get('stu_entrance_time')
			# if stu_entrance_time:
			# 	queryset = queryset.filter(stu_entrance_time=stu_entrance_time)
			#
			# stu_graduation_time = params.get('stu_graduation_time')
			# if stu_graduation_time:
			# 	queryset = queryset.filter(stu_graduation_time=stu_graduation_time)
			#
			# stu_cultivating_mode = params.get('stu_cultivating_mode')
			# if stu_cultivating_mode:
			# 	queryset = queryset.filter(stu_cultivating_mode=stu_cultivating_mode)
			#
			# stu_enrollment_category = params.get('stu_enrollment_category')
			# if stu_enrollment_category:
			# 	queryset = queryset.filter(stu_enrollment_category=stu_enrollment_category)
			#
			# stu_is_regular_income = params.get('stu_is_regular_income')
			# if stu_is_regular_income:
			# 	queryset = queryset.filter(stu_is_regular_income=stu_is_regular_income)
			#
			# stu_is_tuition_fees = params.get('stu_is_tuition_fees')
			# if stu_is_tuition_fees:
			# 	queryset = queryset.filter(stu_is_tuition_fees=stu_is_tuition_fees)
			#
			# stu_is_archives = params.get('stu_is_archives')
			# if stu_is_archives:
			# 	queryset = queryset.filter(stu_is_archives=stu_is_archives)
			#
			# stu_is_superb = params.get('stu_is_superb')
			# if stu_is_superb:
			# 	queryset = queryset.filter(stu_is_superb=stu_is_superb)
			#
			# stu_telephone = params.get('stu_telephone')
			# if stu_telephone:
			# 	queryset = queryset.filter(stu_telephone=stu_telephone)
			#
			# stu_status = params.get('stu_status')
			# if stu_status:
			# 	queryset = queryset.filter(stu_status=stu_status)
			#
			# stu_class = params.get('stu_class')
			# if stu_class:
			# 	queryset = queryset.filter(stu_class=stu_class)
			#
			# major_category = params.get('major_category')
			# if major_category:
			# 	queryset = queryset.filter(major_category=major_category)
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
			data["stu_major"] = Major.objects.filter(maj_name=data.get('stu_major')).uuid
			data["stu_academy"] = Academy.objects.filter(aca_cname=data.get('stu_academy')).uuid
			serializer = self.get_serializer(data=data, context={"stu_academy": "", 'stu_user': "", "stu_major": "", "stu_tutor": ""})
		else:
			for item in data:
				username = item['user']
				item["user"] = user_chanle(username)
				data["stu_major"] = Major.objects.filter(maj_name=item['stu_major']).uuid
				data["stu_academy"] = Academy.objects.filter(aca_cnam=item['stu_academy']).uuid
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
			student_dict["academy"] = Academy.objects.filter(aca_cnam=rowx[11]).uuid
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

