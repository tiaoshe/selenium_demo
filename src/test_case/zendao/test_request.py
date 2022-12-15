import random
import requests

import pytest

test_user_data = ["admin1", "admin2"]
test_user_dic = [
    {"username": "张三", "password": "122345"},
    {"username": "李四", "password": "122345"},

]
i = 0


@pytest.fixture(scope="module")
def login(request):
    user = request.param
    global i
    i += 1
    print('这个会打印两次,用i的值记录i=：%s' % i)
    print("登录账户：%s" % user)
    return user


@pytest.mark.parametrize("fun_c", test_user_dic, indirect=True)
def test_login(fun_c):
    '''登录用例'''
    a = fun_c
    print("测试用例中login的返回值:%s" % a)
    assert a != ""
    return 1


@pytest.mark.one
def test_haha():
    print(1)


@pytest.mark.one
def test_haha1():
    print(2)


# @pytest.mark.flaky()
def test_haha2():
    num = random.randint(1, 100)
    r = requests.get("http://www.baidu.com")


if __name__ == "__main__":
    pytest.main(["-vs", "test_request.py::test_haha2", "--reruns=2"])
