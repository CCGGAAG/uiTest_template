from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.get("http://sso.stable-test.bdfint.cn/#/login")

# 定位器，通过元素属性定位元素对象
account_loc = (By.NAME, "phone")
password_loc = (By.NAME, "smsCode")
vericode_loc = (By.ID, "loginVerifyCode")
submit_loc = (By.ID, "loginBtn")
login_loc = (By.XPATH, "//button[contains(text(),'登录')]")
login_iframe = "1"

# driver.switch_to.frame(login_iframe)
driver.find_element(By.NAME, "phone").send_keys("12025201314")
driver.find_element(By.NAME, "smsCode").send_keys("8888")
driver.find_element(By.XPATH, "//button[contains(text(),'登录')]").click()
sleep(3)

driver.get("http://wl.stable-test.bdfint.cn/goodsSource/goodsDetail/chatDetail/?id=543c54ed1fdb49909e14e101c6633a8d&leftAmount=111.000")
sleep(5)
print("000000000000000000000000000000000000000000000000000000000000000")
print(driver.page_source)
driver.find_element(By.XPATH, "//*[@id='payType']").click()

sleep(2)
driver.find_element(By.XPATH, "//li[contains(text(),'线下支付')]").click()
sleep(3)

print("1111111111111111111111111111111111111111111111111111111111111111")
print(driver.page_source)
driver.find_element(By.XPATH, "//*[@id='invoiceType']").click()
sleep(2)
driver.find_element(By.XPATH, "//li[contains(text(),'增票')]").click()
sleep(2)
print("22222222222222222222222222222222222222222222222222222222222222")
print(driver.page_source)