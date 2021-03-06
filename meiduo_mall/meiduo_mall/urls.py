"""meiduo_mall URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include,re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'', include('users.urls')),
    re_path(r'', include('verifications.urls')),
    re_path(r'', include('oauth.urls')),
    re_path(r'', include('areas.urls')),
    re_path(r'', include('contents.urls')),
    re_path(r'', include('goods.urls')),
    re_path(r'', include('carts.urls')),
    re_path(r'', include('orders.urls')),
    re_path(r'', include('payment.urls')),

    # 把所有请求路径前缀为meiduo_admin的请求，转发给meiduo_admin应用的子路由去匹配
    re_path(r'^meiduo_admin/', include('meiduo_admin.urls')),
]
