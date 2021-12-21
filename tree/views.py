
from django.shortcuts import render
import urllib

from django.utils import timezone

from tree import models
from tree.IPsearch.IPsearch import IPsearch
from tree.infor import infor


def index(request,name):
    #总访问数量
    value = models.visitv.objects.filter(id=1)
    sumtimes = int(value[0].times) + 1
    models.visitv.objects.filter(id=1).update(times=sumtimes)

    #访问信息
    if request.META.get('HTTP_X_FORWARDED_FOR'):
        ip = request.META.get("HTTP_X_FORWARDED_FOR")
    else:
        ip = request.META.get("REMOTE_ADDR")

    print("ip : ", ip)
    print(name)

    infor(name,ip)  #储存并更新信息
    #定位
    try:
        add, pos = IPsearch(ip)
        print(add, pos)
    except:
        print('局域网访问')
    return render(request,'tree/index.html',{'name':name} )