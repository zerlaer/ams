from django.db import models


# 员工信息
class User(models.Model):
    user_status_choice = [
        (0, '在职'),
        (1, '离职'),

    ]
    user_position_choice = [

        ('AD', '行政'),
        ('QA', '质检'),
        ('DH', '跟单'),
        ('TR', '培训'),
        ('RE', '招聘'),
        ('TMR', '销售'),
        ('TMS', '销售主管'),
        ('CCM', '销售经理'),
        ('TM', '项目负责人'),
    ]
    user_area_choice = [
        ('N', '网电西区'),
        ('S', '网电南区'),
        ('E', '网电东区'),
        ('W', '网电北区'),
        ('C', '网电中区'),
    ]
    user_name = models.CharField(max_length=50, verbose_name="姓名")
    user_position = models.CharField(max_length=30, choices=user_position_choice, default='TMR', verbose_name="职务")
    user_workplace = models.CharField(max_length=50, verbose_name="职场")
    user_doamin = models.CharField(max_length=50, verbose_name="域账号")
    user_phone = models.CharField(max_length=50, verbose_name="工作手机")
    user_department = models.ForeignKey('Department', on_delete=models.CASCADE, null=True, blank=True, max_length=50,
        verbose_name="部门")
    user_pid = models.CharField(max_length=100, null=True, blank=True, verbose_name="员工工号")
    user_team = models.ForeignKey('Team', on_delete=models.CASCADE, null=True, blank=True, verbose_name="所在团队")
    user_area = models.CharField(choices=user_area_choice, default='N', max_length=50, verbose_name="所在区域")
    user_email = models.CharField(max_length=100, null=True, blank=True, verbose_name="员工邮箱")
    user_status = models.SmallIntegerField(choices=user_status_choice, default=0, verbose_name="状态")
    user_ctime = models.DateField(auto_now_add=True, verbose_name="创建时间")
    user_utime = models.DateField(auto_now=True, verbose_name="更新时间")

    def __str__(self):
        return self.user_name, self.user_team, self.get_user_area_display()

    class Meta:
        verbose_name = '员工信息'
        verbose_name_plural = verbose_name


# 团队信息
class Team(models.Model):
    tm_name = models.CharField(max_length=50, verbose_name="团队名称", db_column="团队名称")
    tm_department = models.CharField(max_length=50, verbose_name="所属部门", db_column="所属部门")
    tm_ctime = models.DateField(auto_now_add=True, verbose_name="创建时间", db_column="创建时间")

    tm_utime = models.DateField(auto_now=True, verbose_name="更新时间", db_column="更新时间")

    def __str__(self):
        return self.tm_name

    class Meta:
        verbose_name = '团队信息'
        verbose_name_plural = verbose_name


# 部门信息
class Department(models.Model):
    dp_name = models.CharField(max_length=50, verbose_name="部门名称")
    dp_ctime = models.DateField(auto_now_add=True, verbose_name="创建时间")
    dp_utime = models.DateField(auto_now=True, verbose_name="更新时间")

    def __str__(self):
        return self.dp_name

    class Meta:
        verbose_name = '部门信息'
        verbose_name_plural = verbose_name
