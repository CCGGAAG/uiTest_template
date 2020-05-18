# -*- coding: utf-8 -*-
import unittest
from time import sleep
from page.cenpur_pages.main_page.demo_login_page import LoginPage
from page.cenpur_pages.main_page.main_page import MainPage
from selenium import webdriver


class CenpurCommon(unittest.TestCase):
    """
    登录集采平台
    """

    def setUp(self):
        self.url = ""
        self.account = ""
        self.password = ""
        self.vericode = ""
        self.title = ""
        self.driver = webdriver.Chrome()

    # 用例执行体
    def test_cenpur_login(self):
        """
        登录集采平台
        """

        # 调用打开页面组件
        login_page = LoginPage(self.driver, self.url, self.title)
        login_page.open()
        # 切换iframe
        login_page.change_iframe()
        # 调用用户名输入组件
        login_page.input_username(self.account)
        sleep(2)
        # 调用密码输入组件
        login_page.input_password(self.password)
        sleep(2)
        # 调用验证码输入组件
        login_page.input_vericode(self.vericode)
        sleep(2)
        # 调用点击登录按钮组件
        login_page.click_submit()
        sleep(5)
        # # 查看登录用户信息是否正确
        # login_page.find_username()
        # login_page.input_search("1244444444443")


        sleep(3)

        # 在当前浏览器内打开新页面
        test_main_page = MainPage(self.driver, "http://cenpur-stable-test.bdfint.cn", self.title)
        test_main_page.open()
        test_main_page.input_search("1222222222222")



    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()

