安装Django： pip install django 指定版本 pip3 install django==2.0

新建项目： django-admin.py startproject mysite

新建APP : python manage.py startapp blog

启动：python manage.py runserver 8080

同步或者更改生成 数据库：

python manage.py makemigrations

python manage.py migrate

清空数据库： python manage.py flush

创建管理员： python manage.py createsuperuser

修改用户密码： python manage.py changepassword username

Django项目环境终端： python manage.py shell