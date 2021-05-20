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
    com_sn = models.CharField(max_length=50, verbose_name="SN号", null=True)
    com_mac = models.CharField(max_length=50, verbose_name="MAC地址", null=True, blank=True)
    com_type = models.SmallIntegerField(choices=com_type_choice, default=0, verbose_name="电脑类型")
    com_model = models.CharField(max_length=50, verbose_name="电脑型号")
    com_workplace = models.CharField(max_length=50, verbose_name="职场")
    com_product_date = models.DateField(max_length=50, verbose_name="出厂日期")
    com_confirmed_date = models.DateField(max_length=50, verbose_name="过保日期")
    com_manufacturer = models.CharField(max_length=50, verbose_name="制造商", null=True, blank=True, default="联想")
    com_owner = models.ForeignKey('users.User', on_delete=models.SET_NULL, null=True, blank=True, verbose_name="使用人")
    com_department = models.CharField(max_length=50, verbose_name="部门")
    com_status = models.SmallIntegerField(choices=com_status_choice, default=0, verbose_name="设备状态")
    com_ctime = models.DateField(auto_now_add=True, verbose_name="创建时间")
    com_utime = models.DateField(auto_now=True, verbose_name="更新时间")


    class Meta:
        verbose_name = '电脑设备'
        verbose_name_plural = verbose_name


# IP话机
class SipPhone(models.Model):
    sip_status_choice = [
        (0, '使用'),
        (1, '闲置'),
        (2, '库存'),
        (3, '故障'),
        (4, '返修'),
    ]

    sip_workplace = models.CharField(max_length=50, verbose_name="职场")
    sip_model = models.CharField(max_length=50, verbose_name="话机型号")
    sip_mac = models.CharField(max_length=50, verbose_name="MAC地址", null=True, blank=True)
    sip_ip = models.GenericIPAddressField(max_length=50, protocol="ipv4", verbose_name="IP地址", unique=True)
    sip_account1 = models.PositiveBigIntegerField(verbose_name="账号1")
    sip_account2 = models.PositiveBigIntegerField(verbose_name="账号2")
    sip_manufacturer = models.CharField(max_length=200, verbose_name="制造商", null=True,
        blank=True, default='联地科技')
    sip_product_date = models.DateField(max_length=50, verbose_name="出厂日期", null=True, default='2020/6/15')
    sip_confirmed_date = models.DateField(max_length=50, verbose_name="过保日期", null=True)
    sip_status = models.SmallIntegerField(choices=sip_status_choice, default=0, verbose_name="话机状态")
    sip_ctime = models.DateField(auto_now_add=True, verbose_name="创建时间")
    sip_utime = models.DateField(auto_now=True, verbose_name="更新时间")

    class Meta:
        verbose_name = 'IP话机'
        verbose_name_plural = verbose_name


# 模拟话机
class Telephone(models.Model):
    sip_status_choice = [
        (0, '使用'),
        (1, '闲置'),
        (2, '库存'),
        (3, '故障'),
        (4, '返修'),
    ]

    tel_workplace = models.CharField(max_length=50, verbose_name="职场")
    tel_model = models.CharField(max_length=50, verbose_name="话机型号")
    tel_gateway = models.CharField(max_length=30, verbose_name="总机号码")
    tel_ext = models.IntegerField(verbose_name="分机号码")
    tel_user = models.ForeignKey('users.User', on_delete=models.SET_NULL, null=True, blank=True, verbose_name="使用人")
    tel_manufacturer = models.CharField(max_length=200, verbose_name="制造商", null=True, blank=True, default='摩托罗拉')
    tel_product_date = models.DateField(max_length=50, verbose_name="出厂日期", null=True, default='2020/6/15')
    tel_confirmed_date = models.DateField(max_length=50, verbose_name="过保日期", null=True)
    tel_status = models.SmallIntegerField(choices=sip_status_choice, default=0, verbose_name="话机状态")
    tel_ctime = models.DateField(auto_now_add=True, verbose_name="创建时间")
    tel_utime = models.DateField(auto_now=True, verbose_name="更新时间")

    class Meta:
        verbose_name = '模拟话机'
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
    hd_sn = models.CharField(max_length=50, verbose_name="耳机SN号")
    hd_workplace = models.CharField(max_length=50, verbose_name="职场")
    hd_product_date = models.DateField(max_length=50, verbose_name="出厂日期")
    hd_confirmed_date = models.DateField(max_length=50, verbose_name="过保日期")
    hd_user = models.ForeignKey('users.User', on_delete=models.SET_NULL, null=True, blank=True, verbose_name="使用人")
    hd_status = models.SmallIntegerField(choices=hd_status_choice, default=0, verbose_name="设备状态")
    hd_ctime = models.DateField(auto_now_add=True, verbose_name="创建时间")
    hd_utime = models.DateField(auto_now=True, verbose_name="更新时间")

    class Meta:
        verbose_name = '耳机设备'
        verbose_name_plural = verbose_name


# class Username(models.Model):
#     u_name = tel_user = models.ForeignKey('users.User', on_delete=models.SET_NULL, null=True, blank=True, verbose_name="话机型号")
#
#
#     class Meta:
#         verbose_name = '耳机设备'
#         verbose_name_plural = verbose_name
