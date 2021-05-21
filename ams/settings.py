import os
import socket
import time
from pathlib import Path

SITE_ID = 1
# 项目的根目录
# 简化后面的操作
PROJECT_ROOT = os.path.dirname(os.path.dirname(__file__))
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-cthe*m$6xn)ykxn7lcmdsf*74-615r_38_t%4)hz&$xs+60z&%'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'simpleui',
    'import_export',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'assets.apps.AssetsConfig',
    'users.apps.UsersConfig',
    'utils.apps.UtilsConfig'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ams.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR, 'templates']
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'ams.wsgi.application'

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False

# 配置静态文件
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'staticfiles'),  # 主文件下静态文件
)
# 配置文件上传目录
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'uploads')

# MEDIA_URL是指从浏览器访问时的地址前缀。
MEDIA_URL = '/uploads/'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
BASE_LOG_DIR = os.path.join(BASE_DIR, "log")
# 打印日志
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        # 日志格式
        'standard': {
            'format': '[%(asctime)s] [%(filename)s:%(lineno)d] [%(module)s:%(funcName)s] '
                      '[%(levelname)s]- %(message)s'},
        'simple': {  # 简单格式
            'format': '%(levelname)s %(message)s'
        },
    },
    # 过滤
    'filters': {
    },
    # 定义具体处理日志的方式
    'handlers': {
        # 默认记录所有日志
        'default': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_LOG_DIR, 'all-{}.log'.format(time.strftime('%Y-%m-%d'))),
            'maxBytes': 1024 * 1024 * 5,  # 文件大小
            'backupCount': 5,  # 备份数
            'formatter': 'standard',  # 输出格式
            'encoding': 'utf-8',  # 设置默认编码，否则打印出来汉字乱码
        },
        # 输出错误日志
        'error': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_LOG_DIR, 'error-{}.log'.format(time.strftime('%Y-%m-%d'))),
            'maxBytes': 1024 * 1024 * 5,  # 文件大小
            'backupCount': 5,  # 备份数
            'formatter': 'standard',  # 输出格式
            'encoding': 'utf-8',  # 设置默认编码
        },
        # 控制台输出
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'standard'
        },
        # 输出info日志
        'info': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_LOG_DIR, 'info-{}.log'.format(time.strftime('%Y-%m-%d'))),
            'maxBytes': 1024 * 1024 * 5,
            'backupCount': 5,
            'formatter': 'standard',
            'encoding': 'utf-8',  # 设置默认编码
        },
    },
    # 配置用哪几种 handlers 来处理日志
    'loggers': {
        # 类型 为 django 处理所有类型的日志， 默认调用
        'django': {
            'handlers': ['default', 'console'],
            'level': 'INFO',
            'propagate': False
        },
        # log 调用时需要当作参数传入
        'log': {
            'handlers': ['error', 'info', 'console', 'default'],
            'level': 'INFO',
            'propagate': True
        },
    }
}

# 数据库配置
MYDB = {
    'mysql': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'ams',  # 你的数据库名称
        'USER': 'root',  # 你的数据库用户名
        'PASSWORD': 'root',  # 你的数据库密码
        'HOST': '',  # 你的数据库主机，留空默认为localhost
        'PORT': '3306',  # 你的数据库端口
    },
    'sqlite': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_ROOT, 'db/db.sqlite3').replace('\\', '/'),
    }
}
DATABASES = {
    'default': MYDB.get('mysql')
}

# Simple UI 配置

SIMPLEUI_HOME_INFO = False  # 关闭Simple信息
SIMPLEUI_ANALYSIS = False  # 关闭用户数据收集

SIMPLEUI_LOGO = 'https://image-zerlaer.oss-cn-chengdu.aliyuncs.com/logo.png'
SIMPLEUI_CONFIG = {
    'system_keep': False,
    'menus': [

        {
            'app': 'assets',
            'name': '资产管理',
            'icon': 'fa fa-server',
            'models': [
                {
                    'name': '电脑设备',
                    'url': 'assets/computer',
                    'icon': 'fa fa-laptop'
                },
                {
                    'name': '打印机设备',
                    'url': 'assets/printer',
                    'icon': 'fas fa-print'
                },
                {
                    'name': '服务器设备',
                    'url': 'assets/server',
                    'icon': 'fas fa-hdd'
                },
                {
                    'name': '网络设备',
                    'url': 'assets/printer',
                    'icon': 'fas fa-server'
                },
                {
                    'name': 'IP话机',
                    'url': 'assets/sipphone',
                    'icon': 'fa fa-fax'
                },
                {
                    'name': '模拟话机',
                    'url': 'assets/telephone',
                    'icon': 'fa fa-phone'
                },
                {
                    'name': '供应商',
                    'url': 'assets/manufacturer',
                    'icon': 'fa fa-life-ring'
                },
            ]
        },
        {
            'app': 'users',
            'name': '员工管理',
            'icon': 'fa fa-address-book',
            'models': [
                {
                    'name': '员工信息',
                    'url': 'users/user',
                    'icon': 'fa fa-id-badge'
                },
                {
                    'name': '团队信息',
                    'url': 'users/team',
                    'icon': 'fa fa-trademark'
                },

                {
                    'name': '职位管理',
                    'url': 'users/position',
                    'icon': 'fa fa-briefcase'
                },
                {
                    'name': '地区管理',
                    'url': 'users/address',
                    'icon': 'fa fa-location-arrow'
                },
                {
                    'name': '部门信息',
                    'url': 'users/department',
                    'icon': 'fa fa-sitemap'
                },

            ]
        },
        {
            'app': 'auth',
            'name': '权限管理',
            'icon': 'fa fa-cog',
            'models': [
                {
                    'name': '用户管理',
                    'url': 'auth/user',
                    'icon': 'fa fa-user-plus'
                },
                {
                    'name': '用户组管理',
                    'url': 'auth/group',
                    'icon': 'fa fa-users'
                }
            ]
        },
        {
            'app': 'utils',
            'name': '更新记录',
            'icon': 'fa fa-bookmark',
            'models': [
                {
                    'name': '更新记录',
                    'url': 'utils/updatelog',
                    'icon': 'fa fa-list'
                },
                {
                    'name': '待办事项',
                    'url': 'utils/todolist',
                    'icon': 'fa fa-check-square'
                },
            ]
        },
    ]
}
