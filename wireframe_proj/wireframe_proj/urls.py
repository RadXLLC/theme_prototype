"""wireframe_proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from mainpage.views import *
from studies.views import *
from cases.views import *
from teaching_files.views import *
from case_reports.views import *

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^studies/', studies_index),
    url(r'^cases/', cases_index),
    url(r'^teaching_files/edit', teaching_files_edit),
    url(r'^teaching_files/', teaching_files_index),
    url(r'^case_reports/edit', case_reports_edit),
    url(r'^case_reports/', case_reports_index),
    url(r'^$', main_page),

]
