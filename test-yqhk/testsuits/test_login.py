import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from framework.publicmethod import login


class TestLogin():

    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)

    def teardown_method(self, method):
        self.driver.quit()

    def test_ss(self):
        self.driver.get("https://oms.test.tebiemiao.cn/")
        login.login(self)
        time.sleep(5)
