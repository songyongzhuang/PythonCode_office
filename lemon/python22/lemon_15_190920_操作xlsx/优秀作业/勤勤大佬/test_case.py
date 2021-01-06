# @Time : 2019/9/22 11:36 
# @Author : ZhangHaiQin
# @File : test_case.py
# @Software: PyCharm
import unittest
from linaxi_15.lianxi_15 import ExcelFun


class ExcelChoice(unittest.TestCase):
    def setUp(self):
        self.excelFun = ExcelFun("C:\柠檬班/demo.xlsx")


    def test_read_sheet_01(self):
        value = self.excelFun.data_cell("Sheet3",1,1)
        self.assertEqual(value,"new_url")

    def test_read_sheet_02(self):
        value = self.excelFun.data_cell("Sheet3",1,1)
        self.assertNotEqual(value,"url")

    def test_read_sheet_03(self):
        value = self.excelFun.data_cell("Sheet3", 1, 1)
        self.assertEqual(value, "new_ur")
    # 测试读取行
    def test_read_row_04(self):
        value1 = self.excelFun.data_row("Sheet3",1)
        self.assertTrue("nihao",value1)

#     读取所有数据

    def test_read_all_05(self):
        value2 = self.excelFun.data_all("Sheet3")
        self.assertTrue("nihao", value2)

    def test_write_06(self):
        self.excelFun.data_write("Sheet3",1,1,"你好")
        value = self.excelFun.data_cell("Sheet3", 1, 1)
        self.assertEqual("你好",value)







if __name__ == '__main__':
    unittest.main()
