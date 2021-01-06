# --*-- coding : utf-8 --*--
# Project      : Python_ketangpai
# Current file : common_datas.py
# Author       : 大壮
# Create time  : 2020-12-21 12:42
# IDE          : PyCharm
# TODO 成长很苦，进步很甜，加油！
"""
存放 共同的 数据
"""


class CommonData:
    # 服务器访问的base_url
    base_url = 'https://www.ketangpai.com'
    # 登陆页面地址
    login_url = base_url + '/User/login.html'
    # 登录后首页地址
    home_url = base_url + '/Main/index.html'

    # 课程的id是唯一的，换课程请从新获取对应课程 data-id 的值
    # TODO  22期地址：MDAwMDAwMDAwMLOsx5SGqclq  练习地址：MDAwMDAwMDAwMLR2vd6Gz8mw
    data_id = "MDAwMDAwMDAwMLR2vd6Gz8mw"
    # 进入课程url地址
    enter_course_url = base_url + f'/Interact/index/courseid/{data_id}.html'

    # 正确的用户名、密码
    user = '17662460324'
    password = 'song656421952'

    # 需要加入课程的验证码
    course_verify = 'P69UVV'
