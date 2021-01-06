# -*- coding:utf-8 -*-

from configparser import ConfigParser, NoSectionError, NoOptionError
import os

dir_name = os.path.dirname(os.path.abspath(__file__))  # 获取当前文件夹地址
config_name = os.path.join(dir_name, "config.ini")  # 拼接配置文件


class ConfigHandler:
    """封装配置文件类"""

    # 初始化实例变量
    def __init__(self):
        self.cf = ConfigParser()  # 实例类
        self.cf.read(config_name, encoding="utf-8")  # 读取配置文件

    # 读取配置文件的option对应的值
    def read_option(self, section, option):
        try:
            self.cf.has_section(section)
            self.cf.has_option(section, option)
            option_value = self.cf.get(section, option)
            return option_value
        except NoSectionError as e:
            print("数据错误{}".format(e))
        except NoOptionError as er:
            print("数据错误{}".format(er))


if __name__ == "__main__":  # 测试类
    config = ConfigHandler()  # 创建实例
    print(config.read_option("Level", "debug"))  # 测试类方法
