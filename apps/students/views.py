#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ==================================================
# @Time : 2019-04-02 20:11 
# @Author : libin
# @Site :  
# @File : views.py
# @Desc : 
# ==================================================
from rest_framework import generics, status
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt

from core.decorators.excepts import excepts
from contrib.users.models import Student
from apps.students.serializers import StudentSerializers


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
		partial = kwargs.pop('partial', False)
		instance = self.get_object()
		serializer = self.get_serializer(instance, data=request.data, partial=partial)
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
		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		self.perform_create(serializer)
		res['data'] = serializer.data
		return Response(res)

