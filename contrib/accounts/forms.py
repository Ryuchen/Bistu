#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ==================================================
# @Time : 2019-05-12 15:22
# @Author : ryuchen
# @Site :
# @File : forms.py
# @Desc :
# ==================================================
from .models import *

from core.definition.enums import *

from django.forms import ModelForm


class TutorForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(TutorForm, self).__init__(*args, **kwargs)
        self.fields['tut_gender'].choices = GenderChoice
        self.fields['tut_academy'].choices = [(academy.uuid, academy.aca_cname) for academy in Academy.objects.all()]

    class Meta:
        model = Tutor
        fields = '__all__'


class StudentForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)
        self.fields['stu_gender'].choices = GenderChoice
        self.fields['stu_status'].choices = StudentStatusChoice
        self.fields['stu_mid_check'].choices = MidCheckChoice
        self.fields['stu_academy'].choices = [(academy.uuid, academy.aca_cname) for academy in Academy.objects.all()]
        self.fields['stu_major'].choices = [(major.uuid, major.maj_name) for major in Major.objects.all()]
        self.fields['stu_class'].choices = [(item.uuid, item.cla_name) for item in Class.objects.all()]
        self.fields['stu_research'].choices = [(research.uuid, research.res_name) for research in Research.objects.all()]
        self.fields['stu_tutor'].choices = [(tutor.uuid, tutor.tut_name) for tutor in Tutor.objects.all()]
        self.fields['stu_special_program'].choices = SpecialProgramChoice

    class Meta:
        model = Student
        fields = '__all__'
