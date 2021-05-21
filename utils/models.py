from django.db import models


# 系统更新日志
class UpdateLog(models.Model):
    up_title = models.CharField(max_length=100, verbose_name="标题")
    up_text = models.CharField(max_length=200, verbose_name="记录")
    up_ctime = models.DateField(auto_now_add=True, verbose_name="创建时间")
    up_utime = models.DateField(auto_now=True, verbose_name="更新时间")

    class Meta:
        verbose_name = '更新记录'
        verbose_name_plural = verbose_name


# 系统待更新事项
class TodoList(models.Model):
    todo_status_choices = [
        (0, '已完成'),
        (1, '待完成'),

    ]
    tl_title = models.CharField(max_length=100, verbose_name="标题")
    tl_text = models.CharField(max_length=200, verbose_name="记录")
    tl_status = models.CharField(choices=todo_status_choices, max_length=200, verbose_name="进度")
    tl_ctime = models.DateField(auto_now_add=True, verbose_name="创建时间")
    tl_utime = models.DateField(auto_now=True, verbose_name="更新时间")

    class Meta:
        verbose_name = '待办事项'
        verbose_name_plural = verbose_name
