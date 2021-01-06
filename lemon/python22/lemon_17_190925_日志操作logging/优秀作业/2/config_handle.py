# -*- coding:UTF-8 -*-
# @Time     : 2019/9/25 16:17
# @Author   : yizizhiyue
# @Email    : yizizhiyue@qq.com
# @File     : homework_0923.py
# @Software : PyCharm

from configparser import ConfigParser, NoOptionError, NoSectionError


class ConfigHandler:
    def __init__(self, file_name):
        self.file_name = file_name
        conf = ConfigParser()
        conf.read(file_name, encoding='utf-8')
        self.conf = conf

    def get(self, section, option):
        '''获取具体的值'''
        try:
            return self.conf.get(section, option)
        except NoSectionError as e:
            print(e)
        except NoOptionError as e:
            print(e)

    def get_sections(self):
        '''读取sections'''
        return self.conf.sections()

    def get_opotions(self, section_name):
        '''读取options'''
        return self.conf.options(section_name)

    def get_structure(self):
        '''读取配置文件的section-option结构'''
        all = []
        # 遍历所有的分区section
        for sec in self.conf.sections():
            opt_value = []
            # 遍历所有的分区section
            for opt in self.conf.options(sec):
                opt_value.append(opt)
            all.append({sec: opt_value})
        return all

    def add_section(self, section=None):
        '''添加section结构'''
        if not self.conf.has_section(section):
            self.conf.add_section(section)
            # 保存conf到配置文件中去
            with open(self.file_name, 'w', encoding='utf-8') as file:
                self.conf.write(file)

    def set_section_and_value(self, section=None, option=None, value=None):
        '''添加section结构、以及对应的options值'''
        if not self.conf.has_section(section):
            self.conf.add_section(section)
        # 设置值
        self.conf[section][option] = value
        # 保存conf到配置文件中去
        with open(self.file_name, 'w', encoding='utf-8') as file:
            self.conf.write(file)
















