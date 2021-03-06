# Generated by Django 4.0 on 2021-12-27 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='musicList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('localFile', models.CharField(db_collation='utf8_general_ci', max_length=255)),
                ('musicName', models.CharField(db_collation='utf8_general_ci', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='newyearRecords',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('origin_ID', models.CharField(max_length=255)),
                ('sender', models.CharField(db_collation='utf8_general_ci', default='陌生人', max_length=255)),
                ('addressee', models.CharField(db_collation='utf8_general_ci', default='心里人', max_length=255)),
                ('yourQQ', models.CharField(default='809341512', max_length=255)),
                ('TAQQ', models.CharField(default='809341512', max_length=255)),
                ('pic_name', models.CharField(default='None', max_length=255)),
                ('textarea', models.CharField(db_collation='utf8_general_ci', default='祝你有诗有歌有远方，有酒有肉有姑娘~', max_length=255)),
                ('creation_time', models.DateTimeField(auto_now=True)),
                ('musicID', models.IntegerField(default=0, max_length=10)),
            ],
        ),
    ]
