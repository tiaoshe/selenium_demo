import pytest


def test_case01(tmpdir):
    """
    这是用例的描述 巴拉巴拉巴拉
    :return:
    """
    print(tmpdir)
    print("用例运行时")
    print("z我是李杰")
    print("用例运行时")
    # raise SystemExit(1)
    assert 0


if __name__ == '__main__':
    pytest.main(['-s'])
