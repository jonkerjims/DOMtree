# Generated by Django 4.0 on 2021-12-20 21:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tree', '0007_alter_infor_visit_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infor',
            name='visit_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]