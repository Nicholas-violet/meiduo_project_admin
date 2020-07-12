"""
Django settings for meiduo_mall project.

Generated by 'django-admin startproject' using Django 2.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""
import datetime
import os,sys
# sys.path是一个列表，该列表存储所有导包路径

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# 内层工程目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 把apps文件夹加入导包路径列表头部，优先在apps中查找包
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'e2+tq*u827f%7g074@f91(qx3w_g(_%vj4-deaj9ga0ps-p_=m'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Django允许以什么域名来访问Django
ALLOWED_HOSTS = ["*"]
# ALLOWED_HOSTS = ["*"]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'corsheaders',
    # 'django_crontab',
    # 'haystack', # 拓展工具，是Django和ES之间的桥梁

    'users',
    'verifications',
    'oauth',
    'areas',
    'contents',
    'goods',
	'carts',
    'orders',
    'payment',
    'meiduo_admin',
]




MIDDLEWARE = [
    # 优先处理跨域
    'corsheaders.middleware.CorsMiddleware',

    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'meiduo_mall.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'meiduo_mall.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'meiduo_mis_db',
        'HOST': '192.168.203.161',
        'USER': 'root',
        'PASSWORD': 'mysql',
        'PORT': 3306
    },
    # 'slave': {
    #     'ENGINE': 'django.db.backends.mysql',
    #     'NAME': 'meiduo_mall_db',
    #     'HOST': '192.168.203.161',
    #     'USER': 'root',
    #     'PASSWORD': '123456',
    #     'PORT': 8306
    # }
}

# 指定自定义的数据库路由后端导包路径
# DATABASE_ROUTERS = [
#     'meiduo_mall.utils.db_router.MasterSlaveDBRouter'
# ]


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'


# redis缓存
CACHES = {
    "default": { # 默认存储信息: 存到 0 号库
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://192.168.203.161:6379/0",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    },
    "session": { # session 信息: 存到 1 号库
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://192.168.203.161:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    },
    "verify_code": { # session 信息: 存到 1 号库
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://192.168.203.161:6379/2",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    },
    "history": { # 存放用户浏览历史记录
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://192.168.203.161:6379/3",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    },
    "carts": { # 存放用户浏览历史记录
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://192.168.203.161:6379/4",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    },
}
SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "session"


# 定义了一个日志
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,  # 是否禁用已经存在的日志器
    'formatters': {  # 日志信息显示的格式
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(lineno)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(module)s %(lineno)d %(message)s'
        },
    },
    'filters': {  # 对日志进行过滤
        'require_debug_true': {  # django在debug模式下才输出日志
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    # 句柄
    'handlers': {  # 日志处理方法
        'console': {  # 向终端中输出日志
            'level': 'INFO',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'file': {  # 向文件中输出日志
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'logs/meiduo.log'),  # 日志文件的位置
            'maxBytes': 300 * 1024 * 1024,
            'backupCount': 10,
            'formatter': 'verbose'
        },
    },

    'loggers': {  # 日志器
        'django': {  # 定义了一个名为django的日志器
            'handlers': ['console', 'file'],  # 可以同时向终端与文件中输出日志
            'propagate': True,  # 是否继续传递日志信息
            'level': 'INFO',  # 日志器接收的最低日志级别
        },
    }
}


# 配置跨域白名单
CORS_ORIGIN_WHITELIST = (
    # 把静态服务器的协议、域名和端口加入白名单
    'http://127.0.0.1:8081',
    'http://www.meiduo.site:8081',
    'http://127.0.0.1:8080',
    'http://www.meiduo.site:8080',
)

# 跨域请求允许携带cookie数据
CORS_ALLOW_CREDENTIALS = True

# 指定django工程使用的用户模型类
# 该配置项用户模型类指定，有django特殊的语法规范： '应用:模型类'
AUTH_USER_MODEL = 'users.User'

# 认证后端
AUTHENTICATION_BACKENDS = [
    'users.utils.UsernameMobileAuthBackend',
]



# QQ登录参数
# 我们申请的 客户端id
QQ_CLIENT_ID = '101474184'
# 我们申请的 客户端秘钥
QQ_CLIENT_SECRET = 'c6ce949e04e12ecc909ae6a8b09b637c'
# 我们申请时添加的: 登录成功后回调的路径
QQ_REDIRECT_URI = 'http://www.meiduo.site:8080/oauth_callback.html'



# 发送短信的相关设置, 这些设置是当用户没有发送相关字段时, 默认使用的内容:
# 发送短信必须进行的设置:
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# 我们使用的 smtp服务器 地址
EMAIL_HOST = 'smtp.163.com'
# 端口号
EMAIL_PORT = 25
# 下面的内容是可变的, 随后台设置的不同而改变:
# 发送邮件的邮箱
EMAIL_HOST_USER = 'itcast_weiwei@163.com'
# 在邮箱中设置的客户端授权密码
EMAIL_HOST_PASSWORD = 'OQSKSEISPZVTHEMK'
# 收件人看到的发件人
EMAIL_FROM = '美多商城<itcast_weiwei@163.com>'
# 邮箱验证链接
EMAIL_VERIFY_URL = 'http://www.meiduo.site:8080/success_verify_email.html?token='

# 该配置项，指定django使用的文件存储后端
DEFAULT_FILE_STORAGE = "meiduo_mall.utils.fastdfs.fastdfs_storage.FastDFSStorage"


# 自定义fdfs文件存储服务器的域名
FDFS_URL = "http://image.meiduo.site:8888/"


# 自定义静态文件保存的根目录
GENERATED_STATIC_HTML_DIR = os.path.join(os.path.dirname(os.path.dirname(BASE_DIR)), 'front_end_pc')


# 定时任务django_crontab的配置项
CRONJOBS = [
    # 每1分钟生成一次首页静态文件
    ('*/1 * * * *',
     'contents.generate_index.generate_index_html',
     '>> ' + os.path.join(BASE_DIR, 'logs/crontab.log')
    ), # 一个任务
]


# 指定es搜索服务位置
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
        'URL': 'http://192.168.203.161:9200/', # Elasticsearch服务器ip地址，端口号固定为9200
        'INDEX_NAME': 'meiduo_mall', # Elasticsearch建立的索引库的名称
    },
}

# 当添加、修改、删除数据时，自动生成索引
HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'

# 可以在 dev.py 中添加如下代码, 用于决定每页显示数据条数:
HAYSTACK_SEARCH_RESULTS_PER_PAGE = 5




# 应用的id，此处开发阶段写沙盒应用的id
ALIPAY_APPID = '2016091600526851'
ALIPAY_DEBUG = True
# 此处是沙箱url，上线之后修改为线上app的支付链接
ALIPAY_URL = 'https://openapi.alipaydev.com/gateway.do'
ALIPAY_RETURN_URL = "http://www.meiduo.site:8080/pay_success.html"


# DRF配置
REST_FRAMEWORK = {

    # 身份认证后端
    'DEFAULT_AUTHENTICATION_CLASSES': (
        # jwt身份认证
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',

        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
}

# JWT配置项
JWT_AUTH = {
    # 签发的token的有效期为100天
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=100),
}