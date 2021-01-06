# -*- encoding: utf-8 -*-

# @Author  :   满满
# @Contact :   867232508@qq.com
# @Software:   PyCharm
# @File    :   config.py
# @Time    :   2019/9/24 12:13
# @Desc    :

"""
封装配置文件类 ConfigHandler:
1,利用上课讲的配置文件操作，去读取配置参数；
2,动态修改日志参数。
其他觉得需要封装的操作自由发挥。
"""
from configparser import RawConfigParser
import os

# 项目根目录位置
base_name = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# conf文件所在目录
conf_loc = os.path.join(base_name, 'conf')


class ConfigHandler:

    def __init__(self, file_name):
        self.conf = RawConfigParser()
        self.file_name = os.path.join(conf_loc, file_name)
        self.conf.read(self.file_name, encoding='utf-8')

    def get_sections(self):
        """获取所有的sections"""
        return self.conf.sections()

    def get_options(self, section):
        """获取section下所有的option"""
        return self.conf.options(section)

    def read(self, section, option):
        """读取section，下option的值"""
        return self.conf.get(section, option)

    def write(self, section, option, value):
        """1、判断该片段是否存在，不存在新增加一个节点
           2、该节点存在的话，如果键存在，更新值
           3、键不存在，新增一个键，并为其赋值
        """
        if not self.conf.has_section(section):
            self.conf.add_section(section)
        self.conf.set(section, option, value)
        with open(self.file_name, 'w', encoding='utf-8') as f:
            self.conf.write(f)

    def return_data(self, section, option):
        """将查询到的数据范围为原类型"""
        result = self.read(section, option)
        return eval(result)


if __name__ == '__main__':
    conf = ConfigHandler('setting.ini')
    print(conf.read('log', 'pattern'))
