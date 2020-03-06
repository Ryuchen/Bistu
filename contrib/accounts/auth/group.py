#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ==================================================
# @Time : 2020/3/6-11:35
# @Author : Ryuchen
# @Site : https://ryuchen.github.io
# @File : group
# @Desc : 
# ==================================================
from django.contrib import admin
from django.contrib.auth.models import Group
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters

csrf_protect_m = method_decorator(csrf_protect)
sensitive_post_parameters_m = method_decorator(sensitive_post_parameters())


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    ordering = ('name',)
    filter_horizontal = ('permissions',)

    def formfield_for_manytomany(self, db_field, request=None, **kwargs):
        if db_field.name == 'permissions':
            qs = kwargs.get('queryset', db_field.remote_field.model.objects)
            # Avoid a major performance hit resolving permission names which
            # triggers a content_type load:
            kwargs['queryset'] = qs.select_related('content_type')
        return super().formfield_for_manytomany(db_field, request=request, **kwargs)
