import pytest

def test_01():
    print("测试用例 test_01")
    assert 1 == 1

@pytest.mark.skip("跳过用例")
def test_02():
    print("测试用例 test_02")
    assert 1 == 2

def test_03():
    print("测试用例 test_03")
    assert 1 == 2

def test_04():
    print("测试用例 test_04", 1/0)
    assert 1 == 1
