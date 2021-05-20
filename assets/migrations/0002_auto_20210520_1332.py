# Generated by Django 3.2.3 on 2021-05-20 13:32

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20210520_1332'),
        ('assets', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SipPhone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sip_workplace', models.CharField(max_length=50, verbose_name='职场')),
                ('sip_model', models.CharField(max_length=50, verbose_name='话机型号')),
                ('sip_mac', models.CharField(blank=True, max_length=50, null=True, verbose_name='MAC地址')),
                ('sip_ip', models.GenericIPAddressField(protocol='ipv4', unique=True, verbose_name='IP地址')),
                ('sip_account1', models.PositiveBigIntegerField(verbose_name='账号1')),
                ('sip_account2', models.PositiveBigIntegerField(verbose_name='账号2')),
                ('sip_manufacturer',
                 models.CharField(blank=True, default='联地科技', max_length=200, null=True, verbose_name='制造商')),
                ('sip_product_date',
                 models.DateField(default='2020/6/15', max_length=50, null=True, verbose_name='出厂日期')),
                ('sip_confirmed_date', models.DateField(max_length=50, null=True, verbose_name='过保日期')),
                ('sip_status',
                 models.SmallIntegerField(choices=[(0, '使用'), (1, '闲置'), (2, '库存'), (3, '故障'), (4, '返修')], default=0,
                     verbose_name='话机状态')),
                ('sip_ctime', models.DateField(auto_now_add=True, verbose_name='创建时间')),
                ('sip_utime', models.DateField(auto_now=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': 'IP话机',
                'verbose_name_plural': 'IP话机',
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
            name='com_mac',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='MAC地址'),
        ),
        migrations.AddField(
            model_name='computer',
            name='com_manufacturer',
            field=models.CharField(blank=True, default='联想', max_length=50, null=True, verbose_name='制造商'),
        ),
        migrations.AddField(
            model_name='computer',
            name='com_sn',
            field=models.CharField(max_length=50, null=True, verbose_name='电脑SN号'),
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
        migrations.CreateModel(
            name='Telephone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tel_workplace', models.CharField(max_length=50, verbose_name='职场')),
                ('tel_model', models.CharField(max_length=50, verbose_name='话机型号')),
                ('tel_gateway', models.CharField(max_length=30, verbose_name='总机号码')),
                ('tel_ext', models.IntegerField(verbose_name='分机号码')),
                ('tel_manufacturer',
                 models.CharField(blank=True, default='摩托罗拉', max_length=200, null=True, verbose_name='制造商')),
                ('tel_product_date',
                 models.DateField(default='2020/6/15', max_length=50, null=True, verbose_name='出厂日期')),
                ('tel_confirmed_date', models.DateField(max_length=50, null=True, verbose_name='过保日期')),
                ('tel_status',
                 models.SmallIntegerField(choices=[(0, '使用'), (1, '闲置'), (2, '库存'), (3, '故障'), (4, '返修')], default=0,
                     verbose_name='话机状态')),
                ('tel_ctime', models.DateField(auto_now_add=True, verbose_name='创建时间')),
                ('tel_utime', models.DateField(auto_now=True, verbose_name='更新时间')),
                ('tel_user',
                 models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.user',
                     verbose_name='使用人')),
            ],
            options={
                'verbose_name': '模拟话机',
                'verbose_name_plural': '模拟话机',
            },
        ),
        migrations.CreateModel(
            name='Headset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hd_name', models.CharField(max_length=50, verbose_name='耳机名')),
                ('hd_model', models.CharField(max_length=50, verbose_name='耳机型号')),
                ('hd_sn', models.CharField(max_length=50, verbose_name='耳机SN号')),
                ('hd_workplace', models.CharField(max_length=50, verbose_name='职场')),
                ('hd_product_date', models.DateField(max_length=50, verbose_name='出厂日期')),
                ('hd_confirmed_date', models.DateField(max_length=50, verbose_name='过保日期')),
                ('hd_status', models.SmallIntegerField(choices=[(0, '使用'), (1, '库存'), (2, '故障'), (3, '返修')], default=0,
                    verbose_name='设备状态')),
                ('hd_ctime', models.DateField(auto_now_add=True, verbose_name='创建时间')),
                ('hd_utime', models.DateField(auto_now=True, verbose_name='更新时间')),
                ('hd_user',
                 models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.user',
                     verbose_name='使用人')),
            ],
            options={
                'verbose_name': '耳机设备',
                'verbose_name_plural': '耳机设备',
            },
        ),
    ]