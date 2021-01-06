# --*-- coding : utf-8 --*--
# Project      : Python_ketangpai
# Current file : job_page_loc.py
# Author       : 大壮
# Create time  : 2020-12-26 17:28
# IDE          : PyCharm
# TODO 成长很苦，进步很甜，加油！
from selenium.webdriver.common.by import By


class JobPageLoc(object):
    """
    传作业、作业留言、查看作业提交状态 定位表达式
    """
    # 进入课堂页面：作业按钮
    job_button = (By.XPATH, '//div[@id="third-nav"]//a[text()="作业"]')
    # 打开作业页面：上传作业按钮 TODO 22期：MDAwMDAwMDAwMLSsrZaHqbtt 练习：MDAwMDAwMDAwMLScz5mHqa9s
    uploading_button = (By.XPATH, '//div[@data-id="MDAwMDAwMDAwMLScz5mHqa9s"]//a[@class="sc-btn"]')
    # 提交作业页面：添加作业文件
    submit_job_button = (By.XPATH, '//a[@class="sc-btn webuploader-container"]')
    # 提交作业页面：作业留言输入框 先点击，在输入
    job_leave_word_button = (By.XPATH, '//div[@id="mess1"]//span[@class="s2"]')
    job_leave_word_input = (By.XPATH, '//textarea[@id="comment"]')
    # 提交作业页面：作业留言保存按钮
    leave_word_save_button = (By.XPATH, '//div[@class="work-message2 clearfix"]//a')
    # 提交作业页面：提交作业按钮
    submit_button = (By.XPATH, '//div[@class="work-message2 clearfix"]//a')

    # 提交作业页面：作业提交成功提示框
    succeed_hint_text = (By.XPATH, '//div[@class="weui_dialog_bd"]')
    # 提交作业页面：作业提交成功提示框点击我知道了
    got_it_button = (By.XPATH, '//a[@class="weui_btn_dialog primary"]')
    # 断言 提交作业页面： 按钮文字是否是 ‘更新提交’
    update_submit_button = (By.XPATH, '//div[@class="sc-tj fl"]//a[@class="new-tj1"]')

    # 判断已经交作业
    judge = (By.XPATH, '//div[@class="work-new-r fl "]//a')
