"""Bookmarks URL Configuration

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
from django.urls import path
from django.conf.urls import url, include
from project_nicolas import views
from project_nicolas.app_bookmarks.urls import appBookmarks_URL


urlpatterns = [
    path('', views.bare),
    path('index/', views.index, name='index'),
    path('appBookmarks/admin/', admin.site.urls, name='admin_user'),
    url(r'appBookmarks/$', views.AppBookmarks_root, name='Bookmarks_root'),
    url(r'appBookmarks/',appBookmarks_URL),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
