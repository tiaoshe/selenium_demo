import re
import pytest
import hashlib
from common.util import get_root_path
from common.F_loader import load_csv
from src.api.zendao.test_api_zendao import ZendaoApi
from common.F_check import check_resout

assert_list = [{'check': 'status_code', 'assert': 'equals', 'expect': 200, 'msg': 'assert response status code'}]

file_path = get_root_path() + r"/data/csvdata/user1.csv"
user_list = load_csv(file_path)


def get_md5_password(refyrand, password):
    password = password
    a = hashlib.md5(password.encode()).hexdigest() + refyrand
    b = hashlib.md5(a.encode()).hexdigest()
    return b


@pytest.mark.parametrize('params', user_list)
def test_login(params):
    # 实例化接口worker
    woker = ZendaoApi()
    kwargs = dict()
    headers = {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate',
               'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
               'Connection': 'keep-alive', 'Host': '192.168.1.3:8088',
               'Referer': 'http://192.168.1.3:8088/zentao/user-login.html',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0',
               'X-Requested-With': 'XMLHttpRequest'}
    kwargs['headers'] = headers
    response = woker.zentao_user_refreshRandom(**kwargs)
    ret = re.match("zentaosid=(.*?);", response.headers['Set-Cookie'])
    zentaoid = ret.group()
    headers['Cookie'] = zentaoid
    kwargs['headers'] = headers
    body_data = dict()
    body_data['account'] = params['username']
    body_data['password'] = get_md5_password(response.text, params['password'])
    body_data['passwordStrength'] = 1
    body_data['referer'] = "/zentao/"
    body_data['verifyRand'] = response.text
    body_data['keepLogin'] = 0
    body_data['captcha'] = ""
    kwargs['data'] = body_data
    response = woker.zentao_user_login(**kwargs)
    # 检查数据正确性
    check_resout(response, assert_list, params=params)


def login():
    # 实例化接口worker
    woker = ZendaoApi()
    kwargs = dict()
    headers = {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate',
               'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
               'Connection': 'keep-alive', 'Host': '192.168.1.3:8088',
               'Referer': 'http://192.168.1.3:8088/zentao/user-login.html',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0',
               'X-Requested-With': 'XMLHttpRequest'}
    kwargs['headers'] = headers
    response = woker.zentao_user_refreshRandom(**kwargs)
    ret = re.match("zentaosid=(.*?);", response.headers['Set-Cookie'])
    zentaoid = ret.group()
    headers['Cookie'] = zentaoid
    kwargs['headers'] = headers
    body_data = dict()
    body_data['account'] = "howell"
    body_data['password'] = get_md5_password(response.text, "howell3901")
    body_data['passwordStrength'] = 1
    body_data['referer'] = "/zentao/"
    body_data['verifyRand'] = response.text
    body_data['keepLogin'] = 0
    body_data['captcha'] = ""
    kwargs['data'] = body_data
    woker.zentao_user_login(**kwargs)
    return headers


if __name__ == '__main__':
    login()
