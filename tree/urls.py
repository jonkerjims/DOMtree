from tree import views,infor
from django.urls import path, re_path

urlpatterns=[
    path('index/',views.index,name='index'),
    path('infor/',infor.infor,name='infor'),
    re_path("^index/([\s\S]*)/$", views.index),

]