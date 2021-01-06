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
from selenium.webdriver.remote.webdriver import WebDriver

import logging
import time
import datetime


class BasePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    # 等待元素可见
    def wait_ele_visible(self, locator, img_doc, timeout=30, poll_fre=0.5):
        """
        :param locator: 元组类型。(元素定位策略,元素定位表达式)
        :param img_doc: 截图文件的命名部分。${页面名称_行为名称}_当前的时间.png
        :param timeout:
        :param poll_fre:
        """
        logging.info("等待 {} 元素可见".format(locator))
        try:
            # 等待起始时间 datetime
            start = datetime.datetime.now()
            WebDriverWait(self.driver, timeout, poll_fre).until(EC.visibility_of_element_located(locator))
        except:
            # 异常信息写入日志
            logging.exception('当前元素等待元素可见失败')  # 级别：Error   tracebak的信息完整的写入日志。
            # 截图 - 命名。 页面名称_行为名称_当前的时间.png
            self.save_page_screenshot(img_doc)
            raise
        else:
            # 等待结束时间
            end = datetime.datetime.now()
            logging.info(f'等待结束，开始时间为{start},结束时间为{end}, 一共耗时：{end - start}')

    # 等待元素存在
    def wait_page_contains_element(self, locator, img_doc, timeout=30, poll_fre=0.5):
        logging.info("等待 {} 元素存在".format(locator))
        try:
            # 等待起始时间 datetime
            start = datetime.datetime.now()
            # TODO presence_of_element_located  等待元素存在
            WebDriverWait(self.driver, timeout, poll_fre).until(EC.presence_of_element_located(locator))
        except:
            # 异常信息写入日志
            logging.exception('当前元素等待元素存在失败')  # 级别：Error   tracebak的信息完整的写入日志。
            # 截图 - 命名。 页面名称_行为名称_当前的时间.png
            self.save_page_screenshot(img_doc)
            raise
        else:
            # 等待结束时间
            end = datetime.datetime.now()
            logging.info(f'等待结束，开始时间为{start},结束时间为{end}, 一共耗时：{end - start}')

    # 查找元素
    def get_element(self, locator, img_doc, timeout=30, poll_fre=0.5):
        logging.info(f'查找{locator}元素')
        try:
            ele = self.driver.find_element(*locator)
        except:
            # 异常信息写入日志
            logging.exception(f'查找{locator}元素失败')  # 级别：Error   tracebak的信息完整的写入日志。
            # 截图 - 命名。 页面名称_行为名称_当前的时间.png
            self.save_page_screenshot(img_doc)
            raise
        else:
            return ele

    # 输入操作
    def input_text(self, locator, img_doc, timeout=30, poll_fre=0.5):
        # 1.等待元素可见，2.查找元素，3.输入动作
        self.wait_ele_visible(locator, img_doc, timeout, poll_fre)
        ele = self.get_element(locator, img_doc)
        logging.info(f'输入{locator}元素')
        try:
            ele.send_keys()
        except:  # 异常信息写入日志
            logging.exception(f'查找{locator}元素失败')  # 级别：Error   tracebak的信息完整的写入日志。
            # 截图 - 命名。 页面名称_行为名称_当前的时间.png
            self.save_page_screenshot(img_doc)
            raise

    # 点击
    def click_element(self, locator, img_doc, timeout=30, poll_fre=0.5):
        # 1.等待元素可见，2.查找元素，3.点击动作
        self.wait_ele_visible(locator, img_doc, timeout, poll_fre)
        ele = self.get_element(locator, img_doc)
        logging.info(f'点击{locator}元素')
        try:
            ele.click()  # 点击
        except:  # 异常信息写入日志
            logging.exception(f'查找{locator}元素失败')  # 级别：Error   tracebak的信息完整的写入日志。
            # 截图 - 命名。 页面名称_行为名称_当前的时间.png
            self.save_page_screenshot(img_doc)
            raise

    #

    def save_page_screenshot(self, img_doc):
        """
        截图
        :param img_doc:
        :return:
        """
        # 路径配置文件中引入图片保存路径 + 年月日
        screenshot_path = f'{img_doc}_{""}.png'
        # 只能截取网页截图，其他截不了图
        try:
            self.driver.save_screenshot(screenshot_path)
        except:
            logging.exception('当前网页截图失败')
        else:
            logging.info(f'截取当前网页成功并存储在：{screenshot_path}')
