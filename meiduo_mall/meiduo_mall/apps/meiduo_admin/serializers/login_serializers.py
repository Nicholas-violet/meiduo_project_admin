

# 登陆接口数据校验序列化器定义
# 校验username和password两个参数

from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework_jwt.utils import jwt_payload_handler,jwt_encode_handler

class LoginSerializer(serializers.Serializer):

    # 定义序列化器类属性的形式来确定校验的字段
    username = serializers.CharField(
        write_only=True,
        max_length=10,
        required=True
    )
    password = serializers.CharField(
        write_only=True,
        max_length=20,
        required=True
    )


    def validate(self, attrs):
        # 实现验证用户名和密码 —— 传统身份校验
        # attrs = {"username": xxx, "password": "xxx"}

        # 1、传统身份校验
        user = authenticate(**attrs)
        if not user:
            raise serializers.ValidationError("用户名或密码错误！")


        # 2、生成token值
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)

        # 3、返回有效数据
        return {
            'user': user,
            'token': token
        }












