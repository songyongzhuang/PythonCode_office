# --*-- coding : utf-8 --*--
# Project      : Python_ketangpai
# Current file : test_job.py
# Author       : 大壮
# Create time  : 2020-12-26 18:50
# IDE          : PyCharm
# TODO 成长很苦，进步很甜，加油！
import pytest
import time
import logging
# 调用公共数据
from test_datas.common_datas import CommonData as CD
# 调用专门存放作业相关的数据
from test_datas.job_datas import JobDatas as JD
# 用来前置<登录课堂派>
from page_objects.login_page import LoginPage
# 用来前置<进入班级>
from page_objects.course_page import CoursePage
# 调用<元素操作>
from page_objects.job_page import JobPage
# 记录日志/打印日志到控制台/创建日志文件
from common2 import logger


# 前置后置  默认测试用例级别
@pytest.fixture
def init_driver(init):  # 继承同级目录 conf_test 里面的init
    # 登录
    LoginPage(init).login(CD.user, CD.password)
    # 进入班级
    CoursePage(init).enter_course()
    # 初始化 LoginPage 方便调用
    uj = JobPage(init)
    # yield 返回值, 修改成字典格式
    yield {'driver': init, 'uj': uj}
    # 后置不用写，直接使用继承 init 的后置


@pytest.mark.usefixtures('init_driver')
class TestCourse(object):
    """
    作业：上传作业、作业留言、查看作业提交状态
    """

    def test_uploading_jod_success(self, init_driver):
        logging.info('*** 上传作业 - 正常登录用例：上传成功 ***')
        # 调用 上传作业、作业留言 功能操作
        init_driver['uj'].uploading_job_course()
        # 断言
        assert (JD.hint_data == init_driver['uj'].update_submit())

    def test_examine_job_state(self, init_driver):
        logging.info('*** 查看作业提交状态 - 查看作业提交状态 ***')
        # 调用 查看作业提交状态
        init_driver['uj'].examine_job_state()
        # 断言 查看作业提交状态
        assert (JD.submit_state_data == init_driver['uj'].gain_text())
