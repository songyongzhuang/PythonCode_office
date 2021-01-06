#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# datetime:2019/9/20 18:21
# email: wagyu2016@163.com
# author: 雨泽
# copyright: 湖南省零檬信息技术有限公司

# object 是所有类的父类
class Phone(object):

    def __init__(self):
        print("正在初始化")

    def call(self, phone_num):
        """打电话"""
        print("手机正在给  {} 打电话".format(phone_num))

class SmartPhone(Phone):

    def call(self, phone_num, record=True):
        """电话"""
        # Phone().call(phone_num)
        super().call(phone_num)
        if record == True:
            self.record()

    def record(self):
        """录音,封装强迫症"""
        print("手机正在录音")

class Iphone(SmartPhone):
    def call(self, phone_num, record=True, faced=False):
        """电话"""
        super().call(phone_num, record)
        if faced == True:
            self.face_time()

    def face_time(self):
        """视频"""
        print("正在视频")


# 初始化
# phone = Phone()
# phone.call('五五')

# 初始化智能手机
# smart_phone = SmartPhone()
# smart_phone.call('困了睡觉', record=False)

iphone = Iphone()
iphone.call('132', faced=False)


"""
ExcelManual
类。具有获取
sheet
表单， 读取单元格
和
修改单元格功能
"""


class ExcelManual:
    def __init__(self, file_path):
        self.file_path = file_path

    def open(self):
        """打开Excel"""
        print("打开文件{}".format(self.file_path))

    def get_sheet(self, sheet_name):
        """获取sheet表单"""
        print('获取表单')

    def get_cell(self, read_row, column):
        """获取单元格"""
        self.get_sheet('')

    def update_cell(self, write_row, column, data):
        self.get_cell(write_row, column)
        print("修改数据为{}".format(data))


# 实际参数是否是重合