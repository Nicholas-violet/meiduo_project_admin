
from rest_framework.views import APIView
from rest_framework.response import Response
from users.models import *
from django.utils import timezone


# 用户总量展示
class UserTotalCountView(APIView):

    def get(self, request):
        count = User.objects.count()
        date = timezone.localtime().date()

        return Response({
            'count':count,
            'date':date
        })

def get_local_0_time():
    # 获取当前时间
    cur_time = timezone.localtime()
    # 获取到零时刻的时间
    local_0_time = cur_time.replace(hour=0, minute=0, second=0)
    return local_0_time


# 日增用户统计
class UserDayCountView(APIView):

    def get(self, request):
        local_0_time = get_local_0_time()
        count = User.objects.filter(date_joined__gte=local_0_time).count()
        return Response({
            'count':count,
            'date':local_0_time.date()
        })


# 日活跃用户统计
class UserActiveCountView(APIView):

    def get(self, request):
        local_0_time = get_local_0_time()
        count = User.objects.filter(last_login__gte=local_0_time).count()
        return Response({
            'count':count,
            'date':local_0_time.date()
        })


# 日下订单用户统计
class UserOrderCountView(APIView):

    def get(self, request):
        local_0_time = get_local_0_time()
        count = User.objects.filter(orders__create_time__gte=local_0_time).count()
        return Response({
            'count':count,
            'date':local_0_time.date()
        })


# 日分类商品访问,月增用户统计
class UserMonthCountView(APIView):

    def get(self, request):
        # 获取当日零时刻,以及29天前的;零时刻
        # 获取当日时间
        local_0_time = get_local_0_time()
        # 获取到29天前的日期
        cur_0_time = local_0_time - timezone.timedelta(days=29)
        user_count_list = []
        # for循环遍历
        for index in range(30):
            start_time = cur_0_time + timezone.timedelta(days=index)
            end_time = start_time + timezone.timedelta(days=1)

            count = User.objects.filter(date_joined__gte=start_time, date_joined__lt=end_time).count()
            user_count_list.append({
                'count':count,
                'date':cur_0_time.date()
            })

        return Response(user_count_list)

