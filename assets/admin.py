# Register your models here.
from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import Computer, Server, NetworkDevice, SipPhone, Telephone, Manufacturer, Printer


# 注册 Computer 模型
@admin.register(Computer)
class ComputerList(ImportExportModelAdmin):
    list_display = ['id', 'com_name', 'com_tag', 'com_type', 'com_model', 'com_sn', 'com_mac',
                    'com_os_type', 'com_os_release', 'com_address', 'com_department', 'com_owner',
                    'com_product_date',
                    'com_confirmed_date', 'com_manufacturer', 'com_status']  # 后台列表显示
    list_per_page = 50  # 每页显示的数量
    list_filter = ['com_name', 'com_tag', 'com_type', 'com_owner', 'com_status']  # 列表过滤
    ordering = ['id']  # 按创建时间排序
    list_editable = ['com_mac', 'com_department', 'com_owner', 'com_status', ]
    search_fields = ['com_name', 'com_tag', 'com_type', 'com_owner', 'com_status']  #


# Computer 导入导出
class ComputerResource(resources.ModelResource):
    class Meta:
        model = Computer
        export_order = ['id', 'com_name', 'com_tag', 'com_type', 'com_model', 'com_sn', 'com_mac',
                        'com_os_type', 'com_os_release', 'com_address', 'com_department', 'com_owner',
                        'com_product_date',
                        'com_confirmed_date', 'com_manufacturer', 'com_status']  # 导出的项目


# 注册 Printer 模型
@admin.register(Printer)
class PrinterList(ImportExportModelAdmin):
    list_display = ['id', 'pr_name', 'pr_sn', 'pr_ip', 'pr_mac', 'pr_type', 'pr_model',
                    'pr_product_date', 'pr_confirmed_date', 'pr_manufacturer', 'pr_address', 'pr_department',
                    'pr_status']  # 后台列表显示
    list_per_page = 50  # 每页显示的数量
    list_filter = ['pr_name', 'pr_ip', 'pr_manufacturer', 'pr_address', 'pr_department', 'pr_status']  # 列表过滤
    ordering = ['id']  # 按创建时间排序
    list_editable = ['pr_name', 'pr_ip', 'pr_department', 'pr_manufacturer', 'pr_status']
    search_fields = ['pr_name', 'pr_ip', 'pr_department', 'pr_manufacturer', 'pr_status']  #


# Printer 导入导出
class PrinterResource(resources.ModelResource):
    class Meta:
        model = Printer
        export_order = ['id', 'pr_name', 'pr_sn', 'pr_ip', 'pr_mac', 'pr_type', 'pr_model',
                        'pr_product_date', 'pr_confirmed_date', 'pr_manufacturer', 'pr_address', 'pr_department',
                        'pr_status']  # 导出的项目


# 注册 Server 模型
@admin.register(Server)
class ServerList(ImportExportModelAdmin):
    list_display = ['id', 'ser_name', 'ser_tag', 'ser_ip', 'ser_mac', 'ser_type', 'ser_sn', 'ser_model',
                    'ser_raid_type', 'ser_os_type', 'ser_os_release', 'ser_product_date',
                    'ser_confirmed_date', 'ser_manufacturer', 'ser_status']  # 后台列表显示
    list_per_page = 50  # 每页显示的数量
    list_filter = ['ser_name', 'ser_ip', 'ser_type', 'ser_model', 'ser_manufacturer', 'ser_status']  # 列表过滤
    ordering = ['id']  # 按创建时间排序
    list_editable = ['ser_ip', 'ser_model', 'ser_manufacturer', 'ser_status']
    search_fields = ['ser_ip', 'ser_model', 'ser_manufacturer', 'ser_status']  #


# Server 导入导出
class ServerResource(resources.ModelResource):
    class Meta:
        model = Computer
        export_order = ['id', 'ser_name', 'ser_tag', 'ser_ip', 'ser_mac', 'ser_type', 'ser_sn', 'ser_model',
                        'ser_raid_type', 'ser_os_type', 'ser_os_release', 'ser_product_date',
                        'ser_confirmed_date', 'ser_manufacturer', 'ser_status']  # 导出的项目


