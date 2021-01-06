# --*-- coding ：utf-8 --*--
# Project      ：python22_web
# Current file ：Login_Datas.py
# Author       ：Administrator猜猜猜
# Create time  ：2019/12/04 9:17
# IDE          ：PyCharm
# TODO 成长很苦, 进步很甜, 加油！

#
"""
用例数据
"""''
from lemon_10_191204.TestDatas.Common_Datas import CD


class LD(object):
    # 成功用例 - 数据
    success_data = {'user': '18684720553', 'passwd': 'python', 'check_url': CD.home_url, 'check_quit_exist': True}

    # 手机号为空/密码为空/格式不正确/
    wrong_datas = [
        {'user': '', 'passwd': 'python', 'check': '请输入手机号'},
        {'user': '18684720553', 'passwd': '', 'check': '请输入密码'},
        {'user': '186847205', 'passwd': 'python11', 'check': '请输入正确的手机号'}
    ]

