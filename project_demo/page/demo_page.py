from common.pagedriver import Action


class Login(Action):

    # 元素的定位地址或者测试数据
    frame_loc = 0
    link_login_by_password_loc = ("xpath", "//*[@id='J_QRCodeLogin']/div[5]/a[1]")
    input_name_loc = ("id", "TPL_username_1")
    input_password_loc = ("id", "TPL_password_1")
    submit_login_loc = ("id", "J_SubmitStatic")
    assert_name_loc = ("xpath", "//*[@id='header']/div/ul/li[1]")

    def __init__(self, driver, page_url=None, page_title=None):
        """初始化方法"""
        Action.__init__(self, driver, page_url, page_title)

    def switch_page_frame(self):
        """切换frame"""
        self.switch_frame(self.frame_loc)

    def click_login_by_password(self):
        """点击:密码登录标签"""
        # self.find_element(self.link_login_by_password_loc).click()
        self.click_element(self.link_login_by_password_loc)

    def input_login_name(self, name):
        """输入登录名"""
        self.send_keys(locator=self.input_name_loc, value=name)

    def input_login_password(self, password):
        """输入登录密码"""
        self.send_keys(locator=self.input_password_loc, value=password)

    def submit_login(self):
        """点击登录按钮提交登录信息"""
        self.find_element(self.submit_login_loc).click()

    def get_assert_name(self):
        """获取登录后的用户名"""
        return self.find_element(self.assert_name_loc).text

    def open(self):
        self._open(self.page_url, self.page_title)
