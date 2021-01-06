# --*-- coding : utf-8 --*--
# Project      : Interface_test
# Current file : requests_HTTP.py
# Author       : 大壮
# Create time  : 2020-07-12 16:53
# IDE          : PyCharm
# TODO 成长很苦，进步很甜，加油！
import requests
url = 'https://www.bilibili.com/'
res = requests.get(url)
print(res)
