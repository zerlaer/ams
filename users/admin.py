from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import Team, User, Department


# 注册 User 模块
@admin.register(User)
class UserList(ImportExportModelAdmin):
    list_display = ['id', 'user_name', 'user_pid', 'user_email', 'user_team', 'user_position', 'user_department',
                    'user_workplace', 'user_area', 'user_status', 'user_ctime', 'user_utime']  # 后台列表显示
    list_per_page = 50  # 每页显示的数量
    list_filter = ['user_name', 'user_team', 'user_pid', 'user_position', 'user_status']  # 列表过滤
    ordering = ['id']  # 按创建时间排序
    list_editable = ['user_name', 'user_team', 'user_position', 'user_status']
    search_fields = ['user_name', 'user_pid', 'user_team', 'user_position', 'user_status']  # 搜索项


# User 导入导出
class UserResource(resources.ModelResource):
    class Meta:
        model = User
        export_order = ['id', 'user_name', 'user_pid', 'user_email', 'user_team', 'user_position', 'user_department',
                        'user_workplace', 'user_area', 'user_status', 'user_ctime', 'user_utime']  # 导出的项目


# 注册 Team 模块
@admin.register(Team)
class UserList(admin.ModelAdmin):
    list_display = ['id', 'tm_name', 'tm_ctime', 'tm_utime']  # 后台列表显示


# 注册 Department 模块
@admin.register(Department)
class UserList(admin.ModelAdmin):
    list_display = ['id', 'dp_name', 'dp_ctime', 'dp_utime']  # 后台列表显示
