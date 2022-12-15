import allure
import pytest
from common.F_loader import load_csv_to_key
from common.F_check import check_resout
from src.api.shenmeijia.test_api_shengmeijia import Shengmeijia

assert_list = [{'check': 'status_code', 'assert': 'equals', 'expect': 200, 'msg': 'assert response status code'},
               {'check': 'headers.Content-Type', 'assert': 'equals', 'expect': 'application/json; charset=UTF-8',
                'msg': 'assert response header Content-Type'}]

file_path = r'D:\workspace\selenium_demo\data\csvdata\TestV1AccountLogin_data.csv'
data_dict = load_csv_to_key(file_path)


@allure.feature("登录模块-B端登录接口")
class TestV1AccountLogin(object):
    headers = {'Host': 'admin.xzsmjcs.com',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0',
               'Accept': 'application/json, text/plain, */*',
               'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
               'Accept-Encoding': 'gzip, deflate, br', 'Content-Type': 'application/json; charset=UTF-8',
               'Content-Length': '40', 'Origin': 'https://admin.xzsmjcs.com', 'Connection': 'keep-alive',
               'Referer': 'https://admin.xzsmjcs.com/admin/?', 'Sec-Fetch-Dest': 'empty', 'Sec-Fetch-Mode': 'cors',
               'Sec-Fetch-Site': 'same-origin'}
    worker = None

    @classmethod
    def setup_class(cls):
        cls.worker = Shengmeijia()

    @allure.story("登录功能验证")
    @allure.title("username-参数验证")
    @pytest.mark.parametrize("username", data_dict['username'])
    def test_v1_account_login_username(self, username):
        kwargs = dict()
        kwargs['headers'] = TestV1AccountLogin.headers
        data = dict()
        data['username'] = username['username']
        data['password'] = username['password']
        kwargs['json'] = data
        kwargs['verify'] = False
        response = TestV1AccountLogin.worker.v1_account_login(**kwargs)
        # 检查数据正确性
        check_resout(response, assert_list, jsondat=username)

    @allure.story("登录功能验证")
    @allure.title("password-参数验证")
    @pytest.mark.parametrize("password", data_dict['password'])
    def test_v1_account_login_password(self, password):
        kwargs = dict()
        kwargs['headers'] = TestV1AccountLogin.headers
        data = dict()
        data['username'] = password['username']
        data['password'] = password['password']
        kwargs['json'] = data
        kwargs['verify'] = False
        response = TestV1AccountLogin.worker.v1_account_login(**kwargs)
        # 检查数据正确性
        check_resout(response, assert_list, jsondat=password)
