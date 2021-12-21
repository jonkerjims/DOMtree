from django.utils import timezone

from tree import models


def infor(name,ip):
    query = models.infor.objects.filter(name=name).values('name')
    if list(query) != []:
        query_set = models.infor.objects.filter(name=name)
        times = int(query_set[0].visit_times) + 1
        time = timezone.now()
        models.infor.objects.filter(name=name).update(visit_times=times, visit_time=time)
    else:
        models.infor.objects.create(name=name, ip=ip, visit_times=100)