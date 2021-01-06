# --*-- coding : utf-8 --*--
# Project      : Interface
# Current file : requests_发送get请求_有参数.py.py
# Author       : 大壮
# Create time  : 2020-01-15 20:29
# IDE          : PyCharm
# TODO 成长很苦，进步很甜，加油！
import requests

url = 'http://127.0.0.1:5000/'
data = {'username': 'PyCharm', 'pwd': '123456'}
res = requests.get(url, params=data)
print(res.text)

# 带请求头
headers = {'User-Agent': 'Google'}
res = requests.get(url, params=data, headers=headers)
print(res.text)
