#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# datetime:2019/8/16 20:52
# email:936763477@qq.com
# author: 墨墨
# copyright：personal

# 1、在之前定义的手机类下面定义智能手机类和苹果手机类。智能手机打电话具有录音功能。
# 苹果手机打电话不仅具有录音功能，还有 facetime 功能

class MobilePhone(object):
    def __init__(self,brand,type,color):
        self.brand = brand
        self.type = type
        self.color = color
    def callup(self):
        print('我可以打电话')
    def message(self):
        print('我可以发短信')

class SmartPhone(MobilePhone):
    def callup(self):
        super().callup()
        print('我在打电话时还可以录音')

class Iphone(SmartPhone):
    def callup(self):
        super().callup()
        print('我还可以使用FaceTime打电话')

phone = Iphone('苹果','8','粉色')
phone.callup()

############################################

# 2、定义一个 ExcelManual 类。具有获取 sheet 表单， 读取单元格 和 修改单元格功能。
import xlrd
class ExcelManual(object):
    #获取 sheet 表单相关内容
    def get_sht(self,excel_path):
        #根据路径打开Excel
        form = xlrd.open_workbook(excel_path)
        #获取sheet名称
        form.sheet_names()
        #通过索引获取sheet1
        sht = form.sheet_by_index(0)
        #通过表明获取sheet1
        sht1 = form.sheet_by_name(u'sheet1')
        return sht,sht1
    #读取单元格
    def read_cel(self,sheet):
        #获取sheet1的A1单元格的值
        cell_A1 = sheet.cell(0,0).value
        return cell_A1
    #修改单元格
    def amd_cel(self,sheet):
        # 修改单元格A1为：姓名
        sheet.cell(0,0,'姓名')
        return sheet.cell(0,0)

############################################

# 3、 编写一个工具箱类，需要有工具的名称、功能描述、价格，能够添加工具、删除工具、查看工具，
# 并且能获取工具箱中工具的总数。

class ToolKit(object):
    box = []
    def __init__(self,tool_name,function,price,*args):
        self.tool_name = tool_name
        self.function = function
        self.price = price
    def add_tool(self):
        ToolKit.box.append(self.tool_name)
        return ToolKit.box
    def del_tool(self):
        ToolKit.box.remove(self.tool_name)
        return ToolKit.box
    def look_tool(self):
        num = len(ToolKit.box)
        return ToolKit.box,num

shear = ToolKit('剪刀','剪东西','10元')
hammer = ToolKit('锤子','砸东西','15元')
nail = ToolKit('钉子','连接木板','5元')
shear.add_tool()
hammer.add_tool()
print(nail.add_tool())
print(shear.del_tool())
print(f'工具箱目前的工具有{nail.look_tool()[0]}，总数为{nail.look_tool()[1]}')


