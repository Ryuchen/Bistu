#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ==================================================
# @Time : 2019-07-29 15:07
# @Author : ryuchen
# @File : simpleui.py
# @Desc :
# ==================================================

# SimpleUI settings
# https://github.com/newpanjing/simpleui/blob/master/QUICK.md
SIMPLEUI_STATIC_OFFLINE = True
SIMPLEUI_FAVICON_ICON = "/static/bistu/img/logo.png"
SIMPLEUI_LOGIN_LOGO = "/static/bistu/img/caiselogo.png"
SIMPLEUI_INDEX_LOGO = "/static/bistu/img/logo.png"
SIMPLEUI_LOGO = "/static/bistu/img/logo.png"
SIMPLEUI_CONFIG = {
    'system_keep': False,
    'menus': [
        {
            'app': 'auth',
            'name': '账户管理',
            'icon': 'fas fa-user-shield',
            'models': [
                {
                    'name': '用户',
                    'icon': 'fa fa-user',
                    'url': 'auth/user/'
                },
                {
                    'name': '用户组',
                    'icon': 'fa fa-users-cog',
                    'url': 'auth/group/'
                }
            ]
        },
        {
            'app': 'accounts',
            'name': '学生管理',
            'icon': 'fa fa-graduation-cap',
            'url': 'accounts/student/'
        },
        {
            'app': 'accounts',
            'name': '教师管理',
            'icon': 'fa fa-id-card',
            'url': 'accounts/tutor/'
        },
        {
            'app': 'colleges',
            'name': '学院管理',
            'icon': 'fa fa-university',
            'models': [
                {
                    'name': '学院',
                    'icon': 'fa fa-university',
                    'url': 'colleges/academy/'
                },
                {
                    'name': '专业',
                    'icon': 'fa fa-university',
                    'url': 'colleges/major/'
                },
                {
                    'name': '班级',
                    'icon': 'fa fa-university',
                    'url': 'colleges/class/'
                },
                {
                    'name': '教改',
                    'icon': 'fa fa-university',
                    'url': 'colleges/reform/'
                },
                {
                    'name': '统计',
                    'icon': 'fa fa-university',
                    'url': 'colleges/reformresults/'
                }
            ]
        },
        {
            'app': 'education',
            'name': '教学管理',
            'icon': 'fas fa-book',
            'models': [
                {
                    'name': '论文',
                    'icon': 'fa fa-book',
                    'url': 'education/thesis/'
                },
                {
                    'name': '论文查重',
                    'icon': 'fa fa-book',
                    'url': 'education/thesisplacheck/'
                },
                {
                    'name': '论文盲审',
                    'icon': 'fa fa-book',
                    'url': 'education/thesisblindreview/'
                },
            ]
        }
    ]
}
