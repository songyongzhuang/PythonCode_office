import unittest

import HTMLTestRunnerNew

from 柠檬班作业.lemon_14_190918.优秀作业.case_add import Case_Add
from 柠檬班作业.lemon_14_190918.优秀作业.test_excel import DoExcel

suite = unittest.TestSuite()
t = DoExcel()
test_data = t.do_excel(8, 5, 'testdata.xlsx', 'name')
for item in test_data:
    suite.addTest(Case_Add(item['a'], item['b'], item['c'], item['case_id'], item['description'], 'add_test'))
with open('测试报告.html', 'wb+') as file:
    runner = HTMLTestRunnerNew.HTMLTestRunner(file,
                                              title='加法类测试',
                                              description='unittest',
                                              tester='薛振华')
    runner.run(suite)
