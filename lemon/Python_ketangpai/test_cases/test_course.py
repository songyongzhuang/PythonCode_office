# --*-- coding : utf-8 --*--
# Project      : Python_ketangpai
# Current file : test_course.py
# Author       : 大壮
# Create time  : 2020-12-21 18:44
# IDE          : PyCharm
# TODO 成长很苦，进步很甜，加油！
import pytest
import logging
import time

# 调用 浏览器
from selenium import webdriver
# 调用公共数据
from test_datas.common_datas import CommonData as CD
# 用来前置<登录课堂派>
from page_objects.login_page import LoginPage
# 调用<课程相关元素操作>
from page_objects.course_page import CoursePage
# 记录日志/打印日志到控制台/创建日志文件
from common2 import logger


# 前置后置  默认测试用例级别
@pytest.fixture
def init_driver(init):  # 继承同级目录 conf_test 里面的init
    # 登录
    LoginPage(init).login(CD.user, CD.password)
    # 初始化 LoginPage 方便调用
    cp = CoursePage(init)
    # yield 返回值, 修改成字典格式
    yield {'driver': init, 'cp': cp}
    # 后置不用写，直接使用继承 init 的后置


@pytest.mark.usefixtures('init_driver')
class TestCourse(object):
    """
    登录课堂派，加入课程
    """

    def test_quit_course_success(self, init_driver):
        logging.info('*** 课程退课功能 - 正常登录用例：课程退课成功 ***')
        # 调用 课程退课 功能操作
        init_driver['cp'].quit_course()
        # 断言 课程退课功能
        assert ('课程退课成功' == init_driver['cp'].get_quit_course_text_hint())

    def test_add_course_success(self, init_driver):
        logging.info('*** 加入课程功能 - 正常登录用例：加入课程成功 ***')
        # 调用 加入课堂 功能操作
        init_driver['cp'].add_course()
        # 断言 加入课堂操作
        assert ('加入课堂成功' == init_driver['cp'].get_text_hint())

    def test_enter_course_success(self, init_driver):
        logging.info('*** 进入班级功能 - 正常登录用例：进入班级成功 ***')
        # 调用 进入班级 功能操作
        init_driver['cp'].enter_course()
        time.sleep(0.5)
        # 断言 1、比对进入班级后的url地址
        assert (init_driver['driver'].current_url == CD.enter_course_url)
        # 回到上一个页面
        # init_driver['init'].back()
        # 刷新页面
        # init_driver['init'].refresh()
