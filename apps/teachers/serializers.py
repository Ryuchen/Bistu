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
from contrib.accounts.models import Tutor, Education
from apps.accounts.serializers import UserSerializers
from apps.colleges.serializers import AcademySerializers


class EducationSerializers(serializers.ModelSerializer):
    """ 学历 """

    class Meta:
        model = Education
        fields = '__all__'


class TutorSerializers(serializers.ModelSerializer):
    """ 老师 """
    user = UserSerializers(many=False)
    academy = AcademySerializers(many=False, allow_null=True)
    education = EducationSerializers(many=False, allow_null=True)

    class Meta:
        model = Tutor
        fields = '__all__'

    def to_representation(self, instance):
        instance.tut_gender = instance.get_tut_gender_display()
        instance.tut_title = instance.get_tut_title_display()
        instance.tut_political = instance.get_tut_political_display()
        instance.tut_degree = instance.get_tut_degree_display()
        data = super(TutorSerializers, self).to_representation(instance)
        return data

    def create(self, validated_data):
        user = validated_data.pop('user')
        academy = validated_data.pop('academy')
        education = validated_data.pop('education')

        if not User.objects.filter(first_name=user.get('first_name')).count():
            user = User.objects.create(**user)
        else:
            user = User.objects.filter(first_name=user['first_name']).first()

        if education:
            new_tutor = Tutor.objects.create(user=user, academy=academy, education=education,  **validated_data)
        else:
            new_tutor = Tutor.objects.create(user=user, academy=academy, **validated_data)

        return new_tutor

    def update(self, instance, validated_data):
        username = validated_data.get('user')['username']
        education = validated_data.get('education')
        if not User.objects.filter(username=username).count():
            User.objects.filter(id=instance.user_id).update(username=username)
        if isinstance(education, dict):
            Education.objects.filter(uuid=instance.education_id).update(**education)
        return instance
