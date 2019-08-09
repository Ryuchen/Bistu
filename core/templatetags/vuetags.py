#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ==================================================
# @Time : 2019-08-04 00:29
# @Author : ryuchen
# @File : vuetags.py
# @Desc :
# ==================================================
import os
import json
import datetime

from django import template
from django.conf import settings
from django.utils.encoding import force_text
from django.utils.functional import Promise
from django.core.serializers.json import DjangoJSONEncoder
from django.contrib.admin.templatetags.base import InclusionAdminNode

from django.contrib.admin.views.main import (
    ALL_VAR, ORDER_VAR, PAGE_VAR, SEARCH_VAR,
)
from django.db import models
from django.utils import formats
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from django.utils.text import capfirst
from django.utils.translation import gettext as _

register = template.Library()


def unicode_to_str(u):
    return u.encode()


def _field_display(model, field_name):
    for f in model._meta.fields:
        if f.name == field_name:
            if hasattr(f, 'verbose_name'):
                return getattr(f, 'verbose_name')

    return field_name


def __get_config(name):
    value = os.environ.get(name, getattr(settings, name, None))
    return value


def _import_reload(_modules):
    _obj = __import__(_modules, fromlist=_modules.split('.'))
    return _obj


class LazyEncoder(DjangoJSONEncoder):
    """
    解决json __proxy__ 问题
    """

    def default(self, obj):
        if isinstance(obj, Promise):
            return force_text(obj)
        return super(LazyEncoder, self).default(obj)


@register.simple_tag
def adv_logo():
    logo = {
        "full": {
            "src": ""
        },
        "mini": {
            "src": "",
        },
        "alt": "logo"
    }
    logo["full"]["src"] = __get_config('ANT_DESIGN_VUE_HEADER_LOGOFULL')
    logo["mini"]["src"] = __get_config('ANT_DESIGN_VUE_HEADER_LOGOMINI')

    return mark_safe(json.dumps(logo, cls=LazyEncoder))


@register.simple_tag
def adv_toolbox():
    toolbox = {
        "lock": {
            "enable": True,
            "verify": "email"
        },
        "github": {
            "enable": True,
            "link": "https://github.com/ryuchen"
        },
        "search": {
            "enable": True
        },
        "notice": {
            "enable": True
        },
        "utility": {
            "enable": True
        },
        "setting": {
            "enable": True
        }
    }
    # TODO: add support verify method after locking screen
    toolbox["lock"]["enable"] = __get_config('ANT_DESIGN_VUE_HEADER_TOOLBOX_LOCK')
    toolbox["github"]["enable"] = __get_config('ANT_DESIGN_VUE_HEADER_TOOLBOX_GITHUB')
    toolbox["github"]["link"] = __get_config('GITHUB_URL')
    toolbox["search"]["enable"] = __get_config('ANT_DESIGN_VUE_HEADER_TOOLBOX_SEARCH')
    toolbox["notice"]["enable"] = __get_config('ANT_DESIGN_VUE_HEADER_TOOLBOX_NOTICE')
    toolbox["utility"]["enable"] = __get_config('ANT_DESIGN_VUE_HEADER_TOOLBOX_UTILITY')
    toolbox["setting"]["enable"] = __get_config('ANT_DESIGN_VUE_HEADER_TOOLBOX_SETTING')
    return mark_safe(json.dumps(toolbox, cls=LazyEncoder))


@register.simple_tag
def adv_home():
    home = {
        "type": "",
        "title": "",
        "url": ""
    }
    home_type = __get_config('ANT_DESIGN_VUE_HOME_TYPE')
    home["type"] = home_type
    if home["type"] in ["Workplace", "Overview"]:
        home["title"] = home_type

    if home["type"] == "Customize":
        home["title"] = __get_config('ANT_DESIGN_VUE_HOME_TITLE')
        home["url"] = __get_config('ANT_DESIGN_VUE_HOME_URL')
    return mark_safe(json.dumps(home, cls=LazyEncoder))


@register.simple_tag(takes_context=True)
def adv_menu(context):
    data = []

    menus = __get_config('ANT_DESIGN_VUE_NAV_MENUS')
    if menus:  # if user define site menus use defines!
        if __get_config('ANT_DESIGN_VUE_NAV_MENUS_DYNAMIC'):
            menus = _import_reload(__get_config('DJANGO_SETTINGS_MODULE')).ANT_DESIGN_VUE_NAV_MENUS
        key_start = 1
        for menu in menus:
            if "models" in menu and menu["models"]:
                menu["key"] = "sub{}".format(key_start)
                for model in menu["models"]:
                    key_start += 1
                    model["key"] = "{}".format(key_start)
            else:
                key_start += 1
                menu["key"] = "{}".format(key_start)
        data = menus
    else:  # if user not define site menus use default!
        app_list = context.get('app_list')
        for app in app_list:
            _models = [
                {
                    'name': m.get('name'),
                    'icon': '',
                    'url': m.get('admin_url'),
                }
                for m in app.get('models')
            ] if app.get('models') else []

            module = {
                'name': app.get('name'),
                'icon': '',
                'models': _models
            }
            data.append(module)

    return mark_safe(json.dumps(data, cls=LazyEncoder))


