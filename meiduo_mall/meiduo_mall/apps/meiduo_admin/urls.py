
from django.urls import re_path
from meiduo_admin.views.login_views import *
from meiduo_admin.views.home_views import *

urlpatterns = [
    re_path(r'^authorizations/$', LoginAPIView.as_view()),
    # 用户总数量
    re_path(r'^statistical/total_count/$', UserTotalCountView.as_view()),
    # 用户日新增
    re_path(r'^statistical/day_increment/$', UserDayCountView.as_view()),
    # 用户日活跃数量
    re_path(r'^statistical/day_active/$', UserActiveCountView.as_view()),
    # 日用户下订单
    re_path(r'^statistical/day_orders/$', UserOrderCountView.as_view()),
    # 日分类,月用户增加统计
    re_path(r'^statistical/month_increment/$', UserMonthCountView.as_view()),
]