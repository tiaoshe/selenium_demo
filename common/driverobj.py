from selenium import webdriver


def get_driver(browser):
    b = browser.lower()
    if b == "firefox":
        return webdriver.Firefox()
    elif b == "chrome":
        return webdriver.Chrome()
    elif b == "phantomjs":
        return webdriver.PhantomJS(executable_path=r"D:\Program Files\phantomjs-2.1.1-windows\bin\phantomjs.exe")
