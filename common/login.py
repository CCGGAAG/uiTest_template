from selenium.webdriver.common.by import By
from common.loadyaml import get_account_info
from time import sleep
from common.log import Logger
auto_log = Logger()


class Login():
    """统一的登录方法"""
    def __init__(self, driver, user_name="chenyixin"):
        """
        初始化：入参：driver、user_name
        """
        self.driver = driver
        self.account_info = get_account_info(user_name)
        self.account = self.account_info["username"]
        self.password = self.account_info["password"]
        self.vericode = self.account_info["vericode"]
        self.username = self.account_info["cnname"]
        self.username_loc = (By.XPATH, "//a[contains(text(),'%s')]" % self.username)

    # 定位器，通过元素属性定位元素对象
    account_loc = (By.ID, "accountName")
    password_loc = (By.ID, "loginPassword")
    vericode_loc = (By.ID, "loginVerifyCode")
    submit_loc = (By.ID, "loginBtn")
    login_iframe = "loginIframe"
    login_url = "http://cenpur-stable-test.bdfint.cn/login"
    quit_loc = (By.XPATH, "//span[contanins(text(),'退出登录')]")

    def open_url(self):
        self.driver._open(self.login_url, "中联钢信")

    def change_iframe(self):
        """切换iframe"""
        self.driver.switch_frame(self.login_iframe)

    def input_username(self):
        """调用send_keys对象，输入用户名"""
        self.driver.find_element(*self.account_loc).send_keys(self.account)

    def input_password(self):
        """调用send_keys对象，输入密码"""
        self.driver.find_element(*self.password_loc).send_keys(self.password)

    def input_vericode(self):
        """调用send_keys对象，输入验证码"""
        self.driver.find_element(*self.vericode_loc).send_keys(self.vericode)

    def click_submit(self):
        """调用click对象，点击登录"""
        self.driver.find_element(*self.submit_loc).click()

    def find_username(self):
        """登录成功页面中查找用户名字"""
        return self.driver.find_element(*self.username_loc).text

    def click_quit(self):
        """点击退出"""
        self.driver.find_element(*self.quit_loc).click()

    def switch_defult_frame(self):
        """切换主frame"""
        self.driver.switch_default_frame()

    def login(self):
        self.open_url()
        # 切换iframe
        self.change_iframe()
        sleep(0.5)
        # 调用用户名输入组件
        self.input_username()
        # 调用密码输入组件
        self.input_password()
        # 调用验证码输入组件
        self.input_vericode()
        sleep(2)
        # 调用点击登录按钮组件
        self.click_submit()
        sleep(2)

    def quit(self):
        """退出登录"""
        self.click_quit()
        sleep(1)

