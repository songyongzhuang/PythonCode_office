# --*-- coding : utf-8 --*--
# Project      : Python_ketangpai
# Current file : job_page.py
# Author       : 大壮
# Create time  : 2020-12-26 18:17
# IDE          : PyCharm
# TODO 成长很苦，进步很甜，加油！
import time
# 调用 首页操作的定位表达式
from page_locators.job_page_loc import JobPageLoc as JL
# 调用 基础定位(各种定位元素的方法)
from common2.base_page import BasePage
# 调用专门存放作业相关的数据
from test_datas.job_datas import JobDatas as JD
from test_cases import conftest


# 继承 BasePage 可以直接使用它的所有方法，
class JobPage(BasePage):
    """
    传作业、作业留言、查看作业提交状态 定位表达式
    """

    def uploading_job_course(self):
        """
        上传作业
        """
        # 进入课堂页面：点击作业按钮
        self.click_element(JL.job_button, '课堂页面_点击作业按钮')
        # 打开作业页面：点击上传作业按钮
        self.click_element(JL.uploading_button, '作业页面_点击上传作业按钮')
        # 提交作业页面：点击添加作业文件
        self.click_element(JL.submit_job_button, '作业页面_点击添加作业文件')
        # 上传文件
        time.sleep(1)
        self.upload_file(JD.uploading_file_data)
        time.sleep(0.5)
        # 提交作业页面：作业留言输入框 先点击，在输入
        self.click_element(JL.job_leave_word_button, '作业页面_点击作业留言输入框')
        self.input_text(JL.job_leave_word_input, JD.job_leave_word_data, '作业页面_输入作业留言输入框')
        # 提交作业页面：点击保存留言按钮
        self.click_element(JL.leave_word_save_button, '作业页面_点击保存留言按钮')
        # 提交作业页面：点击作业提交按钮
        self.click_element(JL.submit_button, '作业页面_点击作业提交按钮')
        # 提交作业页面：点击我知道了按钮
        self.click_element(JL.got_it_button, '提交作业页面_点击我知道了按钮')

    def update_submit(self):
        # 获取 更新提交按钮 文本值
        return self.get_element_text(JL.update_submit_button, '提交作业页面_更新提交按钮')

    def examine_job_state(self):
        # 进入课堂页面：点击作业按钮
        self.click_element(JL.job_button, '课堂页面_点击作业按钮')

    def gain_text(self):
        # 获取文本值
        return self.get_element_text(JL.judge, '作业页面_提交按钮')
