# -*- coding: utf-8 -*-
import unittest
from page.demo_page import Login
from selenium import webdriver
from time import sleep


class CenpurCommon(unittest.TestCase):
    """
    登录集采平台
    """

    def setUp(self):
        self.name = "123456@123.com"
        self.password = "123456"
        self.url = "https://login.taobao.com/member/login.jhtml"
        self.title = "淘宝网"
        self.driver = webdriver.Chrome()
        self.assert_name = "猪猪"

    # 用例执行体
    def test_taobao_login(self):
        """
        登录淘宝
        """
        login_page = Login(self.driver, self.url, self.title)
        login_page.open()
        # login_page.switch_page_frame()
        sleep(3)
        login_page.click_login_by_password()
        sleep(1)
        login_page.input_login_name(self.name)
        login_page.input_login_password(self.password)
        login_page.submit_login()
        assert self.assert_name in login_page.get_assert_name(), "用户名没有匹配"

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()

