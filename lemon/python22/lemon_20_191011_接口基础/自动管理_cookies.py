# --*-- coding ：utf-8 --*--
# IDE          ：PyCharm
# Project      ：柠檬班作业
# Current file ：自动管理_cookies.py
# Author       ：Administrator
# Create time  ：2019/10/22 14:34
# TODO 成长很苦, 进步很甜, 加油！

import requests

url = 'http://127.0.0.1:5000/'
url_login = 'http://127.0.0.1:5000/login'
# 创建会话对象, 自动收集cookie
session = requests.Session()
# 会话访问
res = session.get(url_login)
res1 = session.get(url)
print(res1.text)


