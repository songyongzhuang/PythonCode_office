# --*-- coding ：utf-8 --*--
# Project      ：python22
# Current file ：d1_json.py
# Author       ：Administrator
# Create time  ：2019/10/23 16:47
# IDE          ：PyCharm
# TODO 成长很苦, 进步很甜, 加油！

import json

# 讲字典转行成json
# None 转换成unll
# 单引号转换成 双引号
# 中文字符问题 ensure_ascii
user_info = {'name': 'manman', 'age': '哈哈'}
user_json = json.dumps(user_info, ensure_ascii=False)
print(user_json)
print(type(user_json))


# json 转换成字典
user_info_new = json.loads(user_json)
print(user_info_new)
print(type(user_info_new))


# 字符串当中应该是双引号，不能用单引号
wrong_json = '{"username": "yuyu"}'
print(json.loads(wrong_json, encoding='utf-8'))
print(type(wrong_json))

























