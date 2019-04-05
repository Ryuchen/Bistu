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
from contrib.users.models import Tutor
from contrib.academy.models import Academy, Major


class TutorSerializers(serializers.ModelSerializer):
	academies = serializers.SlugRelatedField(many=False, queryset=Academy.objects.all(), slug_field='academies')
	majors = serializers.SlugRelatedField(many=False, queryset=Major.objects.all(), slug_field='majors')

	class Meta:
		model = Tutor
		fields = '__all__'