@register.simple_tag
def adv_footer():
    footer = {
        "author": "Ryuchen",
        "year": datetime.datetime.now().year,
        "link": "https://github.com/ryuchen"
    }
    year = __get_config('ANT_DESIGN_VUE_FOOTER_COPYRIGHT_YEAR')
    if year:
        footer["year"] = year

    author = __get_config('ANT_DESIGN_VUE_FOOTER_COPYRIGHT_AUTHOR')
    if author:
        footer["author"] = author

    link = __get_config('ANT_DESIGN_VUE_FOOTER_COPYRIGHT_LINK')
    if link:
        footer["link"] = link

    return mark_safe(json.dumps(footer, cls=LazyEncoder))


@register.simple_tag(takes_context=True)
def adv_search_placeholder(context):
    cl = context.get('cl')
    verboses = []

    # 取消递归，只获取2级
    if cl:
        for sf in cl.search_fields:
            verboses.append(_field_display(cl.model, sf))

    return mark_safe("，".join(verboses))


@register.simple_tag
def adv_list_filter(cl, spec):
    list_filter = {
        'title': spec.title,
        'choices': list(spec.choices(cl)),
    }
    return mark_safe(json.dumps(list_filter, cls=LazyEncoder))


@register.filter
def config(key):
    return __get_config(key)


# ############################## overwrite django admin default tags ################################
DOT = '.'


@register.simple_tag
def paginator_number(cl, i):
    """
    Generate an individual page index link in a paginated list.
    """
    if i == DOT:
        return '… '
    elif i == cl.page_num:
        return format_html('<span class="this-page">{}</span> ', i + 1)
    else:
        return format_html(
            '<a href="{}"{}>{}</a> ',
            cl.get_query_string({PAGE_VAR: i}),
            mark_safe(' class="end"' if i == cl.paginator.num_pages - 1 else ''),
            i + 1,
        )


@register.simple_tag(name='adv_pagination')
def pagination_tag(cl):
    """
    Generate the series of links to the pages in a paginated list.
    """
    paginator, page_num = cl.paginator, cl.page_num
    return mark_safe(json.dumps({
        'current': page_num,
        'total': paginator.count,
        'link': cl.get_query_string({PAGE_VAR: page_num}),
        'size': 20
    }))


def date_hierarchy(cl):
    """
    Display the date hierarchy for date drill-down functionality.
    """
    if cl.date_hierarchy:
        field_name = cl.date_hierarchy
        year_field = '%s__year' % field_name
        month_field = '%s__month' % field_name
        day_field = '%s__day' % field_name
        field_generic = '%s__' % field_name
        year_lookup = cl.params.get(year_field)
        month_lookup = cl.params.get(month_field)
        day_lookup = cl.params.get(day_field)

        def link(filters):
            return cl.get_query_string(filters, [field_generic])

        if not (year_lookup or month_lookup or day_lookup):
            # select appropriate start level
            date_range = cl.queryset.aggregate(first=models.Min(field_name),
                                               last=models.Max(field_name))
            if date_range['first'] and date_range['last']:
                if date_range['first'].year == date_range['last'].year:
                    year_lookup = date_range['first'].year
                    if date_range['first'].month == date_range['last'].month:
                        month_lookup = date_range['first'].month

        if year_lookup and month_lookup and day_lookup:
            day = datetime.date(int(year_lookup), int(month_lookup), int(day_lookup))
            return {
                'show': True,
                'name': _field_display(cl.model, field_name),
                'back': {
                    'link': link({year_field: year_lookup, month_field: month_lookup}),
                    'title': capfirst(formats.date_format(day, 'YEAR_MONTH_FORMAT'))
                },
                'choices': [{'title': capfirst(formats.date_format(day, 'MONTH_DAY_FORMAT'))}]
            }
        elif year_lookup and month_lookup:
            days = getattr(cl.queryset, 'dates')(field_name, 'day')
            return {
                'show': True,
                'name': _field_display(cl.model, field_name),
                'back': {
                    'link': link({year_field: year_lookup}),
                    'title': str(year_lookup)
                },
                'choices': [{
                    'link': link({year_field: year_lookup, month_field: month_lookup, day_field: day.day}),
                    'title': capfirst(formats.date_format(day, 'MONTH_DAY_FORMAT'))
                } for day in days]
            }
        elif year_lookup:
            months = getattr(cl.queryset, 'dates')(field_name, 'month')
            return {
                'show': True,
                'name': _field_display(cl.model, field_name),
                'back': {
                    'link': link({}),
                    'title': _('All dates')
                },
                'choices': [{
                    'link': link({year_field: year_lookup, month_field: month.month}),
                    'title': capfirst(formats.date_format(month, 'YEAR_MONTH_FORMAT'))
                } for month in months]
            }
        else:
            years = getattr(cl.queryset, 'dates')(field_name, 'year')
            return {
                'show': True,
                'name': _field_display(cl.model, field_name),
                'back': None,
                'choices': [{
                    'link': link({year_field: str(year.year)}),
                    'title': str(year.year),
                } for year in years]
            }


@register.tag(name='adv_date_hierarchy')
def date_hierarchy_tag(parser, token):
    return InclusionAdminNode(
        parser, token,
        func=date_hierarchy,
        template_name='date_hierarchy.html',
        takes_context=False,
    )

# ############################## overwrite django admin default tags ################################

