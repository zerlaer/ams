# Generated by Django 3.2.3 on 2021-05-20 15:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('users', '0003_auto_20210520_1448'),
        ('assets', '0003_alter_computer_com_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='computer',
            name='com_confirmed_date',
            field=models.DateField(db_column='过保日期', max_length=50, verbose_name='过保日期'),
        ),
        migrations.AlterField(
            model_name='computer',
            name='com_ctime',
            field=models.DateField(auto_now_add=True, db_column='创建时间', verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='computer',
            name='com_department',
            field=models.CharField(db_column='部门', max_length=50, verbose_name='部门'),
        ),
        migrations.AlterField(
            model_name='computer',
            name='com_mac',
            field=models.CharField(blank=True, db_column='MAC地址', max_length=50, null=True, verbose_name='MAC地址'),
        ),
        migrations.AlterField(
            model_name='computer',
            name='com_manufacturer',
            field=models.CharField(blank=True, db_column='制造商', default='联想', max_length=50, null=True,
                verbose_name='制造商'),
        ),
        migrations.AlterField(
            model_name='computer',
            name='com_model',
            field=models.CharField(db_column='电脑型号', max_length=50, verbose_name='电脑型号'),
        ),
        migrations.AlterField(
            model_name='computer',
            name='com_name',
            field=models.CharField(db_column='计算机名', max_length=50, verbose_name='计算机名'),
        ),
        migrations.AlterField(
            model_name='computer',
            name='com_owner',
            field=models.ForeignKey(blank=True, db_column='使用人', null=True,
                on_delete=django.db.models.deletion.SET_NULL, to='users.user', verbose_name='使用人'),
        ),
        migrations.AlterField(
            model_name='computer',
            name='com_product_date',
            field=models.DateField(db_column='出厂日期', max_length=50, verbose_name='出厂日期'),
        ),
        migrations.AlterField(
            model_name='computer',
            name='com_sn',
            field=models.CharField(db_column='SN号', max_length=50, null=True, verbose_name='SN号'),
        ),
        migrations.AlterField(
            model_name='computer',
            name='com_status',
            field=models.SmallIntegerField(choices=[(0, '使用'), (1, '闲置'), (2, '库存'), (3, '故障'), (4, '返修')],
                db_column='设备状态', default=0, verbose_name='设备状态'),
        ),
        migrations.AlterField(
            model_name='computer',
            name='com_tag',
            field=models.CharField(db_column='资产标签', max_length=50, verbose_name='资产标签'),
        ),
        migrations.AlterField(
            model_name='computer',
            name='com_type',
            field=models.SmallIntegerField(choices=[(0, '台式机'), (1, '笔记本')], db_column='电脑类型', default=0,
                verbose_name='电脑类型'),
        ),
        migrations.AlterField(
            model_name='computer',
            name='com_utime',
            field=models.DateField(auto_now=True, db_column='更新时间', verbose_name='更新时间'),
        ),
        migrations.AlterField(
            model_name='computer',
            name='com_workplace',
            field=models.CharField(db_column='职场', max_length=50, verbose_name='职场'),
        ),
    ]
