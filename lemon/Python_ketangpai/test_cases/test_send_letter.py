# --*-- coding : utf-8 --*--
# Project      : Python_ketangpai
# Current file : test_send_letter.py
# Author       : 大壮
# Create time  : 2020-12-27 14:06
# IDE          : PyCharm
# TODO 成长很苦，进步很甜，加油！
import pytest
import time
import logging
from selenium import webdriver
# 调用公共数据
from test_datas.common_datas import CommonData as CD
# 专门存放发送私信需要的数据
from test_datas.send_letter_datas import SendLetterData as SLD
# 用来前置<登录课堂派>
from page_objects.login_page import LoginPage
# 调用<元素操作>
from page_objects.send_letter_page import SendLetterPage
# 记录日志/打印日志到控制台/创建日志文件
from common2 import logger


# 前置后置  默认测试用例级别
@pytest.fixture
def init_driver(init):  # 继承同级目录 conf_test 里面的init
    # 登录
    LoginPage(init).login(CD.user, CD.password)
    # 初始化 LoginPage 方便调用
    slp = SendLetterPage(init)
    # yield 返回值, 修改成字典格式
    yield {'driver': init, 'slp': slp}
    # 后置不用写，直接使用继承 init 的后置


@pytest.mark.usefixtures('init_driver')
class TestSendLetter(object):
    """
    发送私信、
    """
    def test_send_letter_success(self, init_driver):
        logging.info('*** 发送私信功能 - 正常登录用例：发送私信成功 ***')
        # 调用发送私信功能操作
        init_driver['slp'].send_letter_course(SLD.send_letter_people, SLD.send_letter_test)
        # 断言 是否发送消息成功
        assert (SLD.send_letter_test == init_driver['slp'].send_letter_test_verify())
