import pytest
import allure
from common.F_loader import load_csv_to_key
from common.F_check import check_resout
from src.api.wangxiaobao.test_api_wangxiaobao import Wangxiaobao

assert_list = [{'check': 'status_code', 'assert': 'equals', 'expect': 200, 'msg': 'assert response status code'},
               {'check': 'headers.Content-Type', 'assert': 'equals', 'expect': 'application/json',
                'msg': 'assert response header Content-Type'}]

file_path = r''
data_dict = load_csv_to_key(file_path)


@allure.feature("测试模块")
class TestAppSalerSalerV1Info(object):
    headers = {'Host': 'fandom-video.test.wangxiaobao.com', 'Accept': '*/*', 'Connection': 'keep-alive',
               'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_0_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Html5Plus/1.0 (Immersed/44) uni-app',
               'Content-Fft': '5e01d16bda2ae78dfb29e120406d7491&CICWcMQ6QKwtLFZaNpDu&1675750035408',
               'Accept-Language': 'zh-CN,zh-Hans;q=0.9', 'Accept-Encoding': 'gzip, deflate, br'}
    worker = None

    @classmethod
    def setup_class(cls):
        cls.worker = Wangxiaobao()

    def test_app_saler_v1_info(self):
        kwargs = dict()
        kwargs['headers'] = TestAppSalerSalerV1Info.headers
        data = dict()
        kwargs['data'] = data
        response = TestAppSalerSalerV1Info.worker.app_saler_saler_v1_info(**kwargs)
        print(response.json())
        check_resout(response, assert_list)
