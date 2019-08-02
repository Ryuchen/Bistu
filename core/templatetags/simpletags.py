# -*- coding: utf-8 -*-

import os
import json

from django import template
from django.conf import settings
from django.core.serializers.json import DjangoJSONEncoder
from django.db import models
from django.db.models.fields.related import ForeignKey
from django.utils.encoding import force_text
from django.utils.functional import Promise
from django.utils.safestring import mark_safe

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


@register.simple_tag(takes_context=True)
def context_test(context):
    print(context)
    pass


@register.simple_tag(takes_context=True)
def load_dates(context):
    data = {}
    cl = context.get('cl')
    if cl.has_filters:
        for spec in cl.filter_specs:
            # 自定义的filter，没有field
            if not hasattr(spec, 'field'):
                continue

            field = spec.field
            field_type = None
            if isinstance(field, models.DateTimeField):
                field_type = 'datetime'
            elif isinstance(field, models.DateField):
                field_type = 'date'
            elif isinstance(field, models.TimeField):
                field_type = 'time'

            if field_type:
                data[field.name] = field_type
    context['date_field'] = data

    return '<script type="text/javascript">var searchDates={}</script>'.format(json.dumps(data, cls=LazyEncoder))


@register.filter
def has_filter(spec):
    return hasattr(spec, 'parameter_name')


@register.filter
def get_date_type(spec):
    field = spec.field
    field_type = ''
    if isinstance(field, models.DateTimeField):
        field_type = 'datetime'
    elif isinstance(field, models.DateField):
        field_type = 'date'
    elif isinstance(field, models.TimeField):
        field_type = 'time'

    return field_type


@register.filter
def test(obj):
    print(obj)
    return ''


@register.filter
def to_str(obj):
    return str(obj)


@register.filter
def date_to_json(obj):
    return json.dumps(obj.date_params, cls=LazyEncoder)


@register.simple_tag(takes_context=True)
def home_page(context):
    """
    处理首页，通过设置判断打开的是默认页还是自定义的页面
    :return:
    """
    home = __get_config('SIMPLEUI_HOME_PAGE')
    if home:
        context['home'] = home

    title = __get_config('SIMPLEUI_HOME_TITLE')
    if not title:
        title = '首页'

    icon = __get_config('SIMPLEUI_HOME_ICON')
    if not icon:
        icon = 'el-icon-menu'

    context['title'] = title
    context['icon'] = icon
    return ''


def __get_config(name):
    value = os.environ.get(name, getattr(settings, name, None))
    return value


@register.filter
def get_config(key):
    return __get_config(key)


@register.simple_tag(takes_context=True)
def menus(context):
    data = []

    config = get_config('SIMPLEUI_CONFIG')
    if not config:
        config = {}

    if config.get('dynamic', False) is True:
        config = _import_reload(get_config('DJANGO_SETTINGS_MODULE')).SIMPLEUI_CONFIG

    app_list = context.get('app_list')
    for app in app_list:
        _models = [
            {
                'name': m.get('name'),
                'icon': get_icon(m.get('object_name'), unicode_to_str(m.get('name'))),
                'url': m.get('admin_url'),
                'addUrl': m.get('add_url'),
                'breadcrumbs': [{
                    'name': app.get('name'),
                    'icon': get_icon(app.get('app_label'), app.get('name'))
                }, {
                    'name': m.get('name'),
                    'icon': get_icon(m.get('object_name'), unicode_to_str(m.get('name')))
                }]
            }

            for m in app.get('models')
        ] if app.get('models') else []

        module = {
            'name': app.get('name'),
            'icon': get_icon(app.get('app_label'), app.get('name')),
            'models': _models
        }
        data.append(module)

    # 如果有menu 就读取，没有就调用系统的
    key = 'system_keep'
    if config and 'menus' in config:
        if key in config and config.get(key) != False:
            temp = config.get('menus')
            for i in temp:
                # 处理面包屑
                if 'models' in i:
                    for k in i.get('models'):
                        k['breadcrumbs'] = [{
                            'name': i.get('name'),
                            'icon': i.get('icon')
                        }, {
                            'name': k.get('name'),
                            'icon': k.get('icon')
                        }]
                else:
                    i['breadcrumbs'] = [{
                        'name': i.get('name'),
                        'icon': i.get('icon')
                    }]
                data.append(i)
        else:
            data = config.get('menus')

    # 获取侧边栏排序, 如果设置了就按照设置的内容排序, 留空则表示默认排序以及全部显示
    if config.get('menu_display') is not None:
        display_data = list()
        for _app in data:
            if _app['name'] not in config.get('menu_display'):
                continue
            _app['_weight'] = config.get('menu_display').index(_app['name'])
            display_data.append(_app)
        display_data.sort(key=lambda x: x['_weight'])
        data = display_data
    return '<script type="text/javascript">var menus={}</script>'.format(json.dumps(data, cls=LazyEncoder))


