# coding=utf-8

from selenium.webdriver.common.by import By


class MenusPage(object):

    def __init__(self, dr):
        self.driver = dr.driver

    def menusBar(self):
        element = self.driver.find_element(By.ID, "MenusBar")
        return element

    # el-tabs__header
    def header(self):
        element = MenusPage.menusBar(self).find_element(By.CSS_SELECTOR, ".el-tabs__header")
        return element

    def header_order(self):
        element = MenusPage.header(self).find_element(By.XPATH, "//span[contains(text(), '订单')]")
        return element

    # el-tabs__content
    def content(self):
        element = MenusPage.menusBar(self).find_element(By.CSS_SELECTOR, ".el-tabs__content")
        return element

    def content_order(self):
        element = MenusPage.content(self).find_element(By.ID, "pane-订单")
        return element

    def content_order_ddjy(self):
        element = MenusPage.content_order(self).find_element(By.XPATH, "//*[contains(text(), '订单交易')]")
        return element

    def content_order_ddjy_ddcx(self):
        element = MenusPage.content_order(self).find_element(By.XPATH, "//*[contains(text(), '订单查询')]")
        return element

    def content_order_ddcl(self):
        element = MenusPage.content_order(self).find_element(By.XPATH, "//*[contains(text(), '订单处理')]")
        return element

    def content_order_ddcl_tkwq(self):
        element = MenusPage.content_order(self).find_element(By.XPATH, "//*[contains(text(), '退款维权')]")
        return element

    def content_order_ddcl_plfh(self):
        element = MenusPage.content_order(self).find_element(By.XPATH, "//*[contains(text(), '批量发货')]")
        return element
