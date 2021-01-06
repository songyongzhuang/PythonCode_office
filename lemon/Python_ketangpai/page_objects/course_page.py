# --*-- coding : utf-8 --*--
# Project      : Python_ketangpai
# Current file : course_page.py
# Author       : 大壮
# Create time  : 2020-12-21 18:47
# IDE          : PyCharm
# TODO 成长很苦，进步很甜，加油！
import time
# 调用 首页操作的定位表达式
from page_locators.course_page_loc import CoursePageLoc as clp
# 调用 基础定位(各种定位元素的方法)
from common2.base_page import BasePage
# 调用公共数据，需要用到验证码
from test_datas.common_datas import CommonData as CD


# 继承 BasePage 可以直接使用它的所有方法，
class CoursePage(BasePage):
    """
    操作加入课程步骤
    """

    def add_course(self):
        """
        加入课程操作
        """
        # 点击加入课程
        self.click_element(clp.add_course_button, '课堂派_加入课程按钮')
        # 加入课程输入框内输入验证码
        self.input_text(clp.verify_code_input, CD.course_verify, '课堂派_加入课程输入验证码')
        # 点击确定按钮，加入课程
        self.click_element(clp.confirm_button, '课堂派_加入课程确定按钮')

    def get_text_hint(self):
        # 获取加入课程成功提示
        return self.get_element_text(clp.prompt_box, '课堂派_加入课程成功提示框')

    def enter_course(self):
        """
        进入班级
        """
        # 点击课程进入班级
        self.click_element(clp.enter_course_button, '课堂派_点击课程进入班级')

    def get_enter_course_loc(self):
        # TODO 获取指定元素文本
        return self.get_element_text(clp.course_loc, '进入班级_获取加课验证码')
        pass

    def quit_course(self):
        """
        退课操作
        """
        # 退课第一步-点击更多按钮
        self.click_element(clp.more_button, '课堂派_退课点击更多', timeout=5)
        # 退课第二步-点击退课按钮
        self.click_element(clp.quit_course_button, '课堂派_退课点击退课')
        # 退课第三步-输入登录密码
        self.input_text(clp.quit_course_input_box, CD.password, '课堂派_退课输入密码')
        # 退课第四步-点击确定按钮
        self.click_element(clp.quit_course_confirm_button, '课堂派_确定退课弹框点击确定')

    def get_quit_course_text_hint(self):
        # 获取退出课堂弹框提示
        return self.get_element_text(clp.assert_loc, '课堂派_课程退课成功弹框')
