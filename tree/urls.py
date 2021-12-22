from tree import views,infor
from django.urls import path, re_path

urlpatterns=[
    path('vister_v/',views.vister_v,name='visitor volume'),
    path('DBA/',views.dba,name='dba'),
    path('isShare/',views.isShare,name='isShare'),
    path('share/',views.share,name='share'),
    re_path('^index/([\s\S]*)/$', views.index,name='index'),
]