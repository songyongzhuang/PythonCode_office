# --*-- coding : utf-8 --*--
# Project      : python_lemon_作业
# Current file : 练习requests_post_获取cookie_4.py
# Author       : 大壮
# Create time  : 2019-10-15 20:56
# IDE          : PyCharm
# TODO 成长很苦，进步很甜，加油！
import requests

url = 'http://127.0.0.1:5000/login'
data = {'username': 'mei', 'ped': '123456'}  # 多个参数
# post 把参数通过json
res = requests.post(url, data=data)

# 响应格式
print(res.text)

# 获取所有的cookies
cookie = res.cookies

url1 = 'http://127.0.0.1:5000'
# 不是返回 hello world 是因为没有带cookie
res1 = requests.post(url1, cookies=cookie)
print(res1.text)

requests.session()
