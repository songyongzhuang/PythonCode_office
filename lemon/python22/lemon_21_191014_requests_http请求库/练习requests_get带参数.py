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
res = requests.get(url, params=data)  # get 把参数放到URL里面
print(res.text)

# ------------------ 带请求头 ------------------
headers = {'User-Agent': 'huawei p30'}
res = requests.get(url, params=data, headers=headers)
