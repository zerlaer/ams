from django.db import models


# 员工信息
class User(models.Model):
    user_status_choice = [
        (0, '在职'),
        (1, '离职'),

    ]
    user_name = models.CharField(max_length=50, verbose_name="姓名")
    user_position = models.ForeignKey('Position', on_delete=models.CASCADE, null=True, blank=True, max_length=50,
        verbose_name="职务")
    user_workplace = models.CharField(max_length=50, verbose_name="职场")
    user_doamin = models.CharField(max_length=50, verbose_name="域账号")
    user_phone = models.CharField(max_length=50, verbose_name="工作手机")
    user_department = models.ForeignKey('Department', on_delete=models.CASCADE, null=True, blank=True, max_length=50,
        verbose_name="部门")
    user_pid = models.CharField(max_length=100, null=True, blank=True, verbose_name="员工工号")
    user_team = models.ForeignKey('Team', on_delete=models.CASCADE, null=True, blank=True, verbose_name="所在团队")
    user_address = models.ForeignKey('Address', on_delete=models.CASCADE, null=True, blank=True, verbose_name="所在区域")
    user_email = models.CharField(max_length=100, null=True, blank=True, verbose_name="员工邮箱")
    user_status = models.SmallIntegerField(choices=user_status_choice, default=0, verbose_name="状态")
    user_ctime = models.DateField(auto_now_add=True, verbose_name="创建时间")
    user_utime = models.DateField(auto_now=True, verbose_name="更新时间")

    def __str__(self):
        return self.user_name

    class Meta:
        verbose_name = '员工信息'
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


# 团队信息
class Team(models.Model):
    tm_name = models.CharField(max_length=50, verbose_name="团队名称", db_column="团队名称")
    tm_ctime = models.DateField(auto_now_add=True, verbose_name="创建时间", db_column="创建时间")

    tm_utime = models.DateField(auto_now=True, verbose_name="更新时间", db_column="更新时间")

    def __str__(self):
        return self.tm_name

    class Meta:
        verbose_name = '团队信息'
        verbose_name_plural = verbose_name


# 职位信息
class Position(models.Model):
    po_name = models.CharField(max_length=50, verbose_name="职位名称")
    po_ctime = models.DateField(auto_now_add=True, verbose_name="创建时间")
    po_utime = models.DateField(auto_now=True, verbose_name="更新时间")

    def __str__(self):
        return self.po_name

    class Meta:
        verbose_name = '职位信息'
        verbose_name_plural = verbose_name


# 地区信息
class Address(models.Model):
    ad_province = models.CharField(max_length=100, verbose_name="省份")
    ad_city = models.CharField(max_length=100, verbose_name="城市")
    ad_ctime = models.DateField(auto_now_add=True, verbose_name="创建时间")
    ad_utime = models.DateField(auto_now=True, verbose_name="更新时间")

    def __str__(self):
        return f"{self.ad_province}-{self.ad_city}"

    class Meta:
        verbose_name = '地区信息'
        verbose_name_plural = verbose_name
