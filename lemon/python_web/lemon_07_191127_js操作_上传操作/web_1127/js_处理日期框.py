# --*-- coding : utf-8 --*--
# Project      : python_wed
# Current file : js_处理日期框.py
# Author       : 大壮
# Create time  : 2019-12-01 09:30
# IDE          : PyCharm
# TODO 成长很苦，进步很甜，加油！

"""
1、允许你直接输入日期的。。send_keys()
2、修改readonly属性。

作业：
1、请用selenium的元素定位，不要用js，来实现12306的查票(可选)。
2、请用javascript实现出发地和目的地的选择。
"""
from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://www.12306.cn/index/")

ele = driver.find_element_by_id("train_date")
js = """
// var a = document.getElementById("train_date");
var a = arguments[0]
a.readOnly = false;
a.value = "2019-12-12";
"""
# cur_time = ""

driver.execute_script(js,ele)