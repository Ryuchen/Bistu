#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ==================================================
# @Time : 2019-04-02 20:11 
# @Author : ryuchen
# @Site :  
# @File : urls.py 
# @Desc : 
# ==================================================
<<<<<<< HEAD
from django.conf.urls import url
from .views import MajorList, MajorDetail, AcademyList, AcademyDetail, ResearchList, ResearchDetail
=======
from django.urls import path, include

from .views import MajorList, MajorDetail, AcademyList, AcademyDetail, ResearchList, ResearchDetail, ClassList, ClassDetail
>>>>>>> 9f27577387a6752b6bc33d0280deb765b5689ec5
from .views import OpeningReportList, OpeningReportUpload
from .views import ReformList, ReformUpload
from .views import PaperList, PaperUpload

# Django REST framework URL patterns
urlpatterns = [
<<<<<<< HEAD
    url(r"^research/(?P<pk>[0-9a-z]{8}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{12})$", ResearchDetail.as_view(),
        name="research-detail"),
    url(r"^researches/$", ResearchList.as_view(), name="research-list"),
    url(r"^majors/$", MajorList.as_view(), name="major-list"),
    url(r"^major/(?P<pk>[0-9a-z]{8}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{12})$", MajorDetail.as_view(),
        name="major-detail"),
    url(r"^academies/$", AcademyList.as_view(), name="academy-list"),
    url(r"^academy/(?P<pk>[0-9a-z]{8}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{12})$", AcademyDetail.as_view(),
        name="academy-detail"),

    url(r"^opening_reports/$", OpeningReportList.as_view(), name="opening_report-list"),
    url(r"^opening_report_upload/$", OpeningReportUpload.as_view(), name="opening_report-upload"),

    url(r"^reforms/$", ReformList.as_view(), name="reform-list"),
    url(r"^reform_upload/$", ReformUpload.as_view(), name="reform-upload"),

    url(r"^papers/$", PaperList.as_view(), name="paper-list"),
    url(r"^paper_statistic/$", PaperUpload.as_view(), name="paper-statistic"),
=======
    # New REST URL patterns for new client website.
    path("academies/", AcademyList.as_view(), name="academies"),
    path("academy/", include([
        path("", AcademyDetail.as_view(), name="academy"),
        path("<uuid:pk>/", AcademyDetail.as_view(), name="academy-item"),
    ])),
    path("majors/", MajorList.as_view(), name="majors"),
    path("major/", include([
        path("", MajorDetail.as_view(), name="major"),
        path("<uuid:pk>/", MajorDetail.as_view(), name="major-item"),
    ])),
    path("researches/", ResearchList.as_view(), name="researches"),
    path("research/", include([
        path("", ResearchDetail.as_view(), name="research"),
        path("<uuid:pk>/", ResearchDetail.as_view(), name="research-item"),
    ])),
    path("classes/", ClassList.as_view(), name="classes"),
    path("class/", include([
        path("", ClassDetail.as_view(), name="class"),
        path("<uuid:pk>/", ClassDetail.as_view(), name="class-item"),
    ])),

    # TODO: need to review code.
    path("opening_reports/", OpeningReportList.as_view(), name="opening_report-list"),
    path("opening_report_upload/", OpeningReportUpload.as_view(), name="opening_report-upload"),
    path("reforms/", ReformList.as_view(), name="reform-list"),
    path("reform_upload/", ReformUpload.as_view(), name="reform-upload"),
    path("papers/", PaperList.as_view(), name="paper-list"),
    path("paper_statistic/", PaperUpload.as_view(), name="paper-statistic"),
>>>>>>> 9f27577387a6752b6bc33d0280deb765b5689ec5
]

app_name = 'api-colleges'
