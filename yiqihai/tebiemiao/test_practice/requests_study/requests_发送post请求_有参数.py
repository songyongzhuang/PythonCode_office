# --*-- coding : utf-8 --*--
# Project      : Interface
# Current file : requests_发送get请求_有参数.py.py
# Author       : 大壮
# Create time  : 2020-01-15 20:29
# IDE          : PyCharm
# TODO 成长很苦，进步很甜，加油！
import requests

# data
url = 'http://127.0.0.1:5000/login'
data = {'username': 'PyCharm', 'pwd': '123456'}
# 传递参数的三种方式：params，data，json
res = requests.post(url, params=data, data=data)
# res1 = requests.post(url, params=data, json=data)
print(res.text)
# 获取所有的cookies
cookies = res.cookies

url1 = 'http://127.0.0.1:5000'
res1 = requests.post(url1, cookies=cookies)
print(res1.text)
# session 自动管理 cookies
