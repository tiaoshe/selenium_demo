import pytest
from common.F_loader import load_csv_to_key
from common.util import get_root_path
from src.api.zendaoo.test_api_shengmeijia import Zendao

assert_list = [{'check': 'status_code', 'assert': 'equals', 'expect': 200, 'msg': 'assert response status code'},
               {'check': 'headers.Content-Type', 'assert': 'equals',
                'expect': 'text/html; Language=UTF-8;charset=UTF-8', 'msg': 'assert response header Content-Type'}]

file_path = r'D:\workspace\selenium_demo\data\csvdata\TestZentaoUserLogin_data.csv'
data_dict = load_csv_to_key(file_path)


class TestZentaoUserLogin(object):
    headers = {'Host': '192.168.1.3:8088',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0',
               'Accept': 'application/json, text/javascript, */*; q=0.01',
               'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
               'Accept-Encoding': 'gzip, deflate', 'Referer': 'http://192.168.1.3:8088/zentao/user-login.html',
               'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8', 'X-Requested-With': 'XMLHttpRequest',
               'Content-Length': '138', 'Origin': 'http://192.168.1.3:8088', 'Connection': 'keep-alive'}
    worker = None

    @classmethod
    def setup_class(cls):
        cls.worker = Zendao()

    @pytest.mark.parametrize("account", data_dict['account'])
    def test_zentao_user_login_account(self, account):
        kwargs = dict()
        kwargs['headers'] = TestZentaoUserLogin.headers
        data = dict()
        data['account'] = account['account']
        data['password'] = account['password']
        data['passwordStrength'] = account['passwordStrength']
        data['referer'] = account['referer']
        data['verifyRand'] = account['verifyRand']
        data['keepLogin'] = account['keepLogin']
        data['captcha'] = account['captcha']
        kwargs['json'] = data
        TestZentaoUserLogin.worker.zentao_user_login(**kwargs)

    @pytest.mark.parametrize("password", data_dict['password'])
    def test_zentao_user_login_password(self, password):
        kwargs = dict()
        kwargs['headers'] = TestZentaoUserLogin.headers
        data = dict()
        data['account'] = password['account']
        data['password'] = password['password']
        data['passwordStrength'] = password['passwordStrength']
        data['referer'] = password['referer']
        data['verifyRand'] = password['verifyRand']
        data['keepLogin'] = password['keepLogin']
        data['captcha'] = password['captcha']
        kwargs['json'] = data
        TestZentaoUserLogin.worker.zentao_user_login(**kwargs)

    @pytest.mark.parametrize("passwordStrength", data_dict['passwordStrength'])
    def test_zentao_user_login_passwordStrength(self, passwordStrength):
        kwargs = dict()
        kwargs['headers'] = TestZentaoUserLogin.headers
        data = dict()
        data['account'] = passwordStrength['account']
        data['password'] = passwordStrength['password']
        data['passwordStrength'] = passwordStrength['passwordStrength']
        data['referer'] = passwordStrength['referer']
        data['verifyRand'] = passwordStrength['verifyRand']
        data['keepLogin'] = passwordStrength['keepLogin']
        data['captcha'] = passwordStrength['captcha']
        kwargs['json'] = data
        TestZentaoUserLogin.worker.zentao_user_login(**kwargs)

    @pytest.mark.parametrize("referer", data_dict['referer'])
    def test_zentao_user_login_referer(self, referer):
        kwargs = dict()
        kwargs['headers'] = TestZentaoUserLogin.headers
        data = dict()
        data['account'] = referer['account']
        data['password'] = referer['password']
        data['passwordStrength'] = referer['passwordStrength']
        data['referer'] = referer['referer']
        data['verifyRand'] = referer['verifyRand']
        data['keepLogin'] = referer['keepLogin']
        data['captcha'] = referer['captcha']
        kwargs['json'] = data
        TestZentaoUserLogin.worker.zentao_user_login(**kwargs)

    @pytest.mark.parametrize("verifyRand", data_dict['verifyRand'])
    def test_zentao_user_login_verifyRand(self, verifyRand):
        kwargs = dict()
        kwargs['headers'] = TestZentaoUserLogin.headers
        data = dict()
        data['account'] = verifyRand['account']
        data['password'] = verifyRand['password']
        data['passwordStrength'] = verifyRand['passwordStrength']
        data['referer'] = verifyRand['referer']
        data['verifyRand'] = verifyRand['verifyRand']
        data['keepLogin'] = verifyRand['keepLogin']
        data['captcha'] = verifyRand['captcha']
        kwargs['json'] = data
        TestZentaoUserLogin.worker.zentao_user_login(**kwargs)

    @pytest.mark.parametrize("keepLogin", data_dict['keepLogin'])
    def test_zentao_user_login_keepLogin(self, keepLogin):
        kwargs = dict()
        kwargs['headers'] = TestZentaoUserLogin.headers
        data = dict()
        data['account'] = keepLogin['account']
        data['password'] = keepLogin['password']
        data['passwordStrength'] = keepLogin['passwordStrength']
        data['referer'] = keepLogin['referer']
        data['verifyRand'] = keepLogin['verifyRand']
        data['keepLogin'] = keepLogin['keepLogin']
        data['captcha'] = keepLogin['captcha']
        kwargs['json'] = data
        TestZentaoUserLogin.worker.zentao_user_login(**kwargs)

    @pytest.mark.parametrize("captcha", data_dict['captcha'])
    def test_zentao_user_login_captcha(self, captcha):
        kwargs = dict()
        kwargs['headers'] = TestZentaoUserLogin.headers
        data = dict()
        data['account'] = captcha['account']
        data['password'] = captcha['password']
        data['passwordStrength'] = captcha['passwordStrength']
        data['referer'] = captcha['referer']
        data['verifyRand'] = captcha['verifyRand']
        data['keepLogin'] = captcha['keepLogin']
        data['captcha'] = captcha['captcha']
        kwargs['json'] = data
        TestZentaoUserLogin.worker.zentao_user_login(**kwargs)
