import sys

import pytest


#


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    # print("----------------------")
    # 获取常规的钩子方法的调用结果，返回一个result对象
    out = yield
    # print(dir(out))
    # print('用例的执行结果', out)
    # 获取调用结果的测试报告，返回一个report对象，report对象的属性包括以下
    # 包括when（setup、call、teardown三个值）、nodeid（测试用例的名字）、
    # outcome(用例执行的结果。passed、failed)
    report = out.get_result()
    if report.when == "call":
        # print('测试报告：%s' % report)
        # print('步骤：%s' % report.when)
        # print("nodeid:%s" % report.nodeid)
        # print("description%s" % str(item.function.__doc__))
        # print("运行结果：%s" % report.outcome)
        # print("exception异常%s" % call.excinfo)
        print("这是错误日志：%s" % report.longrepr)
        with open('op.txt', "w+",encoding="utf-8") as f:
            f.write(str(report.longrepr))
    # print("duration用例耗时：%s"% report.duration)
    # print(report.__dict__)
    # print(dir(report))
    print(1)
