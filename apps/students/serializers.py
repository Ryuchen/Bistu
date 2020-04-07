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
from contrib.accounts.models import Student
from apps.accounts.serializers import UserSerializers
from apps.teachers.serializers import TutorSerializers
from apps.colleges.serializer import AcademySerializer, MajorSerializers


class StudentSerializers(serializers.ModelSerializer):
    stu_user = UserSerializers(many=False)
    stu_academy = AcademySerializer(many=False)
    stu_major = MajorSerializers(many=False)
    stu_tutor = TutorSerializers(many=False)

    class Meta:
        model = Student
        fields = '__all__'
        depth = 2

    def to_representation(self, instance):
        instance.stu_gender = instance.get_stu_gender_display()
        instance.stu_political = instance.get_stu_political_display()
        instance.stu_type = instance.get_stu_type_display()
        instance.stu_learn_type = instance.get_stu_learn_type_display()
        instance.stu_learn_status = instance.get_stu_learn_status_display()
        instance.stu_cultivating_mode = instance.get_stu_cultivating_mode_display()
        instance.stu_enrollment_category = instance.get_stu_enrollment_category_display()
        instance.stu_special_program = instance.get_stu_special_program_display()
        instance.stu_status = instance.get_stu_status_display()
        # instance.maj_type = instance.get_maj_type_display()
        # instance.maj_degree = instance.get_maj_degree_display()
        data = super(StudentSerializers, self).to_representation(instance)
        return data

    def to_internal_value(self, data):
        return data

    def create(self, validated_data):
        user = validated_data.pop('stu_user')
        major = validated_data.pop('stu_major')
        tutor = validated_data.pop('stu_tutor')
        academy = validated_data.pop('stu_academy')
        if not User.objects.filter(first_name=user.get('first_name')).count():
            user = User.objects.create(**user)
        else:
            user = User.objects.filter(first_name=user['first_name']).first()
        new_tutor = Student.objects.create(stu_user=user, stu_academy=academy, stu_major=major, stu_tutor=tutor, **validated_data)
        return new_tutor

    def update(self, instance, validated_data):
        username = validated_data.get('stu_user')['username']
        if not User.objects.filter(username=username).count():
            User.objects.filter(id=instance.user_id).update(username=username)
        return instance
