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

from django import template
from django.conf import settings
from django.utils.encoding import force_text
from django.utils.functional import Promise
from django.core.serializers.json import DjangoJSONEncoder
from django.utils.safestring import mark_safe

from core.templatetags.simpletags import _import_reload

register = template.Library()


def unicode_to_str(u):
    return u.encode()


class LazyEncoder(DjangoJSONEncoder):
    """
    解决json __proxy__ 问题
    """

    def default(self, obj):
        if isinstance(obj, Promise):
            return force_text(obj)
        return super(LazyEncoder, self).default(obj)


def __get_config(name):
    value = os.environ.get(name, getattr(settings, name, None))
    return value


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


@register.filter
def config(key):
    return __get_config(key)
