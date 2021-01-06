# --*-- coding : utf-8 --*--
# Project      : Python_ketangpai
# Current file : send_letter_page_loc.py
# Author       : 大壮
# Create time  : 2020-12-27 10:05
# IDE          : PyCharm
# TODO 成长很苦，进步很甜，加油！

from selenium.webdriver.common.by import By
# 专门存放发送私信需要的数据
from test_datas.send_letter_datas import SendLetterData as SLD


class SendLetterPageLoc(object):
    """
     私信：发送私信
    """
    # 课堂派首页：点击私信按钮
    schoolmate_button = (By.XPATH, '//div[@class="privateLetter"]//a[@target="_blank"]')

    # 跳转到新窗口

    # 私信页面：搜索学号、姓名  需要先点击再输入
    seek_student_button = (By.XPATH, '//input[@type="text"]')
    # 私信页面：点击搜索的学生姓名
    student_button = (By.XPATH, '//span[@title="郑凯歌2250"]')
    # 私信页面：选择学生私信输入框  需要先点击再输入
    letter_input = (By.XPATH, '//textarea[@class="ps-container"]')
    # 私信页面：点击发送按钮
    send_button = (By.XPATH, '//a[@class="btn btn-positive"]')
    # 断言发送的文字是否一致
    assert_send_test = (By.XPATH, f'//div[text()="{SLD.send_letter_test}"]')
