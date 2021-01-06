# --*-- coding : utf-8 --*--
# Project      : Python_ketangpai
# Current file : base_page.py
# Author       : 大壮
# Create time  : 2020/12/19 15:33
# IDE          : PyCharm
# TODO 成长很苦，进步很甜，加油！

"""
框架底层的定位表达
"""
# 日志
import logging
# 定义的日志  相当重要的那，要不不记录日志
from common2 import logger
# 显示等待
from selenium.webdriver.support.wait import WebDriverWait
# 判断元素  元素是否可见？ 存在？
from selenium.webdriver.support import expected_conditions as EC
# 操纵浏览器功能
from selenium.webdriver.remote.webdriver import WebDriver
# 对时间日期的多种多样的处理方式  实例：https://blog.csdn.net/python3_2017/article/details/78983370
import time
import os
import datetime
# 项目路径 截图用
from common2.dir_path import DirPath
# 只处理Windows的上传、下载
import win32gui
import win32con


class BasePage(object):
    """
    基础定位
    自己额外封装一些web相关的断言
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
        # ****** logging.info 生成日志记录 ******
        logging.info(f'{img_doc}：等待{locator}元素可见')
        # 异常处理
        try:
            # 起始等待的时间 datetime
            start = datetime.datetime.now()
            # 等待元素可见
            WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll_frequency). \
                until(EC.visibility_of_element_located(locator))
        # except：出现异常进入except
        except Exception:
            # 异常信息写入日志
            # 级别：Error  -- traceback(追溯)的信息完整的写入日志
            # # 异常信息写入日志   ***  *** exception 常规错误的基类
            logging.exception(f'等待{locator}元素可见失败')
            # 截图 -- 只能截取网页图片，命名格式：页面名称_行为名称_当前时间.png
            # 调用自己封装的截图/命名
            self.save_page_screenshot(img_doc)
            raise  # 手动抛出异常
        # else：操作成功会运行else下面的代码
        else:
            # 结束等待时间
            end = datetime.datetime.now()
            # *** logging.info 生成日志记录 ***
            logging.info(f'等待结束.开始时间为{start},结束时间为:{end},一共等待耗时为:{start - end}')

    def wait_element_exist(self, locator, img_doc, timeout=30, poll_frequency=0.5):
        """
        ****** 等待元素存在 ******
        :param locator: 元素定位*表达式。(元素定位策略,元素定位表达式)
        :param img_doc: 截图文件的命名部分(说明)。${页面名称_行为名称}_当前的时间.png
        :param timeout: 超时时间，超过时间就报错，截图
        :param poll_frequency: 轮询时间
        :return: None
        """
        logging.info(f'{img_doc}：等待{locator}元素存在')
        try:
            # 记录元素开始时间
            start = datetime.datetime.now()
            # *** 等待元素存在 presence_of_element_located ***
            WebDriverWait(self.driver, timeout, poll_frequency).until(EC.presence_of_element_located(locator))
        except Exception:
            # 异常信息写入日志
            logging.exception(f'等待元素存在失败：{locator}')
            # 截图 - 命名格式：页面名称_行为名称_当前时间.png
            self.save_page_screenshot(img_doc)
            raise  # 手动抛出异常
        else:
            # 结束等待时间
            end = datetime.datetime.now()
            logging.info(f'等待结束.开始时间为{start},结束时间为:{end},一共等待耗时为:{start - end}')

    def get_element(self, locator, img_doc):
        """
        ****** 查找单个元素 ******
        :param locator: 元素定位*表达式。(元素定位策略,元素定位表达式)
        :param img_doc: 截图文件的命名部分(说明)。${页面名称_行为名称}_当前的时间.png
        :return:
        """
        logging.info(f'{img_doc}：等待{locator}元素存在')
        try:
            # 查找元素
            # find_element 需要两值，第一个是定位方法，第二个是定位表达式
            ele = self.driver.find_element(*locator)
        except Exception:
            # 异常信息写入日志
            logging.exception(f'查找元素失败: {locator}')
            # 截图 - 命名格式：页面名称_行为名称_当前时间.png
            self.save_page_screenshot(img_doc)
            raise  # 手动抛出异常
        else:
            # 成功 把找到的元素返回
            return ele

    def input_text(self, locator, value, img_doc, timeout=30, poll_frequency=0.5):
        """
         ****** 输入操作 ******
         步骤：1）等待元素可见；2）查找元素；3）输入动作
        :param locator: 元素定位*表达式。(元素定位策略,元素定位表达式)
        :param value: 输入的文本内容(值)
        :param img_doc: 截图文件的命名部分(说明)。${页面名称_行为名称}_当前的时间.png
        :param timeout: 超时时间，超过时间就报错，截图
        :param poll_frequency: 轮询时间
        :return:
        """
        # 调用《等待元素可见》 传入：定位表达式、页面名称_行为名称、超时时间、轮询时间
        self.wait_element_visible(locator, img_doc, timeout, poll_frequency)
        # 调用《查找单个元素》 传入：定位表达式、页面名称_行为名称
        ele = self.get_element(locator, img_doc)
        logging.info(f'{img_doc}：等待{locator}元素输入文本：{value}')
        try:
            # 输入
            ele.send_keys(value)
        except Exception:
            # 异常信息写入日志
            logging.exception(f'{locator}输入文本失败{value}')
            # 截图 - 命名格式：页面名称_行为名称_当前时间.png
            self.save_page_screenshot(img_doc)
            raise  # 手动抛出异常

    def click_element(self, locator, img_doc, timeout=30, poll_frequency=0.5):
        """
         ****** 点击元素 ******
         步骤：1）等待元素可见；2）查找元素；3）点击
        :param locator: 元素定位*表达式。(元素定位策略,元素定位表达式)
        :param img_doc: 截图文件的命名部分(说明)。${页面名称_行为名称}_当前的时间.png
        :param timeout: 超时时间，超过时间就报错，截图
        :param poll_frequency: 轮询时间
        :return:
        """
        # 调用《等待元素可见》 传入：定位表达式、页面名称_行为名称、超时时间、轮询时间
        self.wait_element_visible(locator, img_doc, timeout, poll_frequency)
        # 调用《查找单个元素》 传入：定位表达式、页面名称_行为名称
        ele = self.get_element(locator, img_doc)
        logging.info(f'{img_doc}：等待{locator}元素点击')
        try:
            # 点击
            ele.click()
        except Exception:
            # 异常信息写入日志
            logging.exception(f'{locator}元素点击失败')
            # 截图 - 命名。 页面名称_行为名称_当前的时间.png
            self.save_page_screenshot(img_doc)
            raise  # 手动抛出异常

    def get_element_text(self, locator, img_doc, timeout=30, poll_frequency=0.5):
        """
        ****** 获取文本 ******
         步骤：1）等待元素存在；2）查找元素；3）获取动作
        :param locator: 元素定位*表达式。(元素定位策略,元素定位表达式)
        :param img_doc: 截图文件的命名部分(说明)。${页面名称_行为名称}_当前的时间.png
        :param timeout: 超时时间，超过时间就报错，截图
        :param poll_frequency: 轮询时间
        :return:
        """
        # 调用《等待元素可见》 传入：定位表达式、页面名称_行为名称、超时时间、轮询时间
        self.wait_element_exist(locator, img_doc, timeout, poll_frequency)
        # 调用《查找单个元素》 传入：定位表达式、页面名称_行为名称
        ele = self.get_element(locator, img_doc)
        logging.info(f'{img_doc}：获取{locator}元素的文本值')
        try:
            #  ****** 获取元素文本 ******
            text = ele.text
        except Exception:
            # 异常信息写入日志
            logging.exception(f'获取{locator}元素的文本值失败')
            # 截图 - 命名。 页面名称_行为名称_当前的时间.png
            self.save_page_screenshot(img_doc)
            raise  # 手动抛出异常
        else:
            logging.info(f'获取{locator}元素的文本值为：{text}')
            return text

    def get_element_attribute(self, locator, attr, img_doc, timeout=30, poll_frequency=0.5):
        """
        ****** 获取元素属性 ******
         步骤：1）等待元素存在；2）查找元素；3）获取动作
        :param locator: 元素定位*表达式。(元素定位策略,元素定位表达式)
        :param attr: 需要获取属性的元素
        :param img_doc: 截图文件的命名部分(说明)。${页面名称_行为名称}_当前的时间.png
        :param timeout: 超时时间，超过时间就报错，截图
        :param poll_frequency: 轮询时间
        :return:
        """
        # 调用《等待存在》 传入：定位表达式、页面名称_行为名称、超时时间、轮询时间 ***(存在非可见)***
        self.wait_element_exist(locator, img_doc, timeout, poll_frequency)
        # 调用《查找单个元素》 传入：定位表达式、页面名称_行为名称
        ele = self.get_element(locator, img_doc)
        logging.info(f'{img_doc}：获取{locator}元素的{attr}属性')
        try:
            # *** 获取元素属性 ***
            value = ele.get_attribute(attr)
        except Exception:
            # 异常信息写入日志
            logging.exception("获取元素属性失败：")  # 级别：Error   tracebak的信息完整的写入日志。
            # 截图 - 命名。 页面名称_行为名称_当前的时间.png
            self.save_page_screenshot(img_doc)
            raise  # 手动抛出异常
        else:
            logging.info(f'获取元素{logging}属性值为{value}')
            return value

    def check_element_visible(self, locator, img_doc, timeout=30, poll_frequency=0.5):
        """
         ****** 检测元素是否在页面存在且可见 ******
         如果退出元素出现，则返回True, 否则返回False
        :param locator: 元素定位*表达式。(元素定位策略,元素定位表达式)
        :param img_doc: 截图文件的命名部分(说明)。${页面名称_行为名称}_当前的时间.png
        :param timeout: 超时时间，超过时间就报错，截图
        :param poll_frequency: 轮询时间
        :return: 返回 布尔值
        """
        logging.info(f'{img_doc}: 检测元素{locator}, 存在并且可见于页面')
        try:
            # 判断元素可见
            WebDriverWait(self.driver, timeout, poll_frequency).until(EC.visibility_of_element_located(locator))
        except:
            # 异常信息写入日志
            logging.exception(f'{timeout}秒内元素{locator}在页面不可见')
            # 截图 - 命名。 页面名称_行为名称_当前的时间.png
            self.save_page_screenshot(img_doc)
            return False
        else:
            logging.info(f'{timeout}秒内元素{locator}在页面可见')
            return True

    def switch_new_window(self):
        """
        ****** 切换到新窗口 ******
        :return:
        """
        # 等待新窗口出现
        time.sleep(1)  # 强制等待
        wins = self.driver.window_handles
        logging.info(f'当前的窗口{wins}')
        print("当前的窗口句柄是：", wins)
        # 切换到 新窗口
        self.driver.switch_to.window(wins[-1])
        time.sleep(1)  # 强制等待
        pass

    def scroll_bar_jianyiban(self, locator, img_doc):
        """
        ****** 滚动条操作简易版 - 不需要预加载的页面 ******
        :param locator: 元素定位*表达式。(元素定位策略,元素定位表达式) 例如：(By.XPATH, '//*[@id="J_top"]/div[1]/a/h3')
        :param img_doc: 截图文件的命名部分(说明)。${页面名称_行为名称}_当前的时间.png
        :return:
        """
        time.sleep(1)  # 强制等待
        logging.info(f'滚动条操作-{img_doc}：等待{locator}元素存在')
        try:
            # 找到要滚动的元素
            #  判断元素是否存在
            WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(locator))
        except:
            # 异常信息写入日志
            logging.exception("滚动条失败,未找到元素")  # 级别：Error   tracebak的信息完整的写入日志。
            # 截图 - 命名。 页面名称_行为名称_当前的时间.png
            self.save_page_screenshot(img_doc)
            raise  # 手动抛出异常
        else:
            ele = self.driver.find_element(*locator)
            # 先滚动到可视区域后
            # 参数一、 javacript 脚本， 参数二、传给 js 脚本的参数
            # js 脚本用 arguments 接受外部的参数
            # arguments 是列表，外部传递的列表， 只传递了一个值【0】
            # js 脚本中 用 scrollIntoView() 自动滚动到可视区域
            self.driver.execute_script("arguments[0].scrollIntoView()", ele)
            self.driver.find_element(*locator).click()
            logging.info(f'滚动条 - {img_doc}元素{locator}找到并点击')
            # scrollIntoView() 默认与页面顶部对齐
            # scrollIntoView(false) 页面底部对齐

    def scroll_bar(self, locator, img_doc):
        """
        ****** 滚动条操作 - 高级用来处理预加载网页 如：京东淘宝首页 ******
        :param locator: 元素定位*表达式。(元素定位策略,元素定位表达式) 例如：(By.XPATH, '//*[@id="J_top"]/div[1]/a/h3')
        :param img_doc: 截图文件的命名部分(说明)。${页面名称_行为名称}_当前的时间.png
        :return:
        """
        time.sleep(1)  # 强制等待

        logging.info(f'{img_doc}：等待{locator}元素存在')
        # # 获取当前的窗口大小。整个窗口的高和宽。
        # win_size = driver.get_window_size()
        # 窗口有window.outerHeight(包含工具栏和滚动条),window.innerHeight(不包含工具栏和滚动条,仅内容可视区域)
        # 获取当前窗口的内容可视区域
        inner_height = self.driver.execute_script("var a = window.innerHeight;return a;")
        print("当前窗口的内容可视区域-高度：", inner_height)

        # 获取当前整个html页面的body高度。
        body_height = self.driver.execute_script("var a = document.body.scrollHeight;return a;")
        print("当前整个html页面的body-高度:", body_height)

        scrolled_height = 0
        new_body_height = body_height  # 当前整个html页面的body高度
        old_body_height = 0
        break_flag = False
        while new_body_height != old_body_height:
            distance = int((new_body_height - scrolled_height) / (inner_height * 0.5)) + 1
            for i in range(distance):
                # 滚动距离为 窗口内容可视区域的百分之50.可灵活配置哦！
                self.driver.execute_script("var a = window.innerHeight;window.scrollBy(0,a*0.5);")
                # 滚动一次，页面内容会更新一部分。在滚动之后，查找当前页面是否包含了它。如果没有，继续滚动。如果有，退出。
                try:
                    WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
                except:
                    print("滚动失败,没有找到请检查滚动条定位或者其他原因")
                    # 异常信息写入日志
                    # 级别：Error  -- traceback(追溯)的信息完整的写入日志
                    # # 异常信息写入日志   ***  *** exception 常规错误的基类
                    logging.exception(f'等待{locator}元素滚动可见失败')
                    # 截图 -- 只能截取网页图片，命名格式：页面名称_行为名称_当前时间.png
                    # 调用自己封装的截图/命名
                    self.save_page_screenshot(img_doc)
                    raise  # 手动抛出异常
                else:
                    print("找到啦！！！")
                    logging.info(f'获取滚动条元素{logging}属性')
                    self.driver.find_element(*locator).click()
                    break_flag = True  # 终止for循环
                    break
            if break_flag is True:  # 终止While循环
                break
                # time.sleep(3)
            # 更新滚动
            old_body_height = new_body_height
            scrolled_height = new_body_height
            # 获取当前整个html页面的body高度
            new_body_height = self.driver.execute_script("var a = document.body.scrollHeight;return a;")
            print("老 - 当前整个html页面的body-高度:", old_body_height)
            print("新 - 当前整个html页面的body-高度:", new_body_height)

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
            logging.info(f'截取当前网页成功并存储在: {screenshots_path}')

    # 声明他是静态方法
    @staticmethod
    def upload_file(filePath, browser_type="chrome"):
        """
        ******《上传文件》 Windows 窗口 ******
        :param filePath: 传入文件路径 绝对路径 包括文件名称
        :param browser_type: 浏览器默认 chrome(谷歌)

        # Edit - ComboBox - ComboBoxEx32 - #32770
        # 找到输入框和打开按钮 元素；2、输入地址，点击打开。
        # 前提 ：windows上传窗口已经出现。sleep1-2秒等待弹出的出现。
        """
        # 等待 Windows 窗口出现
        time.sleep(2)  # 强制等待
        # 这个是判断的浏览器，不同的浏览器上传的 title(标题头) 是不一样的
        if browser_type == "chrome":
            title = "打开"
        else:
            title = ""

        # 找元素
        # 一级窗口 顶级窗口"#32770","打开"
        dialog = win32gui.FindWindow("#32770", title)
        # FindWindowEx 在爸爸的基础上找后代，1、爸爸是谁. 2、0. 3、找什么类型的后代. 4、有文本写文本，没有文体写 None
        ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, "ComboBoxEx32", None)  # 二级
        comboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, "ComboBox", None)  # 三级
        # 编辑按钮
        edit = win32gui.FindWindowEx(comboBox, 0, 'Edit', None)  # 四级
        # 打开按钮
        button = win32gui.FindWindowEx(dialog, 0, 'Button', "打开(&O)")  # 二级
        # 往编辑当中，输入文件路径 。
        win32gui.SendMessage(edit, win32con.WM_SETTEXT, None, filePath)  # 发送文件路径
        win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)  # 点击打开按钮

    # 声明他是静态方法
    @staticmethod
    def export_file(filePath, browser_type="chrome"):
        """
        《导出文件》 Windows 窗口
        :param filePath: 传入文件路径 绝对路径 例如："E:\WebWebpageTest\酒店商品销售明细表.xls"
        :param browser_type: 浏览器默认 chrome(谷歌)

        # Edit - ComboBox - ComboBoxEx32 - #32770
        # 找到输入框和打开按钮 元素；2、输入地址，点击打开。
        # 前提 ：windows上传窗口已经出现。sleep1-2秒等待弹出的出现。
        """
        # 等待 Windows 窗口出现
        time.sleep(2)  # 强制等待
        # 这个是判断的浏览器，不同的浏览器上传的 title(标题头) 是不一样的
        if browser_type == "chrome":
            title = "另存为"
        else:
            title = ""
        # 找元素
        # 一级窗口 顶级窗口"#32770","打开"
        dialog = win32gui.FindWindow("#32770", title)  # 一级
        # FindWindowEx 在爸爸的基础上找后代，1、爸爸是谁. 2、0. 3、找什么类型的后代. 4、有文本写文本，没有文体写 None
        DUIViewWndClassName = win32gui.FindWindowEx(dialog, 0, "DUIViewWndClassName", None)  # 三级
        DirectUIHWND = win32gui.FindWindowEx(DUIViewWndClassName, 0, "DirectUIHWND", None)  # 四级
        FloatNotifySink = win32gui.FindWindowEx(DirectUIHWND, 0, "FloatNotifySink", None)  # 五级
        ComboBox = win32gui.FindWindowEx(FloatNotifySink, 0, "ComboBox", None)  # 六级
        # 编辑存储路径
        Edit = win32gui.FindWindowEx(ComboBox, 0, 'Edit', None)  # 七级
        # 保存按钮
        button = win32gui.FindWindowEx(dialog, 0, 'Button', "保存(&S)")  # 二级
        # 往编辑当中，输入文件路径 。
        win32gui.SendMessage(Edit, win32con.WM_SETTEXT, None, filePath)  # 发送文件路径
        win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)  # 点击保存按钮
