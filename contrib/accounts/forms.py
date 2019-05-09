#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ==================================================
# @Time : 2019-04-02 10:22
# @Author : ryuchen
# @Site :
# @File : models.py
# @Desc :
# ==================================================
from .models import Student
from .models import Academy
from .models import Major
from .models import Class
from .models import Research
from .models import Tutor

from core.definition.enums import *

from django.forms import ModelForm


GenderChoice = [(choice.name, choice.value) for choice in GenderChoice]

ACADEMIES = [(academy.uuid, academy.aca_cname) for academy in Academy.objects.all()]
MAJORS = [(major.uuid, major.maj_name) for major in Major.objects.all()]
CLASSES = [(item.uuid, item.cla_name) for item in Class.objects.all()]
RESEARCHES = [(research.uuid, research.res_name) for research in Research.objects.all()]
TUTORS = [(tutor.uuid, tutor.tut_name) for tutor in Tutor.objects.all()]


class StudentForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)
        self.fields['stu_gender'].choices = GenderChoice
        self.fields['stu_academy'].choices = ACADEMIES
        self.fields['stu_major'].choices = MAJORS
        self.fields['stu_class'].choices = CLASSES
        self.fields['stu_research'].choices = RESEARCHES
        self.fields['stu_tutor'].choices = TUTORS

    class Meta:
        model = Student
        fields = '__all__'
