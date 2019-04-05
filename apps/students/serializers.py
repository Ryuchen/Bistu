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
from contrib.academy.models import Academy, Major


class TutorSerializers(serializers.ModelSerializer):
	class Meta:
		model = Tutor
		fields = '__all__'


class StudentSerializers(serializers.ModelSerializer):
	classes = serializers.SlugRelatedField(many=False, queryset=Class.objects.all(), slug_field='maj_name')
	academy = serializers.SlugRelatedField(many=False, queryset=Academy.objects.all(), slug_field='academy')
	major = serializers.SlugRelatedField(many=False, queryset=Major.objects.all(), slug_field='majors')
	tutor = serializers.SlugRelatedField(many=False, queryset=Tutor.objects.all(), slug_field='tutor')

	class Meta:
		model = Student
		fields = '__all__'
