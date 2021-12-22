from django.utils import timezone

from tree import models
from tree.IPsearch.IPsearch import IPsearch


def infor(name,ip):
    # 定位
    try:
        add, pos = IPsearch(ip)
        # print(add, pos)
    except:
        add = '异常地址'
        pos = '无经纬度'
    query = models.infor.objects.filter(name=name).values('name')
    if list(query) != []:
        query_set = models.infor.objects.filter(name=name)
        times = int(query_set[0].visit_times) + 1
        time = timezone.now()
        models.infor.objects.filter(name=name).update(visit_times=times, visit_time=time,address=add,position=pos,islogin=1)
    else:
        models.infor.objects.create(name=name, ip=ip, visit_times=100,address=add,position=pos,islogin=1)

def dealData(infor,vv):
    data = {}
    return data