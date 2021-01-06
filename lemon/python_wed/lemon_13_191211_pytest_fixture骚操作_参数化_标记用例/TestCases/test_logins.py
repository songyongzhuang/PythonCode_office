
# Project      : python_wed
# Current file : test_logins.py
# Author       : 大壮
# Create time  : 2019-12-15 10:46
# IDE          : PyCharm
# TODO 成长很苦，进步很甜，加油！
import logging
import pytest

# 导包元素操作，
from lemon_12_191209_引入pytest框架.PageObjects.login_page import LoginPage
from lemon_12_191209_引入pytest框架.PageObjects.home_page import HomePage
from lemon_12_191209_引入pytest框架.Common import logger
from lemon_12_191209_引入pytest框架.TestDatas import Common_Datas as CD
from lemon_12_191209_引入pytest框架.TestDatas import login_datas as LD

# TODO 在同级py文件conftest中
@pytest.fixture
def init_driver(init):
    lp = LoginPage(init)
    yield {'driver': init, 'lp': lp}


# 模块级别前置后置
@pytest.mark.usefixtures('module_gl')
def test_hello():
    pass

# 绑定这个类下面的测试用例，使用 init_driver 这个前置后置
# @pytest.mark.usefixtures('init_driver')  # 调用里前置 后置
# fixture 的函数名称作为用例的参数 = 返回值
# pytest会自动搜索 fixture 当中，没有同名的fixture 函数，有就拿来用
@pytest.mark.usefixtures('init_driver')
class TestLogin:

    # 正常场景 - 登陆成功。
    @pytest.mark.smoke
    def test_login_success(self, init_driver):
        logging.info("******* 登陆功能 - 正常场景用例：登陆成功 *******")
        # 调用登陆页面的。登陆行为。
        init_driver['lp'].login(LD.success_data["user"], LD.success_data["passwd"])
        # 断言 - 首页当中，应该存在 退出元素。
        assert (HomePage(init_driver['driver']).check_user_exist())
        # 断言2 - url地址  应当为 http://120.78.128.25:8765/Index/index
        assert (init_driver['driver'].current_url == LD.success_data["check_url"])

    # 异常用例 - 用户名为空/密码为空/用户名格式不正确
    @pytest.mark.parametrize('case', LD.wrong_datas)
    def test_login_failed_by_wrongData(self, case, init_driver):
        logging.info("******* 登陆功能 - 异常场景用例：数据格式校验 - 用户名为空/密码为空/用户名格式不正确 *******")
        # 调用登陆页面的。登陆行为。
        init_driver['lp'].login(case["user"], case["passwd"])
        # 断言 - 登陆页面 - 应当现提示信息：请输入手机号
        assert (case["check"] == init_driver['lp'].get_error_msg())

    # 错误的密码
    def test_login_failed_by_wrong_passwd(self, init_driver):
        logging.info("******* 登陆功能 - 异常场景用例：数据后台有效性校验 - 密码错误 *******")
        # 调用登陆页面的。登陆行为。
        init_driver['lp'].login("18684720553", "python11")
        # 断言 - 登陆页面 - 应当现提示信息：帐号或密码错误!
        assert ("帐号或密码错误!" == init_driver['lp'].get_error_msg_from_dialog())

