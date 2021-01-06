#!/usr/bin/python3
"""
@File    : basepage.py
@Time    : 2019/12/4 21:54
@Author  : 柠檬班-小简
@Email   : lemonban_simple@qq.com
@Company: 湖南省零檬信息技术有限公司
"""
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
import time


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    # 等待元素可见
    def wait_ele_visible(self, locator, img_doc, timeout=30, poll_fre=0.5):
        """
        :param locator: 元组类型。(元素定位策略,元素定位表达式)
        :param img_doc: 截图文件的命名部分。${页面名称_行为名称}_当前的时间.png
        :param timeout:
        :param poll_fre:
        :return: None
        """
        logging.info("等待 {} 元素可见".format(locator))
        try:
            start = time.time()
            WebDriverWait(self.driver, timeout, poll_fre).until(EC.visibility_of_element_located(locator))
        except:
            # 异常信息写入日志
            logging.exception('')  # 级别：Error   tracebak的信息完整的写入日志。
            # 截图 - 命名。 页面名称_行为名称_当前的时间.png
            # self.save_page_screenshot()

            raise
        else:
            end = time.time()
            duration = (end - start)

    def save_page_screenshot(self, file_name):
        pass
