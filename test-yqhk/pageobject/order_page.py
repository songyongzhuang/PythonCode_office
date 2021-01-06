# coding=utf-8

from selenium.webdriver.common.by import By


class OrderPage(object):

    def __init__(self, dr):
        self.driver = dr.driver

    # 订单查询
    def order(self):
        element = self.driver.find_element(By.ID, "order")
        return element

    # 订单查询
    def order(self):
        element = self.driver.find_element(By.ID, "order")
        return element
