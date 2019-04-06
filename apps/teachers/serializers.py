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
from contrib.users.models import Tutor, Education
from contrib.academy.models import Academy
from apps.accounts.serializers import UserSerializers


class EducationSerializers(serializers.ModelSerializer):
	""" 学历 """

	class Meta:
		model = Education
		fields = '__all__'


class TutorSerializers(serializers.ModelSerializer):
	""" 老师 """
	user = UserSerializers(many=False)
	academy = serializers.SlugRelatedField(many=False, queryset=Academy.objects.all(), slug_field='aca_name')
	education = EducationSerializers(many=False)

	class Meta:
		model = Tutor
		fields = '__all__'

	def create(self, validated_data):
		user = validated_data.pop('user')
		education = validated_data.pop('education')
		if not User.objects.filter(username=user.get('username')).count():
			user = User.objects.create(**user)
		education = Education.objects.create(**education)

		new_tutor = Tutor.objects.create(user=user, education=education, **validated_data)
		return new_tutor

	def update(self, instance, validated_data):
		username = validated_data.get('user')['username']
		education = validated_data.get('education')
		if not User.objects.filter(username=username).count():
			User.objects.filter(id=instance.user_id).update(username=username)
		if isinstance(education, dict):
			Education.objects.filter(uuid=instance.education_id).update(**education)
		return instance
