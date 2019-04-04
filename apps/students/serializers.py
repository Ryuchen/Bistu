#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ==================================================
# @Time : 2019-04-02 20:11 
# @Author : libin
# @Site :  
# @File : views.py
# @Desc : 
# ==================================================
from rest_framework import serializers
from contrib.users.models import Student, Education, Class, Tutor


class EducationSerializers(serializers.ModelSerializer):
	class Meta:
		model = Education
		fields = '__all__'


class ClassSerializers(serializers.ModelSerializer):
	class Meta:
		model = Class
		fields = '__all__'


class TutorSerializers(serializers.ModelSerializer):
	class Meta:
		model = Tutor
		fields = '__all__'


class StudentSerializers(serializers.ModelSerializer):
	class Meta:
		model = Student
		fields = '__all__'
