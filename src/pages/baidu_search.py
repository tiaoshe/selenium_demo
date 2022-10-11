from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

from common import driverobj


class BaiduSearch(object):
    def __init__(self):
        self.driver = driverobj.get_driver("chrome")
        self.driver.get("http://www.baidu.com")

    def find_element(self, location, ftype='id'):
        if ftype == 'id':
            element_obj = WebDriverWait(self.driver, 10, 0.5).until(lambda x: x.find_element(By.ID, location))
            return element_obj

    def search_input(self, word):
        element = self.find_element('kw')
        element.clear()
        element.send_keys(word)
        return element

    def search_button(self):
        element = self.find_element('su')
        element.click()
        return element
