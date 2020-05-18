from selenium import webdriver
from time import sleep

def test():
    driver = webdriver.Chrome()
    driver.get("https://jc.zsteel.cc/")
    driver.implicitly_wait(10)

    ele = driver.find_element_by_css_selector("li[class~=active-3zc9k]~li")
    print(ele)
    print(ele.text)

    js_sentence_light = "arguments[0].setAttribute('style', arguments[1]);"
    js_sentence_args = "color: yellow; border: 5px solid yellow;"
    driver.execute_script(js_sentence_light, ele, js_sentence_args)


if __name__ == "__main__":
    test()