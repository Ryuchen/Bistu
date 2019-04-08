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
from contrib.academy.models import Major, Academy, Research


class ResearchSerializers(serializers.ModelSerializer):
	""" 科研方向 """
	class Meta:
		model = Research
		fields = '__all__'


class MajorSerializers(serializers.ModelSerializer):
	""" 学科专业 """
	# research = serializers.SlugRelatedField(many=True, queryset=Research.objects.filter(), slug_field='res_name')
	research = ResearchSerializers(many=True)

	class Meta:
		model = Major
		fields = '__all__'


class AcademySerializers(serializers.ModelSerializer):
	""" 学院 """
	majors = MajorSerializers(many=True)
	# majors = serializers.SlugRelatedField(many=True, queryset=Major.objects.filter(), slug_field='maj_name')

	class Meta:
		model = Academy
		fields = '__all__'

