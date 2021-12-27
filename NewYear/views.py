import os
import time

from django.shortcuts import render

# Create your views here.
from DOMtree.settings import BASE_DIR
from NewYear import models


def showIndex(request,ID):
    querySet = models.newyearRecords.objects.filter(origin_ID=ID)
    sender = querySet[0].sender
    addressee = querySet[0].addressee
    yourQQ = querySet[0].yourQQ
    TAQQ = querySet[0].TAQQ
    textarea = querySet[0].textarea
    musicID = querySet[0].musicID
    musicSrc = models.musicList.objects.filter(id=musicID)[0].localFile
    if sender == '' or sender == None:
        sender = '陌生人'
    if addressee == '' or addressee == None:
        addressee = '心里人'
    if yourQQ == '' or yourQQ == None:
        yourQQ = '809341512'
    if TAQQ == '' or TAQQ == None:
        TAQQ = '809341512'
    if textarea == '' or textarea == None:
        textarea = '祝你有诗有歌有远方，有酒有肉有姑娘~'
    data = {
        'sender':sender,
        'addressee':addressee,
        'yourQQ':yourQQ,
        'TAQQ':TAQQ,
        'textarea':textarea,
        'musicSrc':musicSrc,
    }
    print(sender,addressee,yourQQ,TAQQ,textarea,musicID)
    return render(request,'NewYear/index.html',context=data)


def share(request):
    if request.method == 'GET':
        context = {}
        data = []
        query_set = models.musicList.objects.all().order_by('id')
        for line in query_set:
            li = {}
            li['id']=line.id
            li['musicName']=line.musicName
            data.append(li)
        context = {
            'data':data,
        }
        print(context)
        return render(request,'NewYear/share.html',context=context)

    if request.method == 'POST':
        sender = request.POST.get('sender')
        addressee = request.POST.get('addressee')
        yourQQ = request.POST.get('yourQQ')
        TAQQ = request.POST.get('TAQQ')
        picture = request.FILES.get('fileName')
        textarea = request.POST.get('textarea')
        musicID = request.POST.get('music')
        origin_ID = str(int(round(time.time() * 1000)))
        fileName = str(int(round(time.time() * 1000))) + '.jpg'
        try:
            if picture:
                fileName = str(int(round(time.time() * 1000))) + '.jpg'
                dir = os.path.join(os.path.join(os.path.join(BASE_DIR, 'static'), 'NewYearStatic'), 'userUpload')
                with open(os.path.join(dir, fileName), 'wb+') as f:
                    for chunk in picture.chunks():
                        f.write(chunk)
                print('文件上传成功')
        except:
            fileName = None

        models.newyearRecords.objects.create(
            origin_ID=origin_ID,
            sender=sender,
            addressee=addressee,
            yourQQ=yourQQ,
            TAQQ=TAQQ,
            pic_name=fileName,
            textarea=textarea,
            musicID=musicID
        )
        if addressee=='' or addressee == None:
            addressee = '意中人'
        data = {
            'ID':origin_ID,
            'addressee':addressee,
        }
        return render(request,'NewYear/shareSucc.html',context=data)