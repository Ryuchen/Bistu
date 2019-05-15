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


class MajorForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(MajorForm, self).__init__(*args, **kwargs)
        self.fields['maj_type'].choices = MajorTypeChoice
        self.fields['maj_degree'].choices = MajorDegreeChoice

    class Meta:
        model = Major
        fields = '__all__'
