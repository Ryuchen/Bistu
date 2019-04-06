#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ==================================================
# @Time : 2019-04-02 20:11 
# @Author : ryuchen
# @Site :  
# @File : views.py
# @Desc : 
# ==================================================
import xlrd
from rest_framework import generics, status
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from core.decorators.excepts import excepts
from contrib.academy.models import Academy, Major
from .serializers import MajorSerializers, AcademySerializers


class SimpleMajor(object):
	model = Major
	queryset = Major.objects.all()
	serializer_class = MajorSerializers


class MajorDetail(SimpleMajor, generics.RetrieveUpdateDestroyAPIView):
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


class MajorList(SimpleMajor, generics.GenericAPIView):
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
			serializer = self.get_serializer(data=data)
		else:
			serializer = self.get_serializer(data=data, many=True)
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
		m_list = list()
		for i in range(1, nrows):
			row = table.row_values(i)
			m_dict = dict()
			m_dict["maj_code"] = row[0]
			m_dict["maj_name"] = row[1]
			m_dict["maj_type"] = row[2]
			m_list.append(m_dict)
		serializer = self.get_serializer(data=m_list, many=True)
		serializer.is_valid(raise_exception=True)
		serializer.save()
		res['data'] = serializer.data
		return Response(res)


class SimpleAcademy(object):
	model = Academy
	queryset = Academy.objects.all()
	serializer_class = AcademySerializers


class AcademyDetail(SimpleAcademy, generics.RetrieveUpdateDestroyAPIView):
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


class AcademyList(SimpleAcademy, generics.GenericAPIView):
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
			serializer = self.get_serializer(data=data, context={"majors": ""})
		else:
			serializer = self.get_serializer(data=data, many=True, context={"majors": ""})
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
		res['data'] = serializer.data
		return Response(res)

