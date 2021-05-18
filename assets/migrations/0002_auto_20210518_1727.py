# Generated by Django 3.2.3 on 2021-05-18 17:27

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('assets', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Headset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hd_name', models.CharField(max_length=50, verbose_name='耳机名')),
                ('hd_model', models.CharField(max_length=50, verbose_name='耳机型号')),
                ('hd_sn', models.CharField(max_length=50, verbose_name='耳机编号')),
                ('hd_workplace', models.CharField(max_length=50, verbose_name='职场')),
                ('hd_product_date', models.DateField(max_length=50, verbose_name='出厂日期')),
                ('hd_confirmed_date', models.DateField(max_length=50, verbose_name='过保日期')),
                ('hd_user', models.CharField(max_length=50, verbose_name='使用人')),
                ('hd_department', models.CharField(max_length=50, verbose_name='部门')),
                ('hd_status', models.SmallIntegerField(choices=[(0, '使用'), (1, '库存'), (2, '故障'), (3, '返修')], default=0,
                    verbose_name='设备状态')),
                ('hd_ctime', models.DateField(auto_now_add=True, verbose_name='创建时间')),
                ('hd_utime', models.DateField(auto_now=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '耳机设备',
                'verbose_name_plural': '耳机设备',
            },
        ),
        migrations.AddField(
            model_name='computer',
            name='com_ctime',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='创建时间'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='computer',
            name='com_sn',
            field=models.CharField(default=django.utils.timezone.now, max_length=50, verbose_name='资产编号'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='computer',
            name='com_utime',
            field=models.DateField(auto_now=True, verbose_name='更新时间'),
        ),
        migrations.AlterField(
            model_name='computer',
            name='com_department',
            field=models.CharField(max_length=50, verbose_name='部门'),
        ),
        migrations.AlterField(
            model_name='computer',
            name='com_model',
            field=models.CharField(max_length=50, verbose_name='电脑型号'),
        ),
        migrations.AlterField(
            model_name='computer',
            name='com_status',
            field=models.SmallIntegerField(choices=[(0, '使用'), (1, '闲置'), (2, '库存'), (3, '故障'), (4, '返修')], default=0,
                verbose_name='设备状态'),
        ),
        migrations.AlterField(
            model_name='computer',
            name='com_tag',
            field=models.CharField(max_length=50, verbose_name='资产标签'),
        ),
        migrations.AlterField(
            model_name='computer',
            name='com_type',
            field=models.SmallIntegerField(choices=[(0, '台式机'), (1, '笔记本')], default=0, verbose_name='电脑类型'),
        ),
    ]
