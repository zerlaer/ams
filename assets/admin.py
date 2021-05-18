# Register your models here.
from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import Computer, Headset


# 注册 Computer 模块
@admin.register(Computer)
class ComputerList(ImportExportModelAdmin):
    list_display = [
        'id', 'com_workplace', 'com_name', 'com_tag', 'com_type', 'com_model', 'com_sn', 'com_product_date',
        'com_confirmed_date', 'com_owner', 'com_department', 'com_status']  # 列表显示的
    list_per_page = 50  # 每页显示的数量
    list_filter = ['com_name', 'com_tag', 'com_type', 'com_owner', 'com_status']  # 列表过滤
    ordering = ('com_ctime',)  # 按创建时间排序
    list_editable = ['com_status']


# Computer 导入导出
class ComputerResource(resources.ModelResource):
    class Meta:
        model = Computer
        export_order = [
            'id', 'com_workplace', 'com_name', 'com_tag', 'com_type', 'com_model', 'com_sn', 'com_product_date',
            'com_confirmed_date', 'com_owner', 'com_department', 'com_status', 'com_ctime']  # 导出的项目


# 注册Headset模块
@admin.register(Headset)
class HeadsetList(ImportExportModelAdmin):
    list_display = ['id', 'hd_workplace', 'hd_name', 'hd_model', 'hd_sn', 'hd_product_date', 'hd_confirmed_date',
                    'hd_user', 'hd_department', 'hd_status', 'hd_ctime']  # 列表显示
    list_per_page = 50  # 每页显示的数量
    list_filter = ['hd_user', 'hd_department', 'hd_status']  # 列表过滤
    ordering = ('hd_ctime',)  # 按创建时间排序
    list_editable = ['hd_user', 'hd_status']  # 可编辑项


# Computer 导入导出
class HeadsetResource(resources.ModelResource):
    class Meta:
        model = Headset
        export_order = ['id', ' hd_workplace', 'hd_name', 'hd_model', 'hd_sn', ' hd_product_date', 'hd_confirmed_date',
                        'hd_user', 'hd_department', 'hd_status', 'hd_ctime']  # 导出的项目


admin.site.site_header = 'AMS资产管理系统'
admin.site.site_title = "AMS资产管理系统"
