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
    com_os_type_choice = [
        (0, 'Windows'),
        (1, 'Linux'),
        (2, 'Macintosh'),
    ]
    com_name = models.CharField(max_length=50, verbose_name="计算机名")
    com_tag = models.CharField(max_length=50, verbose_name="资产标签")
    com_sn = models.CharField(max_length=50, verbose_name="SN号", null=True)
    com_ip = models.GenericIPAddressField(max_length=50, protocol="ipv4", verbose_name="IP地址", blank=True, null=True,
        unique=True)
    com_mac = models.CharField(max_length=50, verbose_name="MAC地址", null=True, blank=True)
    com_type = models.SmallIntegerField(choices=com_type_choice, default=0, verbose_name="电脑类型")
    com_model = models.CharField(max_length=50, verbose_name="电脑型号")
    com_product_date = models.DateField(max_length=50, verbose_name="出厂日期")
    com_confirmed_date = models.DateField(max_length=50, verbose_name="过保日期")
    com_os_type = models.SmallIntegerField(choices=com_os_type_choice, default=0, verbose_name="操作系统")
    com_os_release = models.CharField(max_length=64, blank=True, null=True, verbose_name='操作系统版本')
    com_manufacturer = models.CharField(max_length=50, verbose_name="制造商", null=True, blank=True)
    com_owner = models.ForeignKey('users.User', on_delete=models.SET_NULL, null=True, blank=True, verbose_name="使用人")
    com_department = models.ForeignKey('users.Department', on_delete=models.SET_NULL, null=True, blank=True,
        verbose_name="部门")
    com_address = models.ForeignKey('users.Address', on_delete=models.SET_NULL, null=True, blank=True,
        verbose_name="地区")
    com_status = models.SmallIntegerField(choices=com_status_choice, default=0, verbose_name="设备状态")
    com_ctime = models.DateField(auto_now_add=True, verbose_name="创建时间")
    com_utime = models.DateField(auto_now=True, verbose_name="更新时间")


    class Meta:
        verbose_name = '电脑设备'
        verbose_name_plural = verbose_name


# 打印机设备
class Printer(models.Model):
    pr_status_choice = [
        (0, '在线'),
        (1, '下线'),
        (2, '未知'),
        (3, '故障'),
        (4, '备用'),
    ]
    pr_name = models.CharField(max_length=50, verbose_name="设备名称")
    pr_sn = models.CharField(max_length=50, verbose_name="SN号", null=True)
    pr_ip = models.GenericIPAddressField(max_length=50, protocol="ipv4", verbose_name="IP地址", unique=True)
    pr_mac = models.CharField(max_length=50, verbose_name="MAC地址", null=True, blank=True)
    pr_type = models.CharField(max_length=50, verbose_name="打印机类型")
    pr_model = models.CharField(max_length=50, verbose_name="打印机型号")
    pr_product_date = models.DateField(max_length=50, verbose_name="出厂日期")
    pr_confirmed_date = models.DateField(max_length=50, verbose_name="过保日期")
    pr_manufacturer = models.ForeignKey('Manufacturer', models.SET_NULL, verbose_name="制造商", null=True, blank=True)
    pr_department = models.CharField(max_length=50, verbose_name="部门")
    pr_address = models.ForeignKey('users.Address', on_delete=models.SET_NULL, null=True, blank=True,
        verbose_name="地区")
    pr_status = models.SmallIntegerField(choices=pr_status_choice, default=0, verbose_name="设备状态")
    pr_ctime = models.DateField(auto_now_add=True, verbose_name="创建时间")
    pr_com_utime = models.DateField(auto_now=True, verbose_name="更新时间")

    class Meta:
        verbose_name = '打印机设备'
        verbose_name_plural = verbose_name


