# --*-- coding : utf-8 --*--
# Project      : python_lemon_作业
# Current file : lemon_190923_作业.py
# Author       : 大壮
# Create time  : 2019-09-24 23:07
# IDE          : PyCharm
# TODO 成长很苦，进步很甜，加油！
# 0923-配置文件
# 截至：09月25日  18:00展示词云
# 封装配置文件类 ConfigHandler:
# 1,利用上课讲的配置文件操作，去读取配置参数；
# 2,动态修改配置参数。
# 其他觉得需要封装的操作自由发挥。

# 引入解析配置文件库 ConfigParser
import configparser


class ConfigHandler(object):

    def __init__(self, file, mode='w', encoding=None):
        self.config = configparser.ConfigParser()
        self.file = file  # 文件名
        self.mode = mode  # 模式
        self.encoding = encoding  # 编码格式
        # 2、读取配置文件，填写文件名称，编码格式
        self.config.read(self.file, self.encoding)

    def read_file(self, section, option):
        """读取配置参数"""''
        return self.config.get(section, option)

    def read_file_two(self, section, option):
        """get 字典获取"""''
        return self.config[section][option]

    def transition(self, section, option):
        """去除两端字符串"""''
        return eval(self.config.get(section, option))


class Modification(ConfigHandler):

    def amend_file(self, section, option, amend):
        """
        动态修改配置参数, 有就修改，没有就新增
        section 片名
        option 键名
        amend 修改的数据
        """''
        try:
            self.config.set(section, option, amend)
            with open(self.file, self.mode, encoding=self.encoding) as f:
                self.config.write(f)
                return '修改成功'
        except configparser.NoSectionError:
            return'请输入正确的片名'


class Delete(ConfigHandler):
    """ 删除 
    section 片名
    option 键名
    """''
    def delete(self, section, option):
        try:
            self.config.remove_option(section, option)
            with open(self.file, self.mode, encoding=self.encoding) as f:
                self.config.write(f)
                return '删除成功'
        except configparser.NoSectionError:
            return'请输入正确的片名'


config = ConfigHandler(file='./setting.ini', encoding='utf-8')
print('读取配置参数', config.read_file('demo', 'file_name'))  # 读取配置参数
print('字典获取配置参数', config.read_file_two('demo', 'file_name'))  # 字典获取配置参数
print('去除两端字符串', config.transition('demo', 'file_name'))  # 去除两端字符串

# 修改
xiugai = Modification(file='./setting.ini', encoding='utf-8')
print('修改属性的值', xiugai.amend_file('demo', 'age1', '16'))  # 修改属性的值

# 删除
delete = Delete(file='./setting.ini', encoding='utf-8')
print('删除属性', delete.delete('demo', 'age1'))  # 删除属性
