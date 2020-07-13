
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




