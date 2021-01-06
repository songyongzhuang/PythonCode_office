# --*-- coding : utf-8 --*--
# Project      : python_web
# Current file : 京东02.py
# Author       : 大壮
# Create time  : 2020-03-18 17:19
# IDE          : PyCharm
# TODO 成长很苦，进步很甜，加油！
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
driver.implicitly_wait(5)
driver.maximize_window()
ele = driver.find_element_by_id('kw')
ele.send_keys("京东商城", Keys.ENTER)
loc = (By.XPATH, '//a[contains(text(),"正品低价、品质保障")]')
WebDriverWait(driver, 20).until(EC.visibility_of_element_located(loc))
driver.find_element(*loc).click()
win = driver.window_handles
driver.switch_to.window(win[-1])
lo = (By.XPATH, '//h3[text()="逛好店"]')

while True:
    js = """
            var a = window.innerHeight;
            window.scrollBy(0, a*0.5);
    """
    driver.execute_script(js)
    try:
        WebDriverWait(driver, 3, 0.5).until(EC.visibility_of_element_located(lo))
        driver.find_element(*lo).click()
    except:
        pass
    else:
        break
