
from rest_framework.response import Response
from rest_framework.views import APIView
from meiduo_admin.serializers.login_serializers import *

class LoginAPIView(APIView):

    def post(self, request):
        # 1、构建一个序列化器对象，传入前端传参
        serializer = LoginSerializer(data=request.data)
        # 2、启动校验流程
        serializer.is_valid(raise_exception=True)
        # 3、校验成功，提取有效数据中的用户信息和token值返回
        user = serializer.validated_data['user']
        token = serializer.validated_data['token']
        return Response({
            'username': user.username,
            'user_id': user.id,
            'token': token
        })