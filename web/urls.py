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
from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

urlpatterns = [
    path("accounts/", include("apps.accounts.urls")),
    path("colleges/", include("apps.colleges.urls")),
    path("teachers/", include("apps.teachers.urls")),
    path("students/", include("apps.students.urls")),
    path("settings/", include("apps.settings.urls")),
    path("reports/", include("apps.midcheckreports.urls")),
    path("thesis/", include("apps.thesis.urls")),
    path("statistic/", include("apps.statistic.urls")),
    path("admin/", admin.site.urls),
    path("client/", TemplateView.as_view(template_name="client/index.html")),
    path("history_data/", include("apps.history_data.urls")),
]

admin.sites.AdminSite.site_header = '研究生管理系统'
admin.sites.AdminSite.site_title = '研究生管理系统'
admin.sites.AdminSite.index_title = '研究生管理系统'