# 服务器设备
class Server(models.Model):
    ser_type_choice = [
        (0, '机架式服务器'),
        (1, '塔式服务器'),
    ]
    ser_status_choice = [
        (0, '上线'),
        (1, '下载'),
    ]
    ser_os_type_choice = [
        (0, 'Windows'),
        (1, 'Linux'),
        (2, 'Macintosh'),
    ]
    ser_name = models.CharField(max_length=50, verbose_name="设备名称")
    ser_tag = models.CharField(max_length=50, verbose_name="资产标签")
    ser_ip = models.GenericIPAddressField(max_length=50, protocol="ipv4", verbose_name="IP地址", unique=True)
    ser_mac = models.CharField(max_length=50, verbose_name="MAC地址", null=True, blank=True, unique=True)
    ser_type = models.SmallIntegerField(choices=ser_type_choice, default=0, verbose_name="服务器类型")
    ser_sn = models.CharField(max_length=50, verbose_name="SN号", null=True)
    ser_model = models.CharField(max_length=128, null=True, blank=True, verbose_name='服务器型号')
    ser_raid_type = models.CharField(max_length=512, blank=True, null=True, verbose_name='Raid类型')
    ser_os_type = models.SmallIntegerField(choices=ser_os_type_choice, default=0, verbose_name="操作系统")
    ser_os_release = models.CharField(max_length=64, blank=True, null=True, verbose_name='操作系统版本')
    ser_product_date = models.DateField(max_length=50, verbose_name="出厂日期")
    ser_confirmed_date = models.DateField(max_length=50, verbose_name="过保日期")
    ser_manufacturer = models.ForeignKey('Manufacturer', models.SET_NULL, verbose_name="制造商", null=True, blank=True)
    ser_status = models.SmallIntegerField(choices=ser_status_choice, default=0, verbose_name="设备状态")
    ser_ctime = models.DateField(auto_now_add=True, verbose_name="创建时间")
    ser_utime = models.DateField(auto_now=True, verbose_name="更新时间")

    def __str__(self):
        return '%s--%s--%s <sn:%s>' % (self.ser_name, self.get_ser_type_display(), self.ser_model, self.ser_sn)

    class Meta:
        verbose_name = '服务器设备'
        verbose_name_plural = "服务器设备"


# 网络设备
class NetworkDevice(models.Model):
    net_type_choice = [
        (0, '路由器'),
        (1, '交换机'),
        (2, '防火墙'),
    ]
    net_status_choice = [
        (0, '上线'),
        (1, '下载'),
    ]
    net_name = models.CharField(max_length=50, verbose_name="设备名称")
    net_type = models.SmallIntegerField(choices=net_type_choice, default=0, verbose_name="网络设备类型")
    net_vlan_ip = models.GenericIPAddressField(blank=True, null=True, verbose_name="VLanIP")
    net_ip = models.GenericIPAddressField(blank=True, null=True, verbose_name="内网IP")
    net_sn = models.CharField(max_length=50, verbose_name="SN号", null=True)
    net_mac = models.CharField(max_length=50, verbose_name="MAC地址", null=True, blank=True, unique=True)
    net_manufacturer = models.ForeignKey('Manufacturer', models.SET_NULL, verbose_name="制造商", null=True, blank=True)
    net_product_date = models.DateField(max_length=50, verbose_name="出厂日期")
    net_confirmed_date = models.DateField(max_length=50, verbose_name="过保日期")
    net_model = models.CharField(max_length=128, default='未知型号', verbose_name="网络设备型号")
    net_firmware = models.CharField(max_length=128, blank=True, null=True, verbose_name="设备固件版本")
    net_port_num = models.SmallIntegerField(null=True, blank=True, verbose_name="端口个数")
    net_device_detail = models.TextField(null=True, blank=True, verbose_name="详细配置")
    net_status = models.SmallIntegerField(choices=net_status_choice, default=0, verbose_name="设备状态")
    net_ctime = models.DateField(auto_now_add=True, verbose_name="创建时间")
    net_utime = models.DateField(auto_now=True, verbose_name="更新时间")

    def __str__(self):
        return '%s--%s--%s <sn:%s>' % (self.net_name, self.get_net_type_display(), self.net_model, self.net_sn)

    class Meta:
        verbose_name = '网络设备'
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
        blank=True)
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


# 供应商
class Manufacturer(models.Model):
    mf_name = models.CharField('厂商名称', max_length=64, unique=True)
    mf_telephone = models.CharField('支持电话', max_length=30, blank=True, null=True)

    def __str__(self):
        return self.mf_name

    class Meta:
        verbose_name = '供应商'
        verbose_name_plural = verbose_name
