# Register your models here.
from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import Computer, Headset, SipPhone, Telephone


# 注册 Computer 模块
@admin.register(Computer)
class ComputerList(ImportExportModelAdmin):
    list_display = ['id', 'com_workplace', 'com_name', 'com_tag', 'com_type', 'com_model', 'com_sn', 'com_mac',
                    'com_product_date',
                    'com_confirmed_date', 'com_owner', 'com_manufacturer', 'com_department', 'com_status']  # 后台列表显示
    list_per_page = 50  # 每页显示的数量
    list_filter = ['com_name', 'com_tag', 'com_type', 'com_owner', 'com_status']  # 列表过滤
    ordering = ['id']  # 按创建时间排序
    list_editable = ['com_mac', 'com_status', 'com_owner']
    search_fields = ['com_name', 'com_tag', 'com_type', 'com_owner', 'com_status']  #


# Computer 导入导出
class ComputerResource(resources.ModelResource):
    class Meta:

        model = Computer
        export_order = ['id', 'com_workplace', 'com_name', 'com_tag', 'com_type', 'com_model', 'com_sn',
                        'com_product_date', 'com_confirmed_date', 'com_owner', 'com_manufacturer', 'com_department',
                        'com_status']  # 导出的项目


# 注册SipPhone模块
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


# 注册Telephone模块
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


# 注册Headset模块
@admin.register(Headset)
class HeadsetList(ImportExportModelAdmin):
    list_display = ['id', 'hd_workplace', 'hd_name', 'hd_model', 'hd_sn', 'hd_product_date', 'hd_confirmed_date',
                    'hd_user', 'hd_status']  # 后台列表显示
    list_per_page = 50  # 每页显示的数量
    list_filter = ['hd_user', 'hd_status']  # 列表过滤
    ordering = ['id']  # 按创建时间排序
    list_editable = ['hd_user', 'hd_status']  # 可编辑项
    search_fields = ['hd_user', 'hd_status']


# Headset 导入导出
class HeadsetResource(resources.ModelResource):
    class Meta:
        model = Headset
        export_order = ['id', 'hd_workplace', 'hd_name', 'hd_model', 'hd_sn', ' hd_product_date', 'hd_confirmed_date',
                        'hd_user', 'hd_department', 'hd_status']  # 导出的项目


admin.site.site_header = 'AMS资产管理系统'
admin.site.site_title = "AMS资产管理系统"
