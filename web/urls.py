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

urlpatterns = [
<<<<<<< Updated upstream
    path("", admin.site.urls),
    path("accounts/", include("apps.accounts.urls")),
=======
    path('', lambda request: redirect('client/', permanent=True)),
<<<<<<< HEAD

    path("settings/", include(("apps.settings.urls", "settings"), namespace="settings")),
    path("accounts/", include(("apps.accounts.urls", "accounts"), namespace="accounts")),
>>>>>>> Stashed changes
    path("colleges/", include("apps.colleges.urls")),
=======
    path("settings/", include("apps.settings.urls", namespace="api-settings")),
    path("accounts/", include("apps.accounts.urls", namespace="accounts")),
    path("colleges/", include("apps.colleges.urls", namespace="api-colleges")),
>>>>>>> 9f27577387a6752b6bc33d0280deb765b5689ec5
    path("teachers/", include("apps.teachers.urls")),
    path("students/", include("apps.students.urls")),
    path("settings/", include("apps.settings.urls")),
    path("reports/", include("apps.midcheckreports.urls")),
    path("thesis/", include("apps.thesis.urls")),
    path("statistic/", include("apps.statistic.urls")),
    path("history_data/", include("apps.history_data.urls")),
<<<<<<< HEAD
]

<<<<<<< Updated upstream
=======
# dashboard's router
urlpatterns += [
    url(r"^dashboard/$", views.dashboard, name="dashboard"),
]

=======
]

# dashboard's router
urlpatterns += [
    url(r"^dashboard/$", views.dashboard, name="dashboard"),
]
>>>>>>> 9f27577387a6752b6bc33d0280deb765b5689ec5

# server's router
urlpatterns += [
    path("server/", admin.site.urls),
]

# client's router
urlpatterns += [
<<<<<<< HEAD
    path("client/", views.index, name="index")
=======
    path("client/", views.index, name="index"),
    path("client/colleges/", include("apps.colleges.routers", namespace="colleges"))
>>>>>>> 9f27577387a6752b6bc33d0280deb765b5689ec5
]

>>>>>>> Stashed changes
admin.sites.AdminSite.site_header = '研究生管理系统'
admin.sites.AdminSite.site_title = '研究生管理系统'
admin.sites.AdminSite.index_title = '北京信息科技大学'
