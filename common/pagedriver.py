# -*- coding:utf-8 -*-
import time
import os
from PIL import ImageGrab
from selenium.common.exceptions import *
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from common.log import Logger

auto_log = Logger()


class Action(object):
    """
     Action封装所有页面都公用的方法，例如driver, url ，FindElement等
    """
    # 初始化driver、url、title等
    def __init__(self, driver, page_url, page_title):
        self.page_url = page_url
        self.page_title = page_title
        self.driver = driver
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)

    def _open(self, page_url, page_title):
        """
        打开页面，校验页面链接是否加载正确
        """
        # 使用get打开访问链接地址
        self.driver.get(page_url)
        auto_log.info("打开网址：%s" % page_url)
        auto_log.info("网址预期标题: %s" % page_title)
        # 使用assert进行校验，打开的链接地址是否与配置的地址一致。调用on_page()方法
        assert self.on_page(page_title), u"打开页面%s失败" % page_url

    def open(self):
        """
        定义open方法，调用_open()进行打开链接
        """
        self._open(self.page_url, self.page_title)

    def find_element(self, *locator):
        """
        定位单个元素
        return self.driver.find_element(*locator)
        """
        try:
            WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element(*locator).is_displayed())
            auto_log.info("定位元素:%s" % (locator,))
            return self.driver.find_element(*locator)
        except Exception as msg:
            auto_log.error(u"%s 页面中未能找到 %s 元素" % (self, locator))
            auto_log.error("错误信息%s" % msg)
            # auto_log.debug(self.get_html_source())

    def find_elements(self, *locator):
        """
        定位多个元素
        """
        try:
            WebDriverWait(self.driver, 10).until(lambda driver: driver.find_elements(*locator).is_displayed())
            auto_log.info("定位元素:%s" % (locator,))
            return self.driver.find_elements(*locator)
        except Exception as msg:
            auto_log.error(u"%s 页面中未能找到 %s 元素" % (self, locator))
            auto_log.error("错误信息%s" % msg)

    def switch_frame(self, locator):
        """
        重写switch_frame方法
        """
        auto_log.info("切换frame：%s" % (locator,))
        return self.driver.switch_to.frame(locator)

    def switch_default_frame(self):
        """
        切换回主default_content
        """
        auto_log.info("切换default_frame")
        return self.driver.switch_to.default_content()

    def on_page(self, page_title):
        """
        使用current_url获取当前窗口Url地址，进行与配置地址作比较，返回比较结果（True False）
        """
        return page_title in self.driver.title

    def script(self, src):
        """
        定义script方法，用于执行js脚本，范围执行结果
        """
        self.driver.execute_script(src)

    def send_keys(self, locator, value, clear_first=True):
        """
        重写定义send_keys方法
        """
        try:
            locator = getattr(self, "_%s" % locator)
            if clear_first:
                self.find_element(*locator).clear()
                self.find_element(*locator).send_keys(value)
                auto_log.info("输入值：%s" % value)
            else:
                self.find_element(*locator).click()
        except Exception as msg:
            auto_log.error(u"%s 页面中未能找到 %s 元素" % (self, locator))
            auto_log.error("错误信息%s" % msg)

    def is_text_in_element(self, locator, text, timeout=10):
        """
        判断文本在元素里,没定位到元素返回False
        result = driver.is_text_in_element(locator, text)
        """
        try:
            result = WebDriverWait(self.driver, timeout, 1).until(EC.text_to_be_present_in_element(locator, text))
        except TimeoutException:
            auto_log.info("元素无法在：" + str(locator) + "中定位，或者 链接超时，请检查网络")
            return False
        else:
            return result

    def move_to_element(self, locator):
        """
        鼠标悬停操作
        Usage:
        locator = ("id","xxx")
        driver.move_to_element(locator)
        """
        element = self.find_element(locator)
        ActionChains(self.driver).move_to_element(element).perform()

    def scroll_to_lowest(self):
        """
        移动到浏览器底端
        """
        js = "window.scrollTo(0,document.body.scrollHeight)"
        self.driver.execute_script(js)

    def is_element_exist(self, element_name):
        """
        判断元素是否存在
        """
        try:
            self.find_element(element_name)
        except NoSuchElementException:
            return False
        return True

    def current_window_handle(self):
        """
        获取当前窗口句柄
        :return:
        """
        return self.driver.current_window_handle

    def all_window_handles(self):
        """
        获取所有（all）窗口的句柄
        :return:
        """
        return self.driver.window_handles

    def switch_to_single_window(self):
        all_handles = self.driver.window_handles
        for handle in all_handles:
            self.driver.switch_to.window(handle)

    def switch_window(self):
        now_handle = self.driver.current_window_handle
        all_handles = self.driver.window_handles
        for handle in all_handles:
            if handle is not now_handle:
                self.driver.switch_to.window(handle)
        return self.driver.current_window_handle

    def js_Change_tag_properties(self, locator, attribute_name, attribute_value):
        """
        使用js脚本运行,改变元素标签的属性值
        locator:标签定位
        attribute_name：属性名称
        attribute_value:属性值
        """
        js_statement = "arguments[0].%s='%s'" % (attribute_name, attribute_value)
        element = self.find_element(locator)
        self.driver.execute_script(js_statement, element)

    def execute_js_script(self, locator, file_path):
        """
        支持JavaScript脚本运行，实现上传文件
        """
        self.js_Change_tag_properties(locator, "display", "block")
        self.driver.find_element(locator).send_keys(file_path)

    def get_screenshot(self):
        """
        获取截图
        修改：配置路径待完成
        """
        now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        path = os.path.abspath('../..')
        get_file_path()
        pic_path = path + '\\report\\%s.png' % now
        self.driver.save_screenshot(pic_path)

    def get_cookies(self):
        """
        获取当前浏览器cookie
        :return:
        """
        return self.driver.get_cookies()

    def add_cookies(self, cookie_dic):
        """添加cookie到浏览器"""
        self.driver.add_cookie(cookie_dic)

    def pictureshot():
        """
        第三方方法获取截图
        :return:
        """
        im = ImageGrab.grab()
        now = time.strftime("%Y-%m-%d %H_%M_%S")
        img_name = os.path.abspath('..') + "\\report\\" + now + ".jpeg"
        im.save(img_name)

    def get_html_source(self):
        source = self.driver.page_source
        auto_log.info(source)
        return source