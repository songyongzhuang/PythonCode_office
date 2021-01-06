# --*-- coding : utf-8 --*--
# Project      : python_lemon_作业
# Current file : 练习requests_get带参数.py
# Author       : 大壮
# Create time  : 2019-10-15 20:56
# IDE          : PyCharm
# TODO 成长很苦，进步很甜，加油！
import requests

url = 'http://127.0.0.1:5000/'
data = {'username': 'mei', 'ped': '123456'}  # 多个参数
# 传递参数的三种方式：params, data, json
# post 把参数放到URL里面
# res = requests.post(url, params=data)

# post 把参数通过
# res = requests.post(url, params=data, data=data)

# post 把参数通过json
res = requests.post(url, json=data)

# 响应格式
print(res.text)
