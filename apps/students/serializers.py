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
from django.contrib.auth.models import User
from contrib.users.models import Student, Tutor
from contrib.academy.models import Academy, Major
from apps.teachers.serializers import UserSerializers
from apps.colleges.serializers import AcademySerializers


class StudentSerializers(serializers.ModelSerializer):
	user = UserSerializers(many=False)
	academy = AcademySerializers(many=False)
	major = serializers.SlugRelatedField(many=False, queryset=Major.objects.all(), slug_field='maj_name')
	tutor = serializers.SlugRelatedField(many=False, queryset=Tutor.objects.all(), slug_field='tut_number')

	class Meta:
		model = Student
		fields = '__all__'
		depth = 2
		extra_kwargs = {
			'major': {'lookup_field': 'maj_name'},
			'user': {'lookup_field': 'username'},
			'academy': {'lookup_field': 'aca_cname'},
			'tutor': {'lookup_field': 'tut_number'}
		}

	def create(self, validated_data):
		user = validated_data.pop('user')
		if not User.objects.filter(username=user.get('username')).count():
			user = User.objects.create(**user)
		new_tutor = Student.objects.create(user=user, **validated_data)
		return new_tutor

	def update(self, instance, validated_data):
		username = validated_data.get('user')['username']
		if not User.objects.filter(username=username).count():
			User.objects.filter(id=instance.user_id).update(username=username)
		return instance

