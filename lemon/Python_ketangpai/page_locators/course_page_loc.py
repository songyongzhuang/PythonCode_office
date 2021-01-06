# --*-- coding : utf-8 --*--
# Project      : Python_ketangpai
# Current file : course_page_loc.py
# Author       : 大壮
# Create time  : 2020-12-21 18:47
# IDE          : PyCharm
# TODO 成长很苦，进步很甜，加油！
from selenium.webdriver.common.by import By
# 调用公共数据，需要用到验证码
from test_datas.common_datas import CommonData as CD


class CoursePageLoc(object):
    """
    登录后，加入课堂需要 定位表达式
    """
    # 课堂派：加入课程按钮   //div[@class='ktcon1 cl clearfix']//div[contains(text(),'加入课程')]
    add_course_button = (By.XPATH, '//div[@class="ktcon1 cl clearfix"]/div[1]')
    # 加入课程弹框：验证码输入框
    verify_code_input = (By.XPATH, '//div[@class="chuangjiankc"]//input[@type="text"]')
    # 加入课程弹框：确定按钮
    confirm_button = (By.XPATH, '//div[@class="chuangjiankc"]//a[@class="btn btn-positive"]')
    # 断言加入课堂成功：提示框  //div[@id="show-tip"]//span  //span[text()="加入课堂成功"]
    prompt_box = (By.XPATH, '//div[@id="show-tip"]//span')

    """ 进入班级 """
    # 进入班级
    enter_course_button = (By.XPATH, f'//a[@data-id="{CD.data_id}"]')
    # 断言班级是否正确，判断课程 id 和 加课码
    course_loc = (By.XPATH, f'//div[@data-id="{CD.data_id}"]//div[text()="{CD.course_verify}"]')

    """ 退课 """
    # 退课第一步：点击更多按钮  更多
    more_button = (By.XPATH, f'//dl[@data-id="{CD.data_id}"]//span[text()=""]')
    # 退课第二步：点击退课按钮
    quit_course_button = (By.XPATH, f'//dl[@data-id="{CD.data_id}"]//a[text()="退课"]')
    # 退课第三步：输入登录密码
    quit_course_input_box = (By.XPATH, '//input[@type="password"]')
    # 退课第四步：点击确定按钮
    quit_course_confirm_button = (By.XPATH, '//div[@class="deletekt"]//a[text()="退课"]')
    # 断言是否退课成功：提示框
    assert_loc = (By.XPATH, '//span[text()="课程退课成功"]')
