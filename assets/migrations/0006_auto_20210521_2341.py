# Generated by Django 3.2.3 on 2021-05-21 23:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('users', '0006_auto_20210521_1043'),
        ('assets', '0005_auto_20210520_1607'),
    ]

    operations = [
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mf_name', models.CharField(max_length=64, unique=True, verbose_name='厂商名称')),
                ('mf_telephone', models.CharField(blank=True, max_length=30, null=True, verbose_name='支持电话')),
            ],
            options={
                'verbose_name': '供应商',
                'verbose_name_plural': '供应商',
            },
        ),
        migrations.CreateModel(
            name='NetworkDevice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('net_name', models.CharField(max_length=50, verbose_name='设备名称')),
                ('net_type', models.SmallIntegerField(choices=[(0, '路由器'), (1, '交换机'), (2, '防火墙')], default=0,
                    verbose_name='网络设备类型')),
                ('net_vlan_ip', models.GenericIPAddressField(blank=True, null=True, verbose_name='VLanIP')),
                ('net_ip', models.GenericIPAddressField(blank=True, null=True, verbose_name='内网IP')),
                ('net_sn', models.CharField(max_length=50, null=True, verbose_name='SN号')),
                ('net_mac', models.CharField(blank=True, max_length=50, null=True, unique=True, verbose_name='MAC地址')),
                ('net_product_date', models.DateField(max_length=50, verbose_name='出厂日期')),
                ('net_confirmed_date', models.DateField(max_length=50, verbose_name='过保日期')),
                ('net_model', models.CharField(default='未知型号', max_length=128, verbose_name='网络设备型号')),
                ('net_firmware', models.CharField(blank=True, max_length=128, null=True, verbose_name='设备固件版本')),
                ('net_port_num', models.SmallIntegerField(blank=True, null=True, verbose_name='端口个数')),
                ('net_device_detail', models.TextField(blank=True, null=True, verbose_name='详细配置')),
                (
                    'net_status',
                    models.SmallIntegerField(choices=[(0, '上线'), (1, '下载')], default=0, verbose_name='设备状态')),
                ('net_ctime', models.DateField(auto_now_add=True, verbose_name='创建时间')),
                ('net_utime', models.DateField(auto_now=True, verbose_name='更新时间')),
                ('net_manufacturer',
                 models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL,
                     to='assets.manufacturer', verbose_name='制造商')),
            ],
            options={
                'verbose_name': '网络设备',
                'verbose_name_plural': '网络设备',
            },
        ),
        migrations.CreateModel(
            name='Printer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pr_name', models.CharField(max_length=50, verbose_name='设备名称')),
                ('pr_sn', models.CharField(max_length=50, null=True, verbose_name='SN号')),
                ('pr_ip', models.GenericIPAddressField(protocol='ipv4', unique=True, verbose_name='IP地址')),
                ('pr_mac', models.CharField(blank=True, max_length=50, null=True, verbose_name='MAC地址')),
                ('pr_type', models.CharField(max_length=50, verbose_name='打印机类型')),
                ('pr_model', models.CharField(max_length=50, verbose_name='打印机型号')),
                ('pr_product_date', models.DateField(max_length=50, verbose_name='出厂日期')),
                ('pr_confirmed_date', models.DateField(max_length=50, verbose_name='过保日期')),
                ('pr_department', models.CharField(max_length=50, verbose_name='部门')),
                ('pr_status',
                 models.SmallIntegerField(choices=[(0, '在线'), (1, '下线'), (2, '未知'), (3, '故障'), (4, '备用')], default=0,
                     verbose_name='设备状态')),
                ('pr_ctime', models.DateField(auto_now_add=True, verbose_name='创建时间')),
                ('pr_com_utime', models.DateField(auto_now=True, verbose_name='更新时间')),
                ('pr_address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL,
                    to='users.address', verbose_name='地区')),
                ('pr_manufacturer',
                 models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL,
                     to='assets.manufacturer', verbose_name='制造商')),
            ],
            options={
                'verbose_name': '打印机设备',
                'verbose_name_plural': '打印机设备',
            },
        ),
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ser_name', models.CharField(max_length=50, verbose_name='设备名称')),
                ('ser_tag', models.CharField(max_length=50, verbose_name='资产标签')),
                ('ser_ip', models.GenericIPAddressField(protocol='ipv4', unique=True, verbose_name='IP地址')),
                ('ser_mac', models.CharField(blank=True, max_length=50, null=True, unique=True, verbose_name='MAC地址')),
                ('ser_type',
                 models.SmallIntegerField(choices=[(0, '机架式服务器'), (1, '塔式服务器')], default=0, verbose_name='服务器类型')),
                ('ser_sn', models.CharField(max_length=50, null=True, verbose_name='SN号')),
                ('ser_model', models.CharField(blank=True, max_length=128, null=True, verbose_name='服务器型号')),
                ('ser_raid_type', models.CharField(blank=True, max_length=512, null=True, verbose_name='Raid类型')),
                ('ser_os_type',
                 models.SmallIntegerField(choices=[(0, 'Windows'), (1, 'Linux'), (2, 'Macintosh')], default=0,
                     verbose_name='操作系统')),
                ('ser_os_release', models.CharField(blank=True, max_length=64, null=True, verbose_name='操作系统版本')),
                ('ser_product_date', models.DateField(max_length=50, verbose_name='出厂日期')),
                ('ser_confirmed_date', models.DateField(max_length=50, verbose_name='过保日期')),
                (
                    'ser_status',
                    models.SmallIntegerField(choices=[(0, '上线'), (1, '下载')], default=0, verbose_name='设备状态')),
                ('ser_ctime', models.DateField(auto_now_add=True, verbose_name='创建时间')),
                ('ser_utime', models.DateField(auto_now=True, verbose_name='更新时间')),
                ('ser_manufacturer',
                 models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL,
                     to='assets.manufacturer', verbose_name='制造商')),
            ],
            options={
                'verbose_name': '服务器设备',
                'verbose_name_plural': '服务器设备',
            },
        ),
        migrations.RemoveField(
            model_name='computer',
            name='com_workplace',
        ),
        migrations.AddField(
            model_name='computer',
            name='com_address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL,
                to='users.address', verbose_name='地区'),
        ),
        migrations.AddField(
            model_name='computer',
            name='com_ip',
            field=models.GenericIPAddressField(blank=True, null=True, protocol='ipv4', unique=True,
                verbose_name='IP地址'),
        ),
        migrations.AddField(
            model_name='computer',
            name='com_os_release',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='操作系统版本'),
        ),
        migrations.AddField(
            model_name='computer',
            name='com_os_type',
            field=models.SmallIntegerField(choices=[(0, 'Windows'), (1, 'Linux'), (2, 'Macintosh')], default=0,
                verbose_name='操作系统'),
        ),
        migrations.AlterField(
            model_name='computer',
            name='com_department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL,
                to='users.department', verbose_name='部门'),
        ),
        migrations.AlterField(
            model_name='computer',
            name='com_manufacturer',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='制造商'),
        ),
        migrations.AlterField(
            model_name='sipphone',
            name='sip_manufacturer',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='制造商'),
        ),
        migrations.DeleteModel(
            name='Headset',
        ),
    ]
