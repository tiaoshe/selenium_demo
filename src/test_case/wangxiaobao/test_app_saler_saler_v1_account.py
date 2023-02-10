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
class TestAppSalerSalerV1Account(object):
    headers = {'Host': 'fandom-video.test.wangxiaobao.com', 'Accept': '*/*', 'Connection': 'keep-alive',
               'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_0_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Html5Plus/1.0 (Immersed/44) uni-app',
               'Content-Fft': '46aa178a098aefd28d7b020344d60a41&Q4NxNbRmujQiMiUxIVfG&1675750035385',
               'Accept-Language': 'zh-CN,zh-Hans;q=0.9', 'Accept-Encoding': 'gzip, deflate, br',
               'Cookie': 'sid_fandom-uniapp-gateway=s%3Aac3dGBF8SXuD_ft2MtNNkYrpMH43zpyR.AoU922tjHifn6%2FINWVWP3B5vDCnphyXE4SKaFuz3QX0'}

    worker = None

    @classmethod
    def setup_class(cls):
        cls.worker = Wangxiaobao()

    def test_app_saler_account(self):
        kwargs = dict()
        kwargs['headers'] = TestAppSalerSalerV1Account.headers
        data = dict()
        kwargs['data'] = data
        response = TestAppSalerSalerV1Account.worker.app_saler_saler_v1_account(**kwargs)
        print(response.json())
        check_resout(response, assert_list)


if __name__ == '__main__':
    pytest.main(["--html", "dududu/report.html"])
