# --*-- coding : utf-8 --*--
# Project      : test-yqhk-Project
# Current file : base_page.py
# Author       : 菜鸟一号
# Create time  : 2020-12-07 17:47
# IDE          : PyCharm
# MAIL         : 邮箱地址
# TODO 成长很苦，进步很甜，加油！

"""
框架底层的定位表达
"""
from framework.dir_path import DirPath
# 日志
import logging
# 定义的日志
from framework import logger
# 显示等待
from selenium.webdriver.support.wait import WebDriverWait
# 判断元素
from selenium.webdriver.support import expected_conditions as EC
# 操纵浏览器功能
from selenium.webdriver.remote.webdriver import WebDriver
# 对时间日期的多种多样的处理方式  实例：https://blog.csdn.net/python3_2017/article/details/78983370
import time
import os
import datetime


class BasePage(object):
    """
    基础定位
    自己额外封装一些web相关的
    """

    #  driver: WebDriver 声明driver的类型是一个类的对象 (实例化对象)
    #  声明的类型  driver就可以点出 WebDriver 的方法
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def wait_element_visible(self, locator, img_doc, timeout=30, poll_frequency=0.5):
        """
        ****** 等待元素可见 ******
        :param locator: 元素定位*表达式。(元素定位策略,元素定位表达式)
        :param img_doc: 截图文件的命名部分(说明)。${页面名称_行为名称}_当前的时间.png
        :param timeout: 超时时间，超过时间就报错，截图.
        :param poll_frequency: 轮询时间
        :return: None
        """
        # ****** logging.debug 生成日志记录 ******
        logging.debug(f'{img_doc}：等待元素可见')
        try:
            # 起始等待的时间 datetime
            start = datetime.datetime.now()
            # 等待元素可见
            WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll_frequency). \
                until(EC.visibility_of_element_located(locator))
        except Exception:
            logging.exception(f'等待元素可见失败{img_doc}')
            self.save_page_screenshot(img_doc)
            raise
        else:
            # 结束等待时间
            end = datetime.datetime.now()
            logging.debug(f'等待结束.开始时间为{start},结束时间为:{end},一共等待耗时为:{start - end}')

    def wait_element_exist(self, locator, img_doc, timeout=30, poll_frequency=0.5):
        """
        ****** 等待元素存在 ******
        """
        logging.debug(f'{img_doc}：等待元素存在')
        try:
            # 记录元素开始时间
            start = datetime.datetime.now()
            # *** 等待元素存在 presence_of_element_located ***
            WebDriverWait(self.driver, timeout, poll_frequency).until(EC.presence_of_element_located(locator))
        except Exception:
            logging.exception(f'等待元素存在失败{img_doc}')
            self.save_page_screenshot(img_doc)
            raise
        else:
            # 结束等待时间
            end = datetime.datetime.now()
            logging.debug(f'等待结束.开始时间为{start},结束时间为:{end},一共等待耗时为:{start - end}')

    def get_element(self, locator, img_doc):
        """
        ****** 查找单个元素 ******
        """
        logging.debug(f'{img_doc}：等待元素存在')
        try:
            # 查找元素
            # find_element 需要两值，第一个是定位方法，第二个是定位表达式
            ele = self.driver.find_element(*locator)
        except Exception:
            logging.exception(f'查找元素失败: {img_doc}')
            self.save_page_screenshot(img_doc)
            raise
        else:
            return ele

    def input_text(self, locator, value, img_doc, timeout=30, poll_frequency=0.5):
        """
         ****** 输入操作 ******
        """
        # 调用《等待元素可见》 传入：定位表达式、页面名称_行为名称、超时时间、轮询时间
        self.wait_element_visible(locator, img_doc, timeout, poll_frequency)
        ele = self.get_element(locator, img_doc)
        logging.debug(f'{img_doc}：等待元素输入文本：{value}')
        try:
            # 输入
            ele.send_keys(value)
        except Exception:
            logging.exception(f'输入文本失败{value}')
            self.save_page_screenshot(img_doc)
            raise

    def click_element(self, locator, img_doc, timeout=30, poll_frequency=0.5):
        """
         ****** 点击元素 ******
        """
        # 调用《等待元素可见》 传入：定位表达式、页面名称_行为名称、超时时间、轮询时间
        self.wait_element_visible(locator, img_doc, timeout, poll_frequency)
        ele = self.get_element(locator, img_doc)
        logging.debug(f'{img_doc}：等待元素点击')
        try:
            ele.click()
        except Exception:
            # 异常信息写入日志
            logging.exception(f'{img_doc}元素点击失败')
            self.save_page_screenshot(img_doc)
            raise

    def save_page_screenshot(self, img_doc):
        """
        ********* 网页截图 *********
        :param img_doc: 路径配置 (传入具体哪个页面什么操作)
        # 路径配置文件中引入图片保存路径  + 年月日-时分秒
        #  # 截图 - 命名。 页面名称_行为名称_当前的时间.png
        #  页面_功能_时间.png
        """

        now = time.strftime('%Y-%m-%d %H-%M-%S')
        screenshots_path = os.path.join(DirPath.screenshot_dir, f'{img_doc}_{now}.png')
        try:
            self.driver.save_screenshot(screenshots_path)
        except:
            logging.exception('当前网页截图失败')
        else:
            logging.debug(f'截取当前网页成功并存储在: {screenshots_path}')
