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
from contrib.education.models import Thesis
from apps.students.serializers import StudentSerializers


class ThesisSerializers(serializers.ModelSerializer):
    """ 论文 """
    student = StudentSerializers(many=False)

    class Meta:
        model = Thesis
        fields = '__all__'

    def create(self, validated_data):
        student = validated_data.pop("student")
        thesis = Thesis.objects.create(student=student, **validated_data)
        return thesis
