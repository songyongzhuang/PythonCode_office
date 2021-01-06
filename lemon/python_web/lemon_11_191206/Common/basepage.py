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
from lemon_11_191206.Common.dir_config import screenshot_dir
from lemon_11_191206.Common import logger

import logging
import time
import datetime


class BasePage:
    """
    # 包含了PageObjects当中，用到所有的selenium底层方法。
    # 还可以包含通用的一些元素操作，如alert,iframe,windows...
    # 还可以自己额外封装一些web相关的断言
    # 实现日志记录、实现失败截图
    """

    # TODO  driver: WebDriver 声明driver的类型是一个类的对象 (实例化对象)
    def __init__(self, driver: WebDriver):
        self.driver = driver

    # 等待元素可见
    def wait_ele_visible(self, locator, img_doc, timeout=30, poll_fre=0.5):
        """
        :param locator: 元素定位*表达式。(元素定位策略,元素定位表达式)
        :param img_doc: 截图文件的命名部分(说明)。${页面名称_行为名称}_当前的时间.png
        :param timeout: 超时时间
        :param poll_fre: 轮询时间
        :return: None
        """
        logging.info("{} : 等待 {} 元素可见".format(img_doc, locator))
        try:
            # 起始等待的时间 datetime
            start = datetime.datetime.now()
            # TODO visibility_of_element_located 等待元素可见
            WebDriverWait(self.driver, timeout, poll_fre).until(EC.visibility_of_element_located(locator))
        except:
            # 异常信息写入日志
            logging.exception("等待元素可见失败：")  # 级别：Error   tracebak的信息完整的写入日志。
            # 截图 - 只能截取网页图片 - 命名。 页面名称_行为名称_当前的时间.png
            self.save_page_screenshot(img_doc)
            raise
        else:
            # 结束等待的时间
            end = datetime.datetime.now()
            logging.info("等待结束.开始时间为{},结束时间为:{},一共等待耗时为:{}".format(start, end, end - start))

    def wait_page_contains_element(self, locator, img_doc, timeout=30, poll_fre=0.5):
        """
        TODO 等待元素存在
        :param locator: 元素定位*表达式。(元素定位策略,元素定位表达式)
        :param img_doc: 截图文件的命名部分(说明)。${页面名称_行为名称}_当前的时间.png
        :param timeout: 超时时间
        :param poll_fre: 轮询时间
        :return: None
        """
        logging.info("{} : 等待 {} 元素存在".format(img_doc, locator))
        try:
            # 起始等待的时间 datetime
            start = datetime.datetime.now()
            # TODO presence_of_element_located 等待元素可见
            WebDriverWait(self.driver, timeout, poll_fre).until(EC.presence_of_element_located(locator))
        except:
            # 异常信息写入日志
            logging.exception("等待元素存在失败：")  # 级别：Error   tracebak的信息完整的写入日志。
            # 截图 - 命名。 页面名称_行为名称_当前的时间.png
            self.save_page_screenshot(img_doc)
            raise
        else:
            # 结束等待的时间
            end = datetime.datetime.now()
            logging.info("等待结束.开始时间为{},结束时间为:{},一共等待耗时为:{}".format(start, end, end - start))

    def get_element(self, locator, img_doc):
        """
        TODO 查找单个元素
        :param locator: 元素定位*表达式。(元素定位策略,元素定位表达式)
        :param img_doc: 截图文件的命名部分(说明)。${页面名称_行为名称}_当前的时间.png
        :return: None
        """
        logging.info("{} : 查找 {} 元素.".format(img_doc, locator))
        try:
            # 查找元素
            ele = self.driver.find_element(*locator)
        except:
            # 异常信息写入日志
            logging.exception("查找元素失败：")  # 级别：Error   tracebak的信息完整的写入日志。
            # 截图 - 命名。 页面名称_行为名称_当前的时间.png
            self.save_page_screenshot(img_doc)
            raise
        else:
            return ele

    def input_text(self, locator, value, img_doc, timeout=30, poll_fre=0.5):

        """
        TODO 输入操作，
        TODO 1）等待元素可见；2）查找元素；3）输入动作
        :param locator: 定位表达式
        :param value: 输入的文本
        :param locator: 元素定位*表达式。(元素定位策略,元素定位表达式)
        :param img_doc: 截图文件的命名部分(说明)。${页面名称_行为名称}_当前的时间.png
        :param timeout: 超时时间
        :param poll_fre: 轮询时间
        :return: None
        """
        self.wait_ele_visible(locator, img_doc, timeout, poll_fre)
        ele = self.get_element(locator, img_doc)
        logging.info("{}: 对 {} 元素输入文本 {}".format(img_doc, locator, value))
        try:
            ele.send_keys(value)
        except:
            # 异常信息写入日志
            logging.exception("输入文本失败：")  # 级别：Error   tracebak的信息完整的写入日志。
            # 截图 - 命名。 页面名称_行为名称_当前的时间.png
            self.save_page_screenshot(img_doc)
            raise

    def click_element(self, locator, img_doc, timeout=30, poll_fre=0.5):
        """
        TODO 点击元素
        # 1）等待元素可见；2）查找元素；3）点击
        :param locator: 元素定位*表达式。(元素定位策略,元素定位表达式)
        :param img_doc: 截图文件的命名部分(说明)。${页面名称_行为名称}_当前的时间.png
        :param timeout: 超时时间
        :param poll_fre: 轮询时间
        :return: None
        """
        self.wait_ele_visible(locator, img_doc, timeout, poll_fre)
        ele = self.get_element(locator, img_doc)
        logging.info("{}: 点击 {} 元素 ".format(img_doc, locator))
        try:
            # 点击元素
            ele.click()
        except:
            # 异常信息写入日志
            logging.exception("点击操作失败：")  # 级别：Error   tracebak的信息完整的写入日志。
            # 截图 - 命名。 页面名称_行为名称_当前的时间.png
            self.save_page_screenshot(img_doc)
            raise

    def get_element_text(self, locator, img_doc, timeout=30, poll_fre=0.5):
        """
        TODO 获取文本
        # 1）等待元素存在；2）查找元素；3）获取动作
        :param locator: 元素定位*表达式。(元素定位策略,元素定位表达式)
        :param img_doc: 截图文件的命名部分(说明)。${页面名称_行为名称}_当前的时间.png
        :param timeout: 超时时间
        :param poll_fre: 轮询时间
        :return: None
        """
        self.wait_ele_visible(locator, img_doc, timeout, poll_fre)
        ele = self.get_element(locator, img_doc)
        logging.info("{}: 获取 {}  元素的文本内容.".format(img_doc, locator))
        try:
            # 获取 text 文本
            text = ele.text
        except:
            # 异常信息写入日志
            logging.exception("获取元素文本值失败：")  # 级别：Error   tracebak的信息完整的写入日志。
            # 截图 - 命名。 页面名称_行为名称_当前的时间.png
            self.save_page_screenshot(img_doc)
            raise
        else:
            logging.info("获取的文本值为: {}".format(text))
            return text

    def get_element_attribute(self, locator, attr, img_doc, timeout=30, poll_fre=0.5):
        """
        TODO 获取元素属性
        # 1）等待元素存在；2）查找元素；3）获取动作
        :param locator: 元素定位*表达式。(元素定位策略,元素定位表达式)
        :param attr:
        :param img_doc: 截图文件的命名部分(说明)。${页面名称_行为名称}_当前的时间.png
        :param timeout: 超时时间
        :param poll_fre: 轮询时间
        :return: None
        """
        self.wait_page_contains_element(locator, img_doc, timeout, poll_fre)
        ele = self.get_element(locator, img_doc)
        logging.info("{}: 获取 {}  元素的属性 {}.".format(img_doc, locator, attr))
        try:
            value = ele.get_attribute(attr)
        except:
            # 异常信息写入日志
            logging.exception("获取元素属性失败：")  # 级别：Error   tracebak的信息完整的写入日志。
            # 截图 - 命名。 页面名称_行为名称_当前的时间.png
            self.save_page_screenshot(img_doc)
            raise
        else:
            logging.info("获取的属性值为: {}".format(value))
            return value

    def check_element_visible(self, locator, img_doc, timeout=10, poll_fre=0.5):
        """
         TODO 检测元素是否在页面存在且可见。
         如果退出元素存在，则返回True。否则返回False
        :param locator: 元素定位*表达式。(元素定位策略,元素定位表达式)
        :param img_doc: 截图文件的命名部分(说明)。${页面名称_行为名称}_当前的时间.png
        :param timeout: 超时时间
        :param poll_fre: 轮询时间
        :return: 布尔值
        """
        logging.info("{}: 检测元素 {} 存在且可见于页面。".format(img_doc, locator))
        try:
            WebDriverWait(self.driver, timeout, poll_fre).until(EC.visibility_of_element_located(locator))
        except:
            logging.exception(" {}秒内元素在当前页面不可见。".format(timeout))
            self.save_page_screenshot(img_doc)
            return False
        else:
            logging.info(" {}秒内元素可见。".format(timeout))
            return True

    def switch_window(self):
        pass

    def get_current_url(self):
        pass

    def save_page_screenshot(self, img_doc):
        """
        :param img_doc:
        :return:
        """
        # 路径配置文件中引入图片保存路径  + 年月日-时分秒
        #  # 截图 - 命名。 页面名称_行为名称_当前的时间.png
        #  页面_功能_时间.png
        now = time.strftime("%Y-%m-%d %H_%M_%S")
        screenshot_path = screenshot_dir + "/{}_{}.png".format(img_doc, now)
        try:
            self.driver.save_screenshot(screenshot_path)
        except:
            logging.exception("当前网页截图失败")
        else:
            logging.info("截取当前网页成功并存储在: {}".format(screenshot_path))
