import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.get("https://www.baidu.com/")
# element = driver.find_element(By.LINK_TEXT, "换一换")
# element = driver.find_element_by_xpath("//span[@class='hot-refresh-text']")
element = driver.find_element(By.XPATH, "//span[contains(text(), '换一换')]")

element.click()
print("22222222222222222222")
