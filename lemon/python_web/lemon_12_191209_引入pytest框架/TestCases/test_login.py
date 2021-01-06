
# !/usr/bin/python3
"""
@File    : test_login.py
@Time    : 2019/11/29 21:53
@Author  : 柠檬班-小简
@Email   : lemonban_simple@qq.com
@Company: 湖南省零檬信息技术有限公司
"""
from selenium import webdriver
import ddt
import logging
import pytest

# 导包元素操作，
from lemon_12_191209_引入pytest框架.PageObjects.login_page import LoginPage
from lemon_12_191209_引入pytest框架.PageObjects.home_page import HomePage
from lemon_12_191209_引入pytest框架.Common import logger
from lemon_12_191209_引入pytest框架.TestDatas import Common_Datas as CD
from lemon_12_191209_引入pytest框架.TestDatas import login_datas as LD


@pytest.fixture()
# function 默认是测试用例(函数)级别
# 测试类(class)级别
# module 模块级别(.py)
# package 包
# session 测试用例会话
def init_driver():
    # 前置
    # 打开谷歌浏览器
    driver = webdriver.Chrome()
    # 最大化浏览器
    driver.maximize_window()
    # 打开URL地址
    driver.get(CD.login_url)
    # 初始 LoginPage 方便调用
    lp = LoginPage(driver)
    # 分隔前值和后置
    yield {'driver': driver, 'lp': lp}
    # 后置
    # 关闭浏览器
    driver.quit()


# 绑定这个类下面的测试用例，使用 init_driver 这个前置后置
# @pytest.mark.usefixtures('init_driver')  # 调用里前置 后置
# fixture 的函数名称作为用例的参数 = 返回值
# pytest会自动搜索 fixture 当中，没有同名的fixture 函数，有就拿来用
class TestLogin:

    # 正常场景 - 登陆成功。
    @pytest.mark.usefixtures('init_driver')
    def test_login_success(self, init_driver):
        logging.info("******* 登陆功能 - 正常场景用例：登陆成功 *******")
        # 调用登陆页面的。登陆行为。
        init_driver['lp'].login(LD.success_data["user"], LD.success_data["passwd"])
        # 断言 - 首页当中，应该存在 退出元素。
        assert (HomePage(init_driver['driver']).check_user_exist())
        # 断言2 - url地址  应当为 http://120.78.128.25:8765/Index/index
        assert (init_driver['driver'].current_url == LD.success_data["check_url"])

    # # 异常用例 - 用户名为空/密码为空/用户名格式不正确
    # def test_login_failed_by_wrongData(self, case):
    #     logging.info("******* 登陆功能 - 异常场景用例：数据格式校验 - 用户名为空/密码为空/用户名格式不正确 *******")
    #     # 调用登陆页面的。登陆行为。
    #     self.lp.login(case["user"], case["passwd"])
    #     # 断言 - 登陆页面 - 应当现提示信息：请输入手机号
    #     self.assertEqual(case["check"], self.lp.get_error_msg())
    #
    # # 错误的密码
    # def test_login_failed_by_wrong_passwd(self):
    #     logging.info("******* 登陆功能 - 异常场景用例：数据后台有效性校验 - 密码错误 *******")
    #     # 调用登陆页面的。登陆行为。
    #     self.lp.login("18684720553", "python11")
    #     # 断言 - 登陆页面 - 应当现提示信息：帐号或密码错误!
    #     self.assertEqual("帐号或密码错误!", self.lp.get_error_msg_from_dialog())
