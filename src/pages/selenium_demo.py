import random

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
import time

# 没有配置环境变量
driver = webdriver.PhantomJS(executable_path=r"D:\Program Files\phantomjs-2.1.1-windows\bin\phantomjs.exe")
# 配置了环境变量
# driver = webdriver.PhantomJS()
# 设置隐士等待
driver.implicitly_wait(10)
driver.get("http://www.baidu.com")
time.sleep(1)
data = driver.find_element_by_id("wrapper").text
# 打印数据内容
# print(data)
# print(driver.title)
screen_name = "howell截图" + str(random.randint(1, 1000)) + ".png"
driver.save_screenshot("img/%s" % screen_name)
# print(driver.page_source)
print(driver.get_cookies())
driver.find_element(By.ID, 'kw').send_keys('成都')
driver.find_element_by_id('kw').send_keys(Keys.CONTROL, 'a')
driver.find_element_by_id('kw').send_keys(Keys.CONTROL, 'x')
driver.find_element_by_id('kw').send_keys('java开发')
driver.find_element_by_id('su').click()
time.sleep(2)
driver.save_screenshot("img/%s" % "howell截图" + str(random.randint(1, 1000)) + ".png")
print(driver.current_url)
# 关闭当前页，如果只有一个页面，会关闭浏览器
driver.close()
# 关闭浏览器
# driver.quit()