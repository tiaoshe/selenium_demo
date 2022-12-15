import time

import pytest


def test_case01(tmpdir):
    time.sleep(2)
    """
    这是用例的描述 巴拉巴拉巴拉
    :return:
    """
    print(tmpdir)
    print("用例运行时")
    print("z我是李杰")
    print("用例运行时")
    # raise SystemExit(1)


def test_case02(tmpdir):
    time.sleep(2)
    """
    这是用例的描述 巴拉巴拉巴拉
    :return:
    """
    print(tmpdir)
    print("用例运行时")
    print("z我是李杰")
    print("用例运行时")
    # raise SystemExit(1)
    assert 1 == 2


@pytest.mark.smoke
def test_case03(tmpdir):
    time.sleep(2)
    """
    这是用例的描述 巴拉巴拉巴拉
    :return:
    """
    print(tmpdir)
    print("用例运行时")
    print("z我是李杰")
    print("用例运行时")
    # raise SystemExit(1)


def test_case04(tmpdir):
    time.sleep(2)
    """
    这是用例的描述 巴拉巴拉巴拉
    :return:
    """
    print(tmpdir)
    print("用例运行时")
    print("z我是李杰")
    print("用例运行时")
    # raise SystemExit(1)


if __name__ == '__main__':
    pytest.main(['-sv', "-n=2", "--reruns=2"])
