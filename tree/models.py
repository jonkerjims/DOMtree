from django.db import models
from django.utils import timezone


class visitv(models.Model):
    times = models.CharField(default=6000,max_length=255)
    isclose = models.CharField(default=1,max_length=255)


class infor(models.Model):
    ip = models.CharField(default=6000,max_length=255)
    name= models.CharField(default=6000,max_length=255,db_collation='utf8_general_ci')
    address = models.CharField(default=6000, max_length=255)
    position = models.CharField(default=6000, max_length=255)
    visit_times = models.CharField(default=100,max_length=255)
    visit_time=models.DateTimeField(auto_now=True)
    islogin = models.IntegerField(default=0,max_length=1)

class music(models.Model):
    music = models.CharField(max_length=255)

