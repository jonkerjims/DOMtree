# -*- coding: utf-8 -*-

from django.urls import path, re_path

from NewYear import views

urlpatterns=[
    # re_path('^index/([\s\S]*)/([\s\S]*)/([\s\S]*)/$', views.showIndex,name='showIndex'),
    re_path('^index/([\s\S]*)/$', views.showIndex,name='showIndex'),
    path('share/',views.share,name='share')
]
