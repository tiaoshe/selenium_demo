import re
import pytest
import hashlib
from src.api.zendao.test_api_zendao import ZendaoApi


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    print("----------------------")
    # 获取常规的钩子方法的调用结果，返回一个result对象
    out = yield
    print('用例的执行结果', out)
    # 获取调用结果的测试报告，返回一个report对象，report对象的属性包括以下
    # 包括when（setup、call、teardown三个值）、nodeid（测试用例的名字）、
    # outcome(用例执行的结果。passed、failed)
    report = out.get_result()
    if report.when == "call":
        print('测试报告：%s' % report)
        print('步骤：%s' % report.when)
        print("nodeid:%s" % report.nodeid)
        print("description%s" % str(item.function.__doc__))
        print("运行结果：%s" % report.outcome)


@pytest.fixture(scope="session", autouse=True)
def fix_a():
    """
    scope=session 这个fixture在项目只会启动一次，一般用来做项目级的环境的初始化和清理操作
    autouse=True 代表自动运行，不需要用例主动去调用
    当setup执行结果failed，后面的call用例不会再执行，teardown还是会执行，此时用例状态是error，
    也就是用例call都还没开始执行，就异常了

    call失败的情况   setup正常执行，但是测试用例call失败了，运行结果是failed

    teardown运行失败的情况， setup call正常执行，teardown失败了

    如果保证setup和teardown不报错的情况，只关注测试用例本身的运行结果，可以加个判断：
    if report.when == "call" 只取call的结果
    :return:
    """
    print("setup 前置操作")
    yield
    print("teardown 后置操作")


@pytest.fixture(scope="module")
def fun_c(request):
    username = request.param['username']
    password = request.param['password']
    print(username, password)
    yield "ordlookup"
    print("后置处理")


def get_md5_password(refyrand, password):
    password = password
    a = hashlib.md5(password.encode()).hexdigest() + refyrand
    b = hashlib.md5(a.encode()).hexdigest()
    return b


@pytest.fixture(scope="module")
def login():
    worker = ZendaoApi()
    kwargs = dict()
    headers = {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate',
               'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
               'Connection': 'keep-alive', 'Host': '192.168.1.3:8088',
               'Referer': 'http://192.168.1.3:8088/zentao/user-login.html',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0',
               'X-Requested-With': 'XMLHttpRequest'}
    kwargs['headers'] = headers
    response = worker.zentao_user_refreshRandom(**kwargs)
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
    worker.zentao_user_login(**kwargs)
    return worker
