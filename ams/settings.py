import os
import socket
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
DEBUG = True

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

# 配置文件上传目录
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'uploads')

# MEDIA_URL是指从浏览器访问时的地址前缀。
MEDIA_URL = '/uploads/'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# 打印日志
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django.db.backends': {
            'handlers': ['console'],
            'propagate': True,
            'level': 'DEBUG',
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
                    'name': 'IP话机',
                    'url': 'assets/sipphone',
                    'icon': 'fa fa-microphone'
                }, {
                    'name': '模拟话机',
                    'url': 'assets/telephone',
                    'icon': 'fa fa-phone'
                },
                {
                    'name': '耳机设备',
                    'url': 'assets/headset',
                    'icon': 'fa fa-headphones'
                }
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
                    'name': '部门信息',
                    'url': 'users/department',
                    'icon': 'fa fa-briefcase'
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
    ]
}
