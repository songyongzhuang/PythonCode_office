#-*- coding:utf-8 -*-
# datetime:2019/9/23
# author: jiayuan

from configparser import ConfigParser
from configparser import RawConfigParser
'''
0923-配置文件
截止时间：09月25日18:00
封装配置文件类 ConfigHandler:
1,利用上课讲的配置文件操作，去读取配置参数；
2,动态修改配置参数。
其他觉得需要封装的操作自由发挥。

'''
class ProfileTool:
    def __init__(self,file_name):
        self.file_name = file_name
        # 实例化配置对象
        con = RawConfigParser()
        # 读取配置文件
        con.read(file_name,encoding='utf-8')
        # 将con变为实例属性
        self.config = con

    # 获取指定section及option对应的值并转换成功相应类型
    def read(self,section,option):
        value = None
        # 判断如果section 和option都存在再进行取值，反之返回None
        if self.config.has_option(section,option):
            # 获取指定片段对应key的值
            value = self.config.get(section,option)
        return value

    # 获取指定section下所有键值对
    def reads(self,section):
        values = []
        # 判断如果文件中无section，返回空列表
        if self.config.has_section(section):
            values = self.config.items(section)
        return values

    # 和excel不一样，不用静态也不会出问题，config是独立的？
    def write(self,section,option,data):
        # 判断录入section不存在则新增
        if not self.config.has_section(section):
            self.config.add_section(section)
        # 写入值
        self.config.set(section,option,data)
        with open(self.file_name,'w',encoding='utf-8') as f:
            self.config.write(f)

if __name__ == '__main__':
    pro = ProfileTool("./setting.ini")
    print(pro.read('FileHandler','fmt'))
    pro.write('data','id','编号')