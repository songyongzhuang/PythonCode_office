
# --*-- coding : utf-8 --*--
# Project      : python_wed
# Current file : test_invests.py
# Author       : 大壮
# Create time  : 2019-12-15 17:53
# IDE          : PyCharm
# TODO 成长很苦，进步很甜，加油！

import pytest
import logging

from selenium import webdriver
from lemon_PO_quan.Common import logger
from lemon_PO_quan.PageObjects.login_page import LoginPage
from lemon_PO_quan.PageObjects.home_page import HomePage
from lemon_PO_quan.PageObjects.bid_page import BidPage
from lemon_PO_quan.PageObjects.user_page import UserPage
from lemon_PO_quan.TestDatas import Common_Datas as CD
from lemon_PO_quan.TestDatas import invest_datas as ID

# TODO 在同级py文件conftest中
@pytest.fixture
def init_driver(init):
    # 登录
    LoginPage(init).login(CD.user, CD.passwd)
    HomePage(init).click_first_bid()
    bp = BidPage(init)
    yield {'driver': init, 'bp': bp}


@pytest.mark.usefixtures('init_driver')
class TestInvest:

    # 正常场景 - 投资成功
    def test_invest_success(self, init_driver):
        logging.info("******* 投资功能 - 正常场景用例：投资1000元成功。用户可用余额减少1000，标余额减少1000 *******")
        # 3、标页面获取用户余额；
        user_money_before_invest = init_driver['bp'].get_user_money()
        # 4、标页面获取 标的余额；
        bid_money_before_invest = init_driver['bp'].get_bid_left_money()
        # 5、标页面：投标动作；
        init_driver['bp'].invest(ID.success["money"])
        # 6、点击投标成功提示框当中：查看并激活按钮；
        init_driver['bp'] .click_activeButton_on_success_popup()
        # 7、个人页面：获取用户余额；
        user_money_after_invest = UserPage(init_driver['init']).get_user_left_money()
        # 8、回退到标页面、刷新后：再次获取标的余额；
        # 回到上一个页面
        init_driver['init'].back()
        # 刷新页面
        init_driver['init'].refresh()
        # 获取标的余额
        bid_money_after_invest = init_driver['bp'].get_bid_left_money()
        # 9、断言；
        assert (ID.success["money"] == int(float(user_money_before_invest) - float(user_money_after_invest)))
        assert (ID.success["money"] == int((float(bid_money_before_invest) - float(bid_money_after_invest)) * 10000))

    # 异常场景: 数据字段 格式校验 - 弹框提示金额格式不对。
    @pytest.mark.parametrize('invalid_data', ID.invalid_data_format)
    def test_invest_failed_invalid_money(self, invalid_data, init_driver):
        logging.info("******* 投资功能 - 异常场景用例：投资金额有效性校验 - 投资金额为非100的整数倍、错误的格式等 *******")
        # 3、标页面获取用户余额；
        user_money_before_invest = init_driver['bp'].get_user_money()
        # 4、标页面获取 标的余额；
        bid_money_before_invest = init_driver['bp'].get_bid_left_money()
        # 5、标页面：投标动作；
        init_driver['bp'].invest(invalid_data["money"])
        # 6、获取页面提示信息；
        error_msg = init_driver['bp'].get_errorMsg_from_pageCenter()
        # 7、刷新当前页面，获取用户余额、标余额。
        init_driver['init'].refresh()
        user_money_after_invest = init_driver['bp'].get_user_money()
        bid_money_after_invest = init_driver['bp'].get_bid_left_money()
        # 8、断言 - 提示信息是否正确。标的金额不变，用户的余额也不变。
        assert (error_msg == invalid_data["check"])
        assert (user_money_before_invest == user_money_after_invest)
        assert (bid_money_before_invest == bid_money_after_invest)
