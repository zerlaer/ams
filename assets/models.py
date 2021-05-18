from django.db import models


# 电脑设备
class Computer(models.Model):
    com_type_choice = [
        (0, '台式机'),
        (1, '笔记本'),
    ]
    com_status_choice = [
        (0, '使用'),
        (1, '闲置'),
        (2, '库存'),
        (3, '故障'),
        (4, '返修'),
    ]

    com_name = models.CharField(max_length=50, verbose_name="计算机名")
    com_tag = models.CharField(max_length=50, verbose_name="资产标签")
    com_sn = models.CharField(max_length=50, verbose_name="资产编号")
    com_type = models.SmallIntegerField(choices=com_type_choice, default=0, verbose_name="电脑类型")
    com_model = models.CharField(max_length=50, verbose_name="电脑型号")
    com_workplace = models.CharField(max_length=50, verbose_name="职场")
    com_product_date = models.DateField(max_length=50, verbose_name="出厂日期")
    com_confirmed_date = models.DateField(max_length=50, verbose_name="过保日期")
    com_owner = models.CharField(max_length=50, verbose_name="资产接收人")
    com_department = models.CharField(max_length=50, verbose_name="部门")
    com_status = models.SmallIntegerField(choices=com_status_choice, default=0, verbose_name="设备状态")
    com_ctime = models.DateField("创建时间", auto_now_add=True)
    com_utime = models.DateField(auto_now=True, verbose_name="更新时间")

    class Meta:
        verbose_name = '电脑设备'
        verbose_name_plural = verbose_name


# 耳机设备
class Headset(models.Model):
    hd_status_choice = [
        (0, '使用'),
        (1, '库存'),
        (2, '故障'),
        (3, '返修'),
    ]
    hd_name = models.CharField(max_length=50, verbose_name="耳机名")
    hd_model = models.CharField(max_length=50, verbose_name="耳机型号")
    hd_sn = models.CharField(max_length=50, verbose_name="耳机编号")
    hd_workplace = models.CharField(max_length=50, verbose_name="职场")
    hd_product_date = models.DateField(max_length=50, verbose_name="出厂日期")
    hd_confirmed_date = models.DateField(max_length=50, verbose_name="过保日期")
    hd_user = models.CharField(max_length=50, verbose_name="使用人")
    hd_department = models.CharField(max_length=50, verbose_name="部门")
    hd_status = models.SmallIntegerField(choices=hd_status_choice, default=0, verbose_name="设备状态")
    hd_ctime = models.DateField(auto_now_add=True, verbose_name="创建时间", )
    hd_utime = models.DateField(auto_now=True, verbose_name="更新时间")

    class Meta:
        verbose_name = '耳机设备'
        verbose_name_plural = verbose_name
