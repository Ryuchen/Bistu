#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ==================================================
# @Time : 2019-04-02 20:11 
# @Author : ryuchen
# @Site :  
# @File : views.py
# @Desc : 
# ==================================================
from rest_framework import generics, status
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework_bulk import generics
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


class MajorList(SimpleMajor, generics.ListCreateAPIView):
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


class AcademyList(SimpleAcademy, generics.ListCreateAPIView):
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