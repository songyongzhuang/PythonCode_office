# --*-- coding : utf-8 --*--
# Project      : Python_ketangpai
# Current file : login_datas.py
# Author       : 大壮
# Create time  : 2020-12-21 12:41
# IDE          : PyCharm
# TODO 成长很苦，进步很甜，加油！

"""
存放登录页面的数据
"""
# 调用公共数据
from test_datas.common_datas import CommonData as CD

# 成功用例 - 数据
correct_data = {'account': '17662460324',
                'password': 'song656421952',
                'check_url': CD.home_url}

# 用户名为空/密码为空
wrong_data = [
    {'account': '1', 'password': 'song656421952', 'check': '用户不存在'},
    {'account': '17662460324', 'password': '1', 'check': '请输入6-24位密码'}
]
