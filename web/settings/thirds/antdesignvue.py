#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ==================================================
# @Time : 2019-08-04 00:40
# @Author : ryuchen
# @File : antdesignvue.py
# @Desc :
# ==================================================

from django.conf import settings

STATICFILES_DIR = "web"

# Common Settings
GITHUB_URL = "https://github.com/ryuchen"

# Global Header Settings
ANT_DESIGN_VUE_HEADER_LOGOMINI = settings.STATIC_URL + STATICFILES_DIR + "/img/logo-mini.png"
ANT_DESIGN_VUE_HEADER_LOGOFULL = settings.STATIC_URL + STATICFILES_DIR + "/img/logo-full.png"

# #Header Toolbox Settings
# Enable lock screen function ？
ANT_DESIGN_VUE_HEADER_TOOLBOX_LOCK = True
# Enable author github function ？
ANT_DESIGN_VUE_HEADER_TOOLBOX_GITHUB = True
# Enable haystack function ？ (django-haystack global search function)
ANT_DESIGN_VUE_HEADER_TOOLBOX_SEARCH = True
# Enable notice function ?
ANT_DESIGN_VUE_HEADER_TOOLBOX_NOTICE = True
# Enable utility function ?
ANT_DESIGN_VUE_HEADER_TOOLBOX_UTILITY = True
# Enable setting function ?
ANT_DESIGN_VUE_HEADER_TOOLBOX_SETTING = True

# #Footer Copyright Settings
ANT_DESIGN_VUE_FOOTER_COPYRIGHT_YEAR = 2019
ANT_DESIGN_VUE_FOOTER_COPYRIGHT_AUTHOR = 'Ryuchen'
ANT_DESIGN_VUE_FOOTER_COPYRIGHT_LINK = "https://github.com/ryuchen"

# Global NavMenu Settings
# NavMenu items
ANT_DESIGN_VUE_NAV_MENUS = [
    {
        'app': 'auth',
        'name': '账户管理',
        'icon': 'pie-chart',
        'models': [
            {
                'name': '用户',
                'icon': 'pie-chart',
                'url': 'auth/user/'
            },
            {
                'name': '用户组',
                'icon': 'pie-chart',
                'url': 'auth/group/'
            }
        ]
    },
    {
        'app': 'accounts',
        'name': '学生管理',
        'icon': 'pie-chart',
        'url': 'accounts/student/'
    },
    {
        'app': 'accounts',
        'name': '教师管理',
        'icon': 'pie-chart',
        'url': 'accounts/tutor/'
    },
    {
        'app': 'colleges',
        'name': '学院管理',
        'icon': 'pie-chart',
        'models': [
            {
                'name': '学院',
                'icon': 'pie-chart',
                'url': 'colleges/academy/'
            },
            {
                'name': '专业',
                'icon': 'pie-chart',
                'url': 'colleges/major/'
            },
            {
                'name': '班级',
                'icon': 'pie-chart',
                'url': 'colleges/class/'
            },
            {
                'name': '教改',
                'icon': 'pie-chart',
                'url': 'colleges/reform/'
            },
            {
                'name': '统计',
                'icon': 'pie-chart',
                'url': 'colleges/reformresults/'
            }
        ]
    },
    {
        'app': 'education',
        'name': '教学管理',
        'icon': 'pie-chart',
        'models': [
            {
                'name': '论文',
                'icon': 'pie-chart',
                'url': 'education/thesis/'
            },
            {
                'name': '论文查重',
                'icon': 'pie-chart',
                'url': 'education/thesisplacheck/'
            },
            {
                'name': '论文盲审',
                'icon': 'pie-chart',
                'url': 'education/thesisblindreview/'
            },
        ]
    }
]
# Enable read menus config every time ?
ANT_DESIGN_VUE_NAV_MENUS_DYNAMIC = True

# Home Page Settings
# Home Page Display Type (Choice One of "Workplace | Overview | Customize")
ANT_DESIGN_VUE_HOME_TYPE = "Workplace"
# Title of home page if type = Customize
ANT_DESIGN_VUE_HOME_TITLE = "CSDN"
# Url of home page if type = Customize
ANT_DESIGN_VUE_HOME_URL = "https://blog.csdn.net/lyn1772671980/article/details/82217904"


