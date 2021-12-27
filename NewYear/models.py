from django.db import models

# Create your models here.


class newyearRecords(models.Model):
    origin_ID = models.CharField(max_length=255)
    sender= models.CharField(default='陌生人',max_length=255,db_collation='utf8_general_ci')
    addressee= models.CharField(default='心里人',max_length=255,db_collation='utf8_general_ci')
    yourQQ = models.CharField(default='809341512', max_length=255)
    TAQQ = models.CharField(default='809341512', max_length=255)
    pic_name = models.CharField(default='None',max_length=255)
    textarea = models.CharField(default='祝你有诗有歌有远方，有酒有肉有姑娘~',max_length=255,db_collation='utf8_general_ci')
    creation_time=models.DateTimeField(auto_now=True)
    musicID = models.IntegerField(default=0,max_length=10)


class musicList(models.Model):
    localFile = models.CharField(max_length=255,db_collation='utf8_general_ci')
    musicName = models.CharField(max_length=255,db_collation='utf8_general_ci')