def get_icon(obj, name=None):
    temp = get_config_icon(name)
    if temp != '':
        return temp

    _dict = {
        'auth': 'fas fa-shield-alt',
        'User': 'far fa-user',
        'Group': 'fas fa-users-cog'
    }
    temp = _dict.get(obj)
    if not temp:
        _default = __get_config('SIMPLEUI_DEFAULT_ICON')
        if _default is None or _default:
            return 'far fa-file'
        else:
            return ''
    return temp


# 从配置中读取图标
def get_config_icon(name):
    _config_icon = __get_config('SIMPLEUI_ICON')
    if _config_icon is None:
        return ''

    if name in _config_icon:
        return _config_icon.get(name)
    else:
        return ''


@register.simple_tag(takes_context=True)
def load_message(context):
    messages = context.get('messages')
    array = [dict(msg=msg.message, tag=msg.tags) for msg in messages] if messages else []
    return '<script id="out_message" type="text/javascript">var messages={}</script>'.format(json.dumps(array, cls=LazyEncoder))


@register.simple_tag(takes_context=True)
def context_to_json(context):
    json_str = '{}'
    return mark_safe(json_str)


@register.simple_tag()
def get_language():
    return settings.LANGUAGE_CODE.lower()


@register.filter
def get_language_code(val):
    return settings.LANGUAGE_CODE.lower()


@register.simple_tag(takes_context=True)
def custom_button(context):
    admin = context.get('cl').model_admin
    data = {}
    actions = admin.get_actions(context.request)
    # if hasattr(admin, 'actions'):
    # actions = admin.actions
    # 输出自定义按钮的属性
    for name in actions:
        values = {}
        fun = actions.get(name)[0]
        for key, v in fun.__dict__.items():
            if key != '__len__' and key != '__wrapped__':
                values[key] = v
        data[name] = values
    return json.dumps(data, cls=LazyEncoder)


def get_model_fields(model, base=None):
    list = []
    fields = model._meta.fields
    for f in fields:
        label = f.name
        if hasattr(f, 'verbose_name'):
            label = getattr(f, 'verbose_name')

        if isinstance(label, Promise):
            label = str(label)

        if base:
            list.append(('{}__{}'.format(base, f.name), label))
        else:
            list.append((f.name, label))

    return list


@register.simple_tag(takes_context=True)
def search_placeholder(context):
    cl = context.get('cl')

    # 取消递归，只获取2级
    fields = get_model_fields(cl.model)

    for f in cl.model._meta.fields:
        if isinstance(f, ForeignKey):
            fields.extend(get_model_fields(f.related_model, f.name))

    verboses = []

    for s in cl.search_fields:
        for f in fields:
            if f[0] == s:
                verboses.append(f[1])
                break

    return ",".join(verboses)


def _import_reload(_modules):
    _obj = __import__(_modules, fromlist=_modules.split('.'))
    return _obj
