# --*-- coding ：utf-8 --*--
# Project      ：python22_web
# Current file ：bid_page.py
# Author       ：Administrator猜猜猜
# Create time  ：2019/12/05 11:52
# IDE          ：PyCharm
# TODO 成长很苦, 进步很甜, 加油！
from lemon_10_191208_PO_03.PageLocators.login_page_loc import LoginPageLoc as loc
# 继承
from lemon_10_191208_PO_03.Common.basepage import BasePage


class BidPage(BasePage):

    def click_bid(self):
        """
        点击投标
        :return:
        """
        # 点击登陆
        self.click_element(loc.invest_loc, '点击投标按钮')

    def get_bid_left_money(self):
        """
        获取标的余额
        :return: 
        """''
        pass

    def get_user_left_money(self):
        """
        获取去用户余额
        :return: 
        """''
        pass

    def invest(self, money):
        """
        投标
        :param money: 
        :return: 
        """''
        pass