# 注册 Server 模型
@admin.register(NetworkDevice)
class NetworkDeviceList(ImportExportModelAdmin):
    list_display = ['id', 'net_name', 'net_type', 'net_vlan_ip', 'net_ip', 'net_sn', 'net_mac', 'net_model',
                    'net_firmware', 'net_port_num', 'net_device_detail', 'net_product_date',
                    'net_confirmed_date', 'net_manufacturer', 'net_status']  # 后台列表显示
    list_per_page = 50  # 每页显示的数量
    list_filter = ['net_name', 'net_type', 'net_vlan_ip', 'net_ip', 'net_model', 'net_port_num', 'net_manufacturer',
                   'net_status']  # 列表过滤
    ordering = ['id']  # 按创建时间排序
    list_editable = ['net_name', 'net_vlan_ip', 'net_ip', 'net_manufacturer',
                     'net_status']
    search_fields = ['net_name', 'net_vlan_ip', 'net_ip', 'net_manufacturer',
                     'net_status']  #


# Server 导入导出
class NetworkDeviceResource(resources.ModelResource):
    class Meta:
        model = NetworkDevice
        export_order = ['id', 'net_name', 'net_type', 'net_vlan_ip', 'net_ip', 'net_sn', 'net_mac', 'net_model',
                        'net_firmware', 'net_port_num', 'net_device_detail', 'net_product_date',
                        'net_confirmed_date', 'net_manufacturer', 'net_status']  # 导出的项目


# 注册SipPhone模型
@admin.register(SipPhone)
class SipPhoneList(ImportExportModelAdmin):
    list_display = ['id', 'sip_workplace', 'sip_model', 'sip_ip', 'sip_mac', 'sip_account1', 'sip_account2',
                    'sip_product_date', 'sip_confirmed_date', 'sip_manufacturer', 'sip_status', 'sip_ctime',
                    'sip_utime']  # 后台列表显示
    list_per_page = 50  # 每页显示的数量
    list_filter = ['sip_status', 'sip_account1', 'sip_account2']  # 列表过滤
    ordering = ['id']  # 按创建时间排序
    list_editable = ['sip_status', 'sip_account1', 'sip_account2', 'sip_confirmed_date']  # 可编辑项
    search_fields = ['sip_status', 'sip_account1', 'sip_account2']  # 可搜索项


# Headset 导入导出
class SipPhoneResource(resources.ModelResource):
    class Meta:
        model = SipPhone
        export_order = ['id', 'sip_workplace', 'sip_model', 'sip_ip', 'sip_sn', 'sip_account1', 'sip_account2',
                        'sip_product_date', 'sip_confirmed_date', 'sip_manufacturer', 'sip_status']  # 导出的项目


# 注册Telephone模型
@admin.register(Telephone)
class TelephoneList(ImportExportModelAdmin):
    list_display = ['id', 'tel_workplace', 'tel_model', 'tel_gateway', 'tel_ext', 'tel_user', 'tel_product_date',
                    'tel_confirmed_date', 'tel_manufacturer', 'tel_status', 'tel_ctime', 'tel_utime']  # 后台列表显示
    list_per_page = 50  # 每页显示的数量
    list_filter = ['tel_ext', 'tel_user', 'tel_status']  # 列表过滤
    ordering = ['id']  # 按创建时间排序
    list_editable = ['tel_ext', 'tel_user', 'tel_status']  # 可编辑项
    search_fields = ['tel_ext', 'tel_user', 'tel_status']  # 可搜索项


# Headset 导入导出
class TelephoneResource(resources.ModelResource):
    class Meta:
        model = Telephone
        export_order = ['id', 'tel_workplace', 'tel_model', 'tel_gateway', 'tel_ext', 'tel_user', 'tel_product_date',
                        'tel_confirmed_date', 'tel_manufacturer', 'tel_status', 'tel_ctime', 'tel_utime']  # 导出的项目


# 注册 Position 模块
@admin.register(Manufacturer)
class ManufacturerList(admin.ModelAdmin):
    list_display = ['id', 'mf_name', 'mf_telephone']  # 后台列表显示
    list_editable = ['mf_name']


admin.site.site_header = 'AMS资产管理系统'
admin.site.site_title = "AMS资产管理系统"
