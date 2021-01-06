# --*-- coding : utf-8 --*--
# Project      : Python_practice
# Current file : usecase_datas.py
# Author       : 大壮
# Create time  : 2020-03-24 17:21
# IDE          : PyCharm
# TODO 成长很苦，进步很甜，加油！
from tebiemiao_web.TestDatas.common_datas import CommonData as CD

# 用例数据

# 成功数据
success_data = \
    {'user': '11000000001', 'password': '1234567', 'check_url':CD.test_home_url}

# (登录导致提示弹框) 用户名为空，错误的用户名 / 密码 格式
wrong_data_tooltip = [
    # 调用登录页面，没有用户名
    {'user': '', 'password': '1234567', 'check': '账号密码不正确'},
    # 错误的用户名 / 密码 格式
    {'user': '1100000000', 'password': '123456', 'check': '账号不存在'}
]

# (登录导致密码下方提示文字)密码错误 - 密码下方提示错误
wrong_data_password = [
    # 调用登录页面，不填写密码
    {'user': '11000000001', 'password': '', 'check': '密码不能小于6位'},
    # 调用登录页面，密码填写一位数
    {'user': '11000000001', 'password': '1', 'check': '密码不能小于6位'}
]
