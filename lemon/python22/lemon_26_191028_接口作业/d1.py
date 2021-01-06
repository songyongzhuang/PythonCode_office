# --*-- coding : utf-8 --*--
# Project      : python22
# Current file : d1.py
# Author       : 大壮
# Create time  : 2019-11-02 16:17
# IDE          : PyCharm
# TODO 成长很苦，进步很甜，加油！
from suds import client

user_url = "http://120.24.235.105:9010/sms-service-war-1.0/ws/smsFacade.ws?wsdl "  # 这里是你的webservice访问地址
client = client.Client(user_url)
# print(client)
data = {"client_ip": "1233", "tmpl_id": 1, "mobile": "13511111122"}

res = client.service.sendMCode(data)
print(res)
