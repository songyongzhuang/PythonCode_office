# --*-- coding : utf-8 --*--
# Project      : Python_ketangpai
# Current file : send_letter_page.py
# Author       : 大壮
# Create time  : 2020-12-27 12:57
# IDE          : PyCharm
# TODO 成长很苦，进步很甜，加油！
import time
# 调用 首页操作的定位表达式
from page_locators.send_letter_page_loc import SendLetterPageLoc as SPL
# 调用 基础定位(各种定位元素的方法)
from common2.base_page import BasePage


# 继承 BasePage 可以直接使用它的所有方法，
class SendLetterPage(BasePage):
    """
    发送私信
    """

    def send_letter_course(self, student, word):
        """
        发送私信操作
        :param student: 传入搜索学生
        :param word: 传入发送的消息
        :return:
        """
        # 课堂派首页：点击私信按钮
        self.click_element(SPL.schoolmate_button, '课堂派首页_点击私信按钮')
        # 跳转到新窗口
        self.switch_new_window()
        # 私信页面：搜索学号、姓名  需要先点击再输入
        self.click_element(SPL.seek_student_button, '私信页面_点击搜索学号姓名')
        self.input_text(SPL.seek_student_button, student, '私信页面_输入学号姓名')
        # 私信页面：点击搜索的学生姓名
        self.click_element(SPL.student_button, '课堂派首页_点击搜索的学生姓名')
        # 私信页面：选择学生私信输入框
        self.click_element(SPL.letter_input, '私信页面_点击学生私信输入框')
        self.input_text(SPL.letter_input, word, '私信页面_输入数据到学生私信输入框')
        # 私信页面：点击发送按钮
        self.click_element(SPL.send_button, '私信页面_点击发送按钮')

    def send_letter_test_verify(self):
        # 获取聊天输入框的第一个数据 文本，用来判断发送成功
        return self.get_element_text(SPL.assert_send_test, '聊天窗口_判断数据是否发送成功')
