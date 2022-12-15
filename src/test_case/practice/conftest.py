import pytest



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