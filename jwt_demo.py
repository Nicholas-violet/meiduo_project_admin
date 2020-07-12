

import json,base64

# =======生成header========
header = {
  'typ': 'JWT', # 类型/格式
  'alg': 'HS256' # 哈希算法，使用该算法生成token字符串的第三部分
}
# 1、把字典序列化成json字符串
header = json.dumps(header)
# 2、把字符串，使用base64编码
header = base64.b64encode(header.encode())
print("header:", header)

# =======生成payload========
payload = {
    'username': 'weiwei',
    'user_id': 1
}
payload = json.dumps(payload)
payload = base64.b64encode(payload.encode())
print('payload:', payload)



# =======生成签名========
# hmac:算法接口，hashlib:算法实现
import hmac,hashlib

SECRET_KEY = b'e2+tq*u827f%7g074@f91(qx3w_g(_%vj4-deaj9ga0ps-p_=m'
# 1、构造信息摘要
message = header.decode() + '.' + payload.decode()
# 2、配合密钥和信息摘要，使用HS256生成签名
h_obj = hmac.new(SECRET_KEY, msg=message.encode(), digestmod=hashlib.sha256)
signature = h_obj.hexdigest()
print("signature:", signature)


# ======完整的token值========
token = header.decode() + '.' + payload.decode() + '.' + signature
print('token值:', token)



# ======演示验证的流程======
# 原理：对摘要信息重写签名，比对心就签名是否一致来判断信息是否被篡改

# 1、模拟前端接受token值
# token_from_browser = token # 模拟没有篡改
token_from_browser = "fewf" + token # 篡改

# 2、提取三段数据
header_front = token_from_browser.split('.')[0]
payload_front = token_from_browser.split('.')[1]
old_signature = token_from_browser.split('.')[2]

# 3、重写签发新签名和旧签名比对
message = header_front + '.' + payload_front
h_obj = hmac.new(SECRET_KEY, message.encode(), digestmod=hashlib.sha256)
new_signture = h_obj.hexdigest()

# 4、判断
if new_signture == old_signature:
    print("数据是完整的！")
else:
    print("数据被篡改了！")









