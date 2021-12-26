import os
import threading

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from DOMtree.settings import BASE_DIR
from tree import models
from tree.IPsearch.IPsearch import IPsearch
from tree.infor import infor


def index(request,name):
    # print(name)
    # print(name.decode('utf-8'))
    #总访问数量
    value = models.visitv.objects.filter(id=1)
    music = models.music.objects.filter(id=1)[0].music
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
        'music':music
    }
    return render(request,'tree/index.html',context=data)


def vister_v(request):
    value = models.visitv.objects.filter(id=1)
    music = models.music.objects.filter(id=1)[0].music
    isclose = value[0].isclose
    times = value[0].times
    data = {
        'times':times,
        'isclose': isclose,
        'music':music
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
            inforObj = models.infor.objects.all().order_by('-visit_time')
            oldTimes = models.visitv.objects.filter(id=1)[0].oldtimes
            vv = models.visitv.objects.all()

            infor = inforObj[0:100]
            newUserCount = inforObj.count() - int(oldTimes)

            models.visitv.objects.filter(id=1).update(oldtimes=inforObj.count())
            # 读取music下的所有音乐
            path = os.path.join(BASE_DIR,'static/music')
            musicList = os.listdir(path)
            # 读取选中的音乐
            selectedMusic = models.music.objects.filter(id=1)[0].music
            data = {
                'infor':infor,
                'vv':vv,
                'musicList':musicList,
                'selectedMusic':selectedMusic,
                'newUser':newUserCount,
            }
            return render(request,'DBA/index.html',context=data)
        else:
            return render(request, 'DBA/login.html')


def updateMusic(request):
    if request.method == "GET":
        music = request.GET.get('opt_values')
        try:
            models.music.objects.filter(id=1).update(music=music)
            code = 200
        except:
            code = 400
        state = {
            'code': code,
        }
        return JsonResponse(data=state)


def uploadToMusic(request):
    data = 'error'
    try:
        if request.method == 'POST':
            newMusic = request.FILES.get('file', None)
            if newMusic:
                dir = os.path.join(os.path.join(BASE_DIR, 'static'), 'music')
                with open(os.path.join(dir, newMusic.name), 'wb+') as f:
                    for chunk in newMusic.chunks():
                        f.write(chunk)
                data = 'success'
        return HttpResponse(content=data)
    except:
        return HttpResponse(content=data)
