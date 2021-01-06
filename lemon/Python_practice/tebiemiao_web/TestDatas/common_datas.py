# --*-- coding : utf-8 --*--
# Project      : Python_practice
# Current file : common_datas.py
# Author       : 大壮
# Create time  : 2020-03-24 17:07
# IDE          : PyCharm
# TODO 成长很苦，进步很甜，加油！

# 公共数据


class CommonData(object):
    # ------------------------  生产环境URL地址 ------------------------
    # 线上平台后台
    base_url = 'https://cs.tebiemiao.cn'
    # 线上酒店后台
    hotel = 'https://hotel.tebiemiao.cn'
    # 线上环境平台后台登录 url 地址
    production_login_url = base_url + '/#/login'

    # ------------------------  测试环境URL地址 ------------------------
    # 测试环境平台后台 - base_url域名地址
    test_base = 'https://cs.test.tebiemiao.cn'
    # 测试环境酒店后台
    test_hotel = 'https://hotel.test.tebiemiao.cn'
    # 测试环境平台后台登录 url 地址
    test_login_url = test_base + '/#/login'
    # 测试环境酒店后台登录 url 地址
    test_hotel_url = test_hotel + '/#/login'
    # 测试环境平台后台首页地址(登录成功后首页URL地址)
    test_home_url = test_base + '/#/dashboard'

    # ------------------------  生产环境用户角色 ------------------------
    # 平台后台test-测试运营人员01
    user = '11000000001'
    password = '1234567'
    # 超管
    super_user = 'super'
    super_password = 'sss921028'
    # 酒店后台管理员角色
    hotel_user = '11000000014'
    hotel_password = '1234567'
