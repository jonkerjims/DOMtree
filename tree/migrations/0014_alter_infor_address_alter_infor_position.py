# Generated by Django 4.0 on 2021-12-22 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tree', '0013_alter_infor_address_alter_infor_position'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infor',
            name='address',
            field=models.CharField(db_collation='utf8_general_ci', default=6000, max_length=255),
        ),
        migrations.AlterField(
            model_name='infor',
            name='position',
            field=models.CharField(db_collation='utf8_general_ci', default=6000, max_length=255),
        ),
    ]
