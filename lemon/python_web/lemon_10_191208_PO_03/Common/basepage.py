# --*-- coding : utf-8 --*--
# Project      : python_wed
# Current file : basepage.py
# Author       : 大壮
# Create time  : 2019-12-05 20:57
# IDE          : PyCharm
# TODO 成长很苦，进步很甜，加油！
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from datetime import datetime  # 时间模块
import time
import os  # 使用os模块获取路径
# TODO 引入封装好的日志
import logging  # 先顶用，到时候换成自己封装的日志
from lemon_10_191208_PO_03.Common.dir_paths import ProjectPath as PP


class BasePage(object):
    """
    1、等待元素可见行为：try 元素可见 except: 失败截图/详细异常信息写入日志
    2、等待元素存在行为：try 元素存在 except: 失败截图/详细异常信息写入日志
    3、查找元素行为：
    4、点击行为(传元素定位表达式)：1）等待元素可见；2）查找元素；3）点击
    5、输入行为(传元素定位表达式)：1）等待元素可见；2）查找元素；3）输入动作
    6、获取元素文本(传元素定位表达式)：1）等待元素存在；2）查找元素；3）输入动作
    7、获取元素属性(传元素定位表达式)：1）等待元素存在；2）查找元素；3）输入动作
    """

    def __init__(self, driver: WebDriver):
        self.driver = driver

    # 等待元素可见
    def wait_ele_visible(self, locator, img_doc, timeout=30, poll_fre=0.5):
        """
        :param locator: 元组类型，(元素定位策略, 元素定位表达式)
        :param img_doc: 截图的文件命名部分  页面名称_行为名称_当前时间.png
        :param timeout: 等待时间
        :param poll_fre: 轮询周期
        :return:
        """
        logging.info(f'等待{locator}元素可见')
        try:
            # TODO 记录查找元素开始时间
            start = time.time()
            WebDriverWait(self.driver, timeout, poll_fre).until(EC.visibility_of_element_located(locator))
        except:
            # TODO 异常信息写入日志
            logging.exception('')  # 级别：Error tracebak 控制台信息完整的写入日志
            # 截图 - 命名- 页面名称_行为名称_当前时间.png
            self.save_page_screenshot(img_doc)
            raise  # 手动抛出异常：raise 触发异常后，后面的代码就不会再执行
        else:
            # TODO 记录查找元素结束时间
            end = time.time()
            # TODO 计算等待多少秒，转换成秒
            duration = (end - start)
            logging.info(f'等待结束, 开始时间为{start},结束时间为{end},一共等待耗时为{duration},')

    # TODO 等待元素存在
    def wait_page_contains_element(self, locator, img_doc, timeout=30, poll_fre=0.5):
        logging.info(f'等待{locator}元素存在')
        try:
            #  记录查找元素开始时间
            start = time.time()
            WebDriverWait(self.driver, timeout, poll_fre).until(EC.presence_of_element_located(locator))
        except:
            # TODO 异常信息写入日志
            logging.exception('')  # 级别：Error tracebak 控制台信息完整的写入日志
            # 截图 - 命名- 页面名称_行为名称_当前时间.png
            self.save_page_screenshot(img_doc)
            raise  # 手动抛出异常：raise 触发异常后，后面的代码就不会再执行
        else:
            #  记录查找元素结束时间
            end = time.time()
            #  计算等待多少秒，转换成秒
            duration = (end - start)
            logging.info(f'等待结束, 开始时间为{start},结束时间为{end},一共等待耗时为{duration},')

    def get_element(self, locator, img_doc):
        """
        # 查找元素
        :param locator:传递的定位表达式，查找的元素
        :param img_doc:图片的说明，页面名称
        :return:
        """
        logging.info(f'查找{locator}元素。')
        try:
            ele = self.driver.find_element(*locator)
        except:
            # TODO 异常信息写入日志
            logging.exception('')  # 级别：Error tracebak 控制台信息完整的写入日志
            # 截图 - 命名- 页面名称_行为名称_当前时间.png
            self.save_page_screenshot(img_doc)
            raise  # 手动抛出异常：raise 触发异常后，后面的代码就不会再执行
        else:
            return ele

    def imput_text(self, locator, value, img_doc, timeout=30, poll_fre=0.5):
        """
        TODO 输入行为(传元素定位表达式)：1）等待元素可见；2）查找元素；3）输入动作
        :param locator:传递的定位表达式，查找的元素
        :param img_doc:截图，图片的说明，页面名称
        :param value:输入的内容
        :param timeout: 等待时间
        :param poll_fre: 查找间隔
        :return:
        """
        self.wait_ele_visible(locator, img_doc, timeout, poll_fre)
        ele = self.get_element(locator, img_doc)
        logging.info(f'对{locator}元素输入文本：{value}')
        try:
            ele.send_keys(value)
        except:
            # TODO 异常信息写入日志
            logging.exception('')  # 级别：Error tracebak 控制台信息完整的写入日志
            # 截图 - 命名- 页面名称_行为名称_当前时间.png
            self.save_page_screenshot(img_doc)
            raise  # 手动抛出异常：raise 触发异常后，后面的代码就不会再执行
        else:
            return ele

    def click_element(self, locator, img_doc, timeout=30, poll_fre=0.5):
        """
        TODO 点击行为(传元素定位表达式)：1）等待元素可见；2）查找元素；3）点击
        :param locator: 传递的定位表达式，查找的元素
        :param img_doc: 截图，图片的说明，页面名称
        :param timeout:
        :param poll_fre:
        :return:
        """
        self.wait_ele_visible(locator, img_doc, timeout, poll_fre)
        ele = self.get_element(locator, img_doc)
        logging.info(f'点击{locator}元素。')
        try:
            ele.click()
        except:
            # TODO 异常信息写入日志
            logging.exception('')  # 级别：Error tracebak 控制台信息完整的写入日志
            # 截图 - 命名- 页面名称_行为名称_当前时间.png
            self.save_page_screenshot(img_doc)
            raise  # 手动抛出异常：raise 触发异常后，后面的代码就不会再执行

    def get_element_text(self, locator, img_doc):
        # TODO 获取元素文本(传元素定位表达式)：1）等待元素存在；2）查找元素；3）输入动作
        self.wait_page_contains_element(locator, img_doc)
        ele = self.get_element(locator, img_doc)
        logging.info(f'获取{locator}元素文本内容。')
        try:
            text = ele.text
        except:
            # TODO 异常信息写入日志
            logging.exception('')  # 级别：Error tracebak 控制台信息完整的写入日志
            # 截图 - 命名- 页面名称_行为名称_当前时间.png
            self.save_page_screenshot(img_doc)
            raise  # 手动抛出异常：raise 触发异常后，后面的代码就不会再执行
        else:
            logging.info(f'获取文本值为{text}.')
            return text

    def get_element_attribute(self, locator, attr, img_doc, timeout=30, poll_fre=0.5):
        # TODO 获取元素属性(传元素定位表达式)：1）等待元素存在；2）查找元素；3）输入动作
        self.wait_page_contains_element(locator, img_doc, timeout, poll_fre)
        ele = self.get_element(locator, img_doc)
        logging.info(f'获取{locator}元素属性{attr}.')
        try:
            value = ele.get_attribute(attr)
        except:
            # TODO 异常信息写入日志
            logging.exception('')  # 级别：Error tracebak 控制台信息完整的写入日志
            # 截图 - 命名- 页面名称_行为名称_当前时间.png
            self.save_page_screenshot(img_doc)
            raise  # 手动抛出异常：raise 触发异常后，后面的代码就不会再执行
        else:
            logging.info(f'获取{locator}元素属性值为：{value}.')
            return value

    def save_page_screenshot(self, img_doc):
        """
        :param img_doc: 图片名称
        :return:
        """
        # 路径配置文件中引入图片保存路径, 注意问题命名格式 不要写 ‘:’
        # 截图 - 命名- 页面名称_行为名称_当前时间.png
        time_str = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')  # 时间
        screenshot_path = f'{img_doc}_{time_str}.png'  # 图片名称
        picture = os.path.join(PP.SCREENSHOT_PATH, screenshot_path)  # 图片路径加名称
        logging.info(f'截取当前网页并存储在：{picture}')
        try:
            # save_screenshot 只能保存网页的截图
            self.driver.save_screenshot(screenshot_path)
        except:  # 失败
            logging.exception('当前网页截图失败')
        else:  # 成功
            logging.info(f'截取当前网页成功并存储在：{screenshot_path}')

    def cut_new_window(self):
        # 切换到新窗口：1、sleep 2秒，2、获取窗口列表，3、切换到最好一个
        pass

    def acquire_url(self):
        # 获取url
        pass
