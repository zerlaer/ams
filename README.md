## AMS资产管理系统

> Python3.8.5+Django3.2 + Bootstrap4.7 + MySQL8.0

## 项目简介

ams 是基于 Django+django-simpleui+ Bootstrap+MySQL的后台管理系统，
是我学习Django框架的练手项目，使用Django自带的admin管理后台修改而成；开发初衷是想使用WEB页面+数据库代替Excel和纸质统计表；

默认账号：admin，密码：admin

目前前端已完成基本视图和路由，页面内容还未完成。

![image-20210522025623430](https://image-zerlaer.oss-cn-chengdu.aliyuncs.com/image-20210522025623430.png)

![image-20210522025427343](https://image-zerlaer.oss-cn-chengdu.aliyuncs.com/image-20210522025427343.png)

## 主要功能

- 资产管理：对常见资产设备信息进行统一管理

    - 电脑设备
    - 打印机设备
    - 服务器设备
    - 网络设备
    - IP话机
    - 模拟话机

- 员工管理：对人员信息进行统一管理

    - 员工信息

    - 部门信息
    - 团队信息
    - 职位信息
    - 地区信息

- 系统日志：记录用户操作日志与异常日志，方便开发人员定位排错

  ![AMS资产管理系统](https://image-zerlaer.oss-cn-chengdu.aliyuncs.com/AMS%E8%B5%84%E4%BA%A7%E7%AE%A1%E7%90%86%E7%B3%BB%E7%BB%9F.png)

## [#](https://el-admin.vip/guide/kslj.html#项目结构)项目结构

![详细结构](https://image-zerlaer.oss-cn-chengdu.aliyuncs.com/%E8%AF%A6%E7%BB%86%E7%BB%93%E6%9E%84.png)

# 快速开始

使用该项目前，你需要检查你本地的开发环境，避免出现问题!

## [#](https://el-admin.vip/guide/ksks.html#所需环境)所需环境

这里列出本人做项目时所使用的的环境，方便想使用的朋友参考和安装

> TIP
>
> python安装包可以使用华为云镜像或阿里镜像，pip源可使用清华pypi源，最好使用python虚拟环境运行项目
>
> https://repo.huaweicloud.com/python/
>
> http://npm.taobao.org/mirrors/python/
>
> https://mirrors.tuna.tsinghua.edu.cn/help/pypi/

```text
1.Python 3.8.5
安装教程：https://www.runoob.com/python/python-install.html
2.Django 3.2.3
安装教程：https://www.runoob.com/django/django-install.html
3、django-simpleui 2021.5.21 
安装教程：https://simpleui.72wo.com/docs/simpleui/doc.html
4、MYSQL 8.0.0
安装教程：https://www.runoob.com/mysql/mysql-install.html

```

这里提供我自己的requirements.txt 安装好python后终端输入pip install -r requirements.txt 安装所需要的包

```text
asgiref==3.3.4
defusedxml==0.7.1
diff-match-patch==20200713
django-import-export==2.5.0
django-simpleui==2021.5.21
Django==3.2.3
et-xmlfile==1.1.0
MarkupPy==1.14
mysqlclient==2.0.3
odfpy==1.4.1
openpyxl==3.0.7
pip==21.1.1
pytz==2021.1
PyYAML==5.4.1
setuptools==56.2.0
sqlparse==0.4.1
tablib==3.0.0
xlrd==2.0.1
xlwt==1.3.0
```

## 运行项目

前面的环境搭建好之后就可以运行项目了，需要首先在终端输入下面的命令

```
# 收集django所需静态文件:
python manage.py collectstatic
# 同步或者更改生成 数据库:
python manage.py makemigrations
python manage.py migrate
# 创建管理员: 
python manage.py createsuperuser
# 运行项目:
python manage.py runserver --insecure
```