# --*-- coding : utf-8 --*--
# Project      : Python_ketangpai
# Current file : test_login.py
# Author       : 大壮
# Create time  : 2020-12-21 13:34
# IDE          : PyCharm
# TODO 成长很苦，进步很甜，加油！
import pytest
import logging
import time

# 记录日志/打印日志到控制台/创建日志文件
from common2 import logger
# 导包元素操作，
from page_objects.login_page import LoginPage
# TODO 待定写退出登录
# 导入 存放登录页面的数据
from test_datas import login_datas as LD


# 前置后置  默认测试用例级别
@pytest.fixture
def init_driver(init):  # 继承同级目录 conf_test 里面的init
    # 初始化 LoginPage 方便调用
    lp = LoginPage(init)
    # yield 返回值, 修改成字典格式
    yield {'driver': init, 'lp': lp}
    # 后置不用写，直接使用继承 init 的后置


# 绑定这个类下面的测试用例，使用 init_driver 这个前置后置
# @pytest.mark.usefixtures('init_driver')  # 调用 init_driver 里前置 后置
# fixture 的函数名称作为用例的参数 = 返回值
# pytest会自动搜索 fixture 当中，没有同名的 fixture 函数，有就拿来用
@pytest.mark.usefixtures('init_driver')
class TestLogin(object):

    # TODO   @pytest.mark.smoke   一会了解这是什么意思
    def test_login_success(self, init_driver):
        """
        正常场景 -- 登录成功
        :param init_driver: 使用前置后置的返回值
        :return:
        """
        logging.info('*** 登录功能 - 正常登录用例：登录成功 ***')
        # 调用登录页面的登录行为、传入账号，密码
        init_driver['lp'].login(LD.correct_data['account'], LD.correct_data['password'])
        time.sleep(0.5)
        # 断言 URL地址   current_url：获取当前url地址
        assert (init_driver['driver'].current_url == LD.correct_data['check_url'])

    # py_test 数据驱动
    @pytest.mark.parametrize('case', LD.wrong_data)
    def test_login_failed(self, case, init_driver):
        """
        异常用例 - 用户名不能为空/密码不能为空
        :param case: 数据驱动，使用 LD.wrong_data 传递的参数
        :param init_driver: 使用前置后置的返回值
        :return:
        """
        logging.info("*** 登陆功能 - 异常用例 - 用户名不能为空/密码不能为空 ***")
        # 调用登录页面的登录行为、传入账号，密码
        init_driver['lp'].login(case["account"], case["password"])
        # 断言 - 登陆页面 - 应当现提示信息：请输入手机号
        assert (case["check"] == init_driver['lp'].get_error_hint())
