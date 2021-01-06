import unittest

from 柠檬班作业.lemon_14_190918_测试框架_unittest.优秀作业.test_excel import DoExcel
from 柠檬班作业.lemon_14_190918_测试框架_unittest.优秀作业.test_math import TestAdd


class Case_Add(unittest.TestCase):

    def __init__(self, a, b, c, case_id, title, methodName):
        super(Case_Add,self).__init__(methodName)
        self.a = a
        self.b = b
        self.c = c
        self.title = title
        self.case_id = case_id

    def setUp(self):
        print('测试开始了')
        print('您现在执行的测试用例是{}'.format(self.title))
        print('您输入的以一个值是{}，第二个值是{}，预期结果是{}'.format(self.a, self.b, self.c))
        self.t = TestAdd()
        self.wb = DoExcel()

    def add_test(self):
        res = self.t.math_add(self.a, self.b)
        try:
            self.assertEqual(self.c, res)
            ifpass = 'PASS'
        except AssertionError as e:
            print('测试出错了')
            ifpass = 'FALL'
            raise e
        finally:
            self.wb.write_back('testdata.xlsx', 'name', self.case_id+1, res, ifpass)
            print('您得到的结果是{}'.format(res))

    def tearDown(self):
        print('测试结束了')
