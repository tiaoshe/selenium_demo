import os
import pytest
import allure
from src.pages.baidu_search import BaiduSearch
import time
from common import util
from common.howelllog import WriteLog


@allure.epic("百度搜索页")
class TestBaidu(object):
    def setup_class(self):
        self.bs = BaiduSearch()
        self.logger = WriteLog(__file__)

    def teardown_class(self):
        self.bs.driver.close()

    @allure.feature('搜索功能一')
    @pytest.mark.parametrize("search_content", ["成都", "重庆"])
    def test_search(self, search_content):
        self.bs.search_input(search_content)
        self.bs.search_button()
        self.logger.write("执行搜索测试搜索关键词:%s" % search_content)
        time.sleep(5)
        # 屏幕截图
        path = util.get_root_path() + r"\pictures\截图" + str(int(time.time())) + ".png"
        self.bs.driver.save_screenshot(path)
        # 校验
        assert search_content in self.bs.driver.page_source

    @allure.feature('搜索功能二')
    @pytest.mark.parametrize("search_content", ["上海", "北京"])
    # @pytest.mark.skip("reason no")
    def test_search1(self, search_content):
        self.bs.search_input(search_content)
        self.bs.search_button()
        self.logger.write("执行搜索测试搜索关键词:%s" % search_content)
        time.sleep(5)
        # 屏幕截图
        path = util.get_root_path() + r"\pictures\截图" + str(int(time.time())) + ".png"
        self.bs.driver.save_screenshot(path)
        # 校验
        assert search_content in self.bs.driver.page_source
        assert 1 == 2


if __name__ == '__main__':
    # pytest.main(["-s","allure-test.py"])
    '''
    -q: 安静模式, 不输出环境信息
    -v: 丰富信息模式, 输出更详细的用例执行信息
    -s: 显示程序中的print/logging输出
    添加参数： --alluredir ../../Reports/allure
    '''
    pytest.main(["--alluredir", '../../Reports/allure', 'test_search.py', ])
    # os.system(r"allure generate -c -o allure-report")
