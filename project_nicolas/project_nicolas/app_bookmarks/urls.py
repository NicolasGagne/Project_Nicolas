
from rest_framework import routers
from project_nicolas.app_bookmarks import views

from django.conf.urls import url, include
from django.urls import path

app_name = 'appBookmarks'

router_app_bookmarks = routers.DefaultRouter()
router_app_bookmarks.register(r'users', views.UserViewSet, base_name='users')
router_app_bookmarks.register(r'bookmarks', views.ListCreateBookmarkViewSet, base_name='bookmarks')


appBookmarks_URL = include((router_app_bookmarks.urls, app_name), namespace='appBookmarks')
appBookmarks_URL[0].append(path(r'check_link/', views.check_link, name='check_link'))
appBookmarks_URL[0].append(path(r'clic_link/(?P<id>\d+)/$', views.clic_link, name='clic_link'))