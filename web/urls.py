"""web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import include, path
from . import views

# API's router
urlpatterns = [
    path('', lambda request: redirect('client/', permanent=True)),

    path("settings/", include(("apps.settings.urls", "settings"), namespace="settings")),
    path("accounts/", include(("apps.accounts.urls", "accounts"), namespace="accounts")),
    path("colleges/", include("apps.colleges.urls")),
    path("teachers/", include("apps.teachers.urls")),
    path("students/", include("apps.students.urls")),
    path("reports/", include("apps.midcheckreports.urls")),
    path("thesis/", include("apps.thesis.urls")),
    path("statistic/", include("apps.statistic.urls")),
    path("history_data/", include("apps.history_data.urls")),
]

# dashboard's router
urlpatterns += [
    url(r"^dashboard/$", views.dashboard, name="dashboard"),
]


# server's router
urlpatterns += [
    path("server/", admin.site.urls),
]

# client's router
urlpatterns += [
    path("client/", views.index, name="index")
]

admin.sites.AdminSite.site_header = '研究生管理系统'
admin.sites.AdminSite.site_title = '研究生管理系统'
admin.sites.AdminSite.index_title = '研究生管理系统'
