from django.contrib import admin

# Register your models here.
from utils.models import UpdateLog, TodoList


@admin.register(UpdateLog)
class TeamList(admin.ModelAdmin):
    list_display = ['id', 'up_title', 'up_text', 'up_ctime']  # 后台列表显示
    ordering = ['up_ctime']


@admin.register(TodoList)
class TeamList(admin.ModelAdmin):
    list_display = ['id', 'tl_title', 'tl_text', 'tl_ctime']  # 后台列表显示
    list_editable = ['tl_title', 'tl_text']
    ordering = ['tl_ctime']
