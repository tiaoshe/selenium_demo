import sys

import pytest
#
#
# @pytest.hookimpl(hookwrapper=True)
# def pytest_collection(session):
#     print("当前运行" + sys._getframe().f_code.co_name)
#     print('启动测试采集器' + str(session))
#     result = yield
#     print('最终测试采集结果' + str(session.items))
#     print("结束运行" + sys._getframe().f_code.co_name)
#     print("\n")
#
#
# @pytest.hookimpl(hookwrapper=True)
# def pytest_collectstart(collector):
#     print("当前运行" + sys._getframe().f_code.co_name)
#     print("当前节点" + collector.nodeid)
#     result = yield
#     print("结束运行" + sys._getframe().f_code.co_name)
#     print("\n")
#
#
# @pytest.hookimpl(hookwrapper=True)
# def pytest_make_collect_report(collector):
#     print("当前运行" + sys._getframe().f_code.co_name)
#     result = yield
#     print("当前节点" + result.get_result().nodeid + ",采集结果：" + result.get_result().outcome + ",采集节点为：" + str(
#         result.get_result().result))
#     print("结束运行" + sys._getframe().f_code.co_name)
#     print("\n")
#
#
# @pytest.hookimpl(hookwrapper=True)
# def pytest_pycollect_makemodule(path, parent):
#     print("当前运行" + sys._getframe().f_code.co_name)
#     print('在目录' + str(parent.fspath) + '采集到测试脚本' + str(path))
#     result = yield
#     print('当前采集模块' + result.get_result().nodeid)
#     print("结束运行" + sys._getframe().f_code.co_name)
#     print("\n")
#
#
# @pytest.hookimpl(hookwrapper=True)
# def pytest_generate_tests(metafunc):
#     print("当前运行" + sys._getframe().f_code.co_name)
#     result = yield
#     print("结束运行" + sys._getframe().f_code.co_name)
#     print("\n")
#
#
# @pytest.hookimpl(hookwrapper=True)
# def pytest_collectreport(report):
#     print("当前运行" + sys._getframe().f_code.co_name)
#     print('在节点' + report.nodeid + '采集到' + str(report.result))
#     result = yield
#     print("结束运行" + sys._getframe().f_code.co_name)
#     print("\n")
#
#
# @pytest.hookimpl(hookwrapper=True)
# def pytest_collection_modifyitems(session, config, items):
#     print("当前运行" + sys._getframe().f_code.co_name)
#     result = yield
#     print('测试顺序为' + str(items))
#     print("结束运行" + sys._getframe().f_code.co_name)
#     print("\n")
#
#
# @pytest.hookimpl(hookwrapper=True)
# def pytest_collection_finish(session):
#     print("当前运行" + sys._getframe().f_code.co_name)
#     result = yield
#     print('用例采集完成')
#     print("结束运行" + sys._getframe().f_code.co_name)
#     print("\n")


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    print("----------------------")
    # 获取常规的钩子方法的调用结果，返回一个result对象
    out = yield
    print(dir(out))
    print('用例的执行结果', out)
    # 获取调用结果的测试报告，返回一个report对象，report对象的属性包括以下
    # 包括when（setup、call、teardown三个值）、nodeid（测试用例的名字）、
    # outcome(用例执行的结果。passed、failed)
    report = out.get_result()
    print('测试报告：%s' % report)
    print('步骤：%s' % report.when)
    print("nodeid:%s" % report.nodeid)
    print("description%s" % str(item.function.__doc__))
    print("运行结果：%s" % report.outcome)
    print("exception异常%s" % call.excinfo)
    print("这是错误日志：%s"% report.longrepr)
    print("duration用例耗时：%s"% report.duration)
    print(report.__dict__)
    print(dir(report))


# pytest_runtest_call

# @pytest.hookimpl()
# def pytest_runtest_call(item):
#     print("啊啊啊啊" * 50)
#     print(item)


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
