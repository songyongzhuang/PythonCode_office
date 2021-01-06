#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# author:muji
# datetime:2019/6/17 16:51
"""

2、在之前定义的手机类下面定义智能手机类和苹果手机类。智能手机打电话具有录音功能。 苹果手机打电话不仅具有录音功能，还有 facetime 功能

"""


# class Phone:
#
#     def __init__(self, color):
#         self.color = color
#
#     def call(self):
#         print("正在打电话")
#
#
# class SmartPhone(Phone):
#
#     def call(self,record=False):
#         # 重写和超继承
#         super().call()
#         if record:
#             self.record()
#         # print("正在打电话")
#
#     def record(self):
#         print('正在录音')
#
#
# class ApplePhone(SmartPhone):
#     def call(self,record=False, face_time=False):
#         super().call(record)
#         if face_time:
#             self.face_time()
#
#     def face_time(self):
#         print("正在 facetime")
#
#
# apple = ApplePhone('red')
# apple.call(record=True, face_time=True)


"""
3、定义一个 ExcelManual 类。具有获取 sheet 表单， 读取单元格 和 修改单元格功能。
"""


class ExcelManual:
    def __init__(self, path):
        self.path = path

    def sheets(self):
        """获取所有表单"""
        pass

    def open(self):
        print("正在打开文件{}".format(self.path))

    def close(self):
        print("正在关闭文件{}".format(self.path))

    def save(self):
        print("正在保存")

    def sheet_by_name(self, name):
        print("获取 sheet {}".format(name))

    def sheet_by_index(self, index):
        pass

    def read_cell(self,row, column):
        pass

    def chage_cell(self):
        pass


# workbook 工作簿
# sheet 表单，表格
# cell 单元格
# row  行
# column  列
# openpyxl
# [['baidu','yuze', '1'], ['douban', 'shoushou', '2']]


class Qiongren:

    def attack(self, furen):
        print("正在攻击 {}".format(furen))


class Furen:

    def attack(self, qiongren):
        print("正在攻击 {}".format(qiongren))


qr = Qiongren()
fr = Furen()

qr.attack(fr)
