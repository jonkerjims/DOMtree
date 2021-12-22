import threading

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from tree import models
from tree.IPsearch.IPsearch import IPsearch
from tree.infor import infor


def index(request,name):
    # print(name)
    # print(name.decode('utf-8'))
    #总访问数量
    value = models.visitv.objects.filter(id=1)
    sumtimes = int(value[0].times) + 1
    models.visitv.objects.filter(id=1).update(times=sumtimes)
    # 设置session来标志是否处于登录状态
    # request.session[name] = 'login'

    #访问信息
    if request.META.get('HTTP_X_FORWARDED_FOR'):
        ip = request.META.get("HTTP_X_FORWARDED_FOR")
    else:
        ip = request.META.get("REMOTE_ADDR")
    # 开启线程
    t = threading.Thread(target=infor, args=(name,ip), name='saveMSG')
    t.start()

    data = {
        'name':name,
        'times':sumtimes,
    }
    return render(request,'tree/index.html',context=data)


def vister_v(request):
    value = models.visitv.objects.filter(id=1)
    isclose = value[0].isclose
    times = value[0].times
    data = {
        'times':times,
        'isclose': isclose,
    }
    # print(data)
    return JsonResponse(data=data)


def share(request):

    return render(request,'tree/share.html')


def isShare(request):
    if request.method == "GET":
        state = request.GET.get('state')
        try:
            models.visitv.objects.filter(id=1).update(isclose=state)
            code = 200
        except:
            code = 400
        state = {
            'code':code,
        }
        return JsonResponse(data=state)


def dba(request):
    if request.method == 'GET':
        return render(request,'DBA/login.html')
    if request.method == 'POST':
        password = request.POST.get('password')
        if password == '970619':
            infor = models.infor.objects.all()
            vv = models.visitv.objects.all()
            data = {
                'infor':infor,
                'vv':vv
            }
            return render(request,'DBA/index.html',context=data)
        else:
            return render(request, 'DBA/login.html')
