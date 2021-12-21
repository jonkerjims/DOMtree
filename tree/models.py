from django.db import models
from django.utils import timezone


class visitv(models.Model):
    times = models.CharField(default=6000,max_length=255)


class infor(models.Model):
    ip = models.CharField(default=6000,max_length=255)
    name= models.CharField(default=6000,max_length=255,db_collation='utf8_general_ci')
    visit_times = models.CharField(default=100,max_length=255)
    visit_time=models.DateTimeField(auto_now=True)
